# Generated by Django 4.2.6 on 2023-10-18 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_project_link_alter_project_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Enlace'),
        ),
    ]
