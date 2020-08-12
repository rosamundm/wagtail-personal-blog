from django import forms
from django.db import models

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.core.models import Page, Orderable
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtailcodeblock.blocks import CodeBlock

from wagtail.core.fields import StreamField, RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet

from .blocks import MyStream
from wagtail_markdown.utils import MarkdownPanel, MarkdownField

from markdown import markdown


from wagtailmarkdownblock.blocks import MarkdownBlock


class TextPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

# models for BlogIndexPage and BlogPageTag need to come before BlogPage
class BlogIndexPage(Page):
    body = RichTextField(blank=True)

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        blogpages = BlogPage.objects.live().public().order_by('-date')

        if request.GET.get('tag', None):
            tags = request.GET.get('tag')
            blogpages = blogpages.filter(tags__slug__in=[tags])

        context['blogpages'] = blogpages
        return context

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]



class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


# model for BlogPage itself:
class BlogPage(Page):
    date = models.DateField("Post date")
    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)

#    search_fields = Page.search_fields + [
 #       index.SearchField('body'),
  #  ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="Blog information"),
        FieldPanel("body"),  
    ]


class BlogTagIndexPage(Page):
    def get_context(self, request):

        # filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context


class StreamBlogPage(BlogPage):
    template = "blog/stream_blog_page.html"

    contents = StreamField(
        MyStream(),
        verbose_name = "My Stream",
        blank=True,
	null=True,
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
           FieldPanel('date'),
           FieldPanel('tags'),
           FieldPanel('categories', widget=forms.CheckboxSelectMultiple)],
           heading = "Blog information"),
        StreamFieldPanel("contents"),
    ]

    class Meta:
        verbose_name = "Stream blog page"


class StreamTextPage(Page):
    template = "blog/stream_text_page.html"
    body = RichTextField(blank=True)
    contents = StreamField(
        MyStream(),
        verbose_name = "My Stream",
        blank=True,
        null=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        StreamFieldPanel("contents"),
    ]




@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name

