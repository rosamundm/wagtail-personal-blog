# Generated by Django 3.0.4 on 2020-07-25 20:55

import blog.blocks
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="streamblogpage",
            name="contents",
            field=wagtail.core.fields.StreamField(
                [
                    ("paragraph", blog.blocks.ParaBlock()),
                    (
                        "image",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                (
                                    "caption",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                            ]
                        ),
                    ),
                    (
                        "code",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "language",
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[
                                            ("bash", "Bash/Shell"),
                                            ("css", "CSS"),
                                            ("diff", "diff"),
                                            ("html", "HTML"),
                                            ("javascript", "Javascript"),
                                            ("json", "JSON"),
                                            ("python", "Python"),
                                            ("scss", "SCSS"),
                                            ("yaml", "YAML"),
                                        ],
                                        help_text="Coding language",
                                        identifier="language",
                                        label="Language",
                                    ),
                                ),
                                (
                                    "code",
                                    wagtail.core.blocks.TextBlock(
                                        identifier="code", label="Code"
                                    ),
                                ),
                            ]
                        ),
                    ),
                ],
                blank=True,
                null=True,
                verbose_name="My Stream",
            ),
        ),
    ]
