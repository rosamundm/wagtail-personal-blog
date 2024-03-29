from django import forms
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    StreamFieldPanel,
)
from wagtail.snippets.models import register_snippet
from .blocks import MyStream


class TextPage(Page):
    """
    Basic text page model, suitable for non-blog post pages.
    """

    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body", classname="full"),
    ]


class BlogIndexPage(Page):
    """
    Return a list of blog posts.
    """

    body = RichTextField(blank=True)

    def get_context(self, request, *args, **kwargs):
        """
        In Wagtail, get_context() essentially stands in for a Django FBV.
        """
        context = super().get_context(request, *args, **kwargs)
        blogpages = BlogPage.objects.live().public().order_by("-date")
        page = request.GET.get("page")
        paginator = Paginator(blogpages, 5)

        try:
            blogpages = paginator.page(page)
        except PageNotAnInteger:
            blogpages = paginator.page(1)
        except EmptyPage:
            blogpages = paginator.page(paginator.num_pages)

        if request.GET.get("tag", None):
            tags = request.GET.get("tag")
            blogpages = blogpages.filter(tags__slug__in=[tags])

        context["blogpages"] = blogpages
        return context

    content_panels = Page.content_panels + [FieldPanel("body", classname="full")]


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        "BlogPage", related_name="tagged_items", on_delete=models.CASCADE
    )


class BlogPage(Page):
    """
    Regular blog post page (no streamfields).
    """

    body = RichTextField(blank=True)
    categories = ParentalManyToManyField("blog.BlogCategory", blank=True)
    date = models.DateField("Post date")
    last_modified = models.DateField("Last updated")
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("date"),
                FieldPanel("last_modified"),
                FieldPanel("tags"),
                FieldPanel("categories", widget=forms.CheckboxSelectMultiple),
            ],
            heading="Blog information",
        ),
        FieldPanel("body"),
    ]

    @property
    def preview_modes(self):
        return Page.DEFAULT_PREVIEW_MODES


class BlogTagIndexPage(Page):
    """
    Show all blog tags.
    """

    def get_context(self, request, *args, **kwargs):
        """
        Filter posts by tag.
        """
        tag = request.GET.get("tag")
        blogpages = BlogPage.objects.live().filter(tags__name=tag).order_by("-date")
        context = super().get_context(request, *args, **kwargs)
        context["blogpages"] = blogpages
        return context


class StreamBlogPage(BlogPage):
    """
    Blog post page with streamfield functionality.
    """

    template = "blog/stream_blog_page.html"

    contents = StreamField(
        MyStream(),
        verbose_name="My Stream",
        blank=True,
        null=True,
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("date"),
                FieldPanel("last_modified"),
                FieldPanel("tags"),
                FieldPanel("categories", widget=forms.CheckboxSelectMultiple),
            ],
            heading="Blog information",
        ),
        StreamFieldPanel("contents"),
    ]

    class Meta:
        verbose_name = "Stream blog page"


class StreamTextPage(Page):
    """
    Text page with streamfield functionality.
    """

    template = "blog/stream_text_page.html"
    body = RichTextField(blank=True)
    contents = StreamField(
        MyStream(),
        verbose_name="My Stream",
        blank=True,
        null=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body", classname="full"),
        StreamFieldPanel("contents"),
    ]


@register_snippet
class BlogCategory(models.Model):
    """
    Category for sorting blog posts.
    """

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=80, null=True)

    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name = "Categories"
