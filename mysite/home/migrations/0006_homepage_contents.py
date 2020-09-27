# Generated by Django 3.0.4 on 2020-07-26 13:21

import blog.blocks
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_auto_20200312_2118"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="contents",
            field=wagtail.core.fields.StreamField(
                [
                    ("paragraph", blog.blocks.ParaBlock()),
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
                    ("html", blog.blocks.HTMLBlock()),
                ],
                blank=True,
                null=True,
                verbose_name="My Stream",
            ),
        ),
    ]
