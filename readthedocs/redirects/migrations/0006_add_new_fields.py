# Generated by Django 4.2.5 on 2023-10-31 17:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("redirects", "0005_allow_to_force_redirects"),
    ]

    operations = [
        migrations.AddField(
            model_name="redirect",
            name="description",
            field=models.CharField(
                blank=True,
                max_length=255,
                verbose_name="Description",
                null=True,
                default="",
            ),
        ),
        migrations.AddField(
            model_name="redirect",
            name="enabled",
            field=models.BooleanField(
                default=True,
                help_text="Enable or disable the redirect.",
                verbose_name="Enabled",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="redirect",
            name="position",
            field=models.PositiveIntegerField(
                default=0,
                help_text="Order of execution of the redirect.",
            ),
        ),
        migrations.AlterField(
            model_name="redirect",
            name="http_status",
            field=models.SmallIntegerField(
                choices=[
                    (302, "302 - Temporary Redirect"),
                    (301, "301 - Permanent Redirect"),
                ],
                default=302,
                verbose_name="HTTP status code",
            ),
        ),
        migrations.AlterField(
            model_name="redirect",
            name="status",
            field=models.BooleanField(choices=[], default=True, null=True),
        ),
        migrations.AlterField(
            model_name="redirect",
            name="redirect_type",
            field=models.CharField(
                choices=[
                    ("page", "Page Redirect"),
                    ("exact", "Exact Redirect"),
                    ("clean_url_to_html", "Clean URL to HTML (file/ to file.html)"),
                    ("html_to_clean_url", "HTML to clean URL (file.html to file/)"),
                ],
                help_text="The type of redirect you wish to use.",
                max_length=255,
                verbose_name="Redirect Type",
            ),
        ),
    ]
