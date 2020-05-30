# Generated by Django 3.0.4 on 2020-05-30 17:21

from django.db import migrations
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('blog', '0002_auto_20200530_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='contents',
            field=wagtail.core.fields.StreamField([('title', streams.blocks.TitleBlock()), ('paragraph', streams.blocks.ParaBlock()), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(classname='post_image', required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('date', streams.blocks.DmyBlock())], blank=True, null=True, verbose_name='My Stream'),
        ),
        migrations.DeleteModel(
            name='NewBlogPage',
        ),
    ]
