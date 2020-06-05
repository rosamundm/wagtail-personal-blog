from wagtail.core import blocks
from wagtail.core.blocks import (
    CharBlock, ChoiceBlock, RichTextBlock, StreamBlock,
StructBlock, TextBlock, DateBlock
)
from wagtail.images.blocks import ImageChooserBlock
from wagtailcodeblock.blocks import CodeBlock


class TitleBlock(blocks.CharBlock):
    title = CharBlock(classname="post_title", required=True)
    template = "streams/title_block.html"

    class Meta:
        icon = "title"
        template = "streams/title_block.html"

class ParaBlock(blocks.RichTextBlock):
    paragraph = RichTextBlock(classname="post_text", required=True)
    editor = "default"

    class Meta:
        template = "streams/para_block.html"

class PicBlock(blocks.StructBlock):
    image = ImageChooserBlock(classname="post_image", required=False)
    caption = CharBlock(required=False)
  
    class Meta:
        icon = "image"
        template = "streams/pic_block.html"


class DmyBlock(blocks.DateBlock):
    date = DateBlock(classname="post_date", required=True)
    format = "%d %B %Y"

    class Meta:
        template = "streams/date_block.html"

"""
class CodingBlock(blocks.StructBlock):
    code = CodeBlock(classname = "post_code", required=False)

    class Meta:
        template = "streams/templates/streams/code_block.html"

"""
# all blocks put together in one stream for use in blog/models:
class MyStream(blocks.StreamBlock):
    title = TitleBlock()
    paragraph = ParaBlock()
    image = PicBlock()
    date = DmyBlock()
    #code = CodeBlock()
