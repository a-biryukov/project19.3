# Generated by Django 5.0.6 on 2024-06-21 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_blog_view_count_blog_views_count_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'permissions': [('can_edit_publication', 'Can edit publication'), ('can_edit_tittle', 'Can edit tittle'), ('can_edit_text', 'Can edit text'), ('can_edit_image', 'Can edit image')], 'verbose_name': 'Блог', 'verbose_name_plural': 'Блоги'},
        ),
    ]