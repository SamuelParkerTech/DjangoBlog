# Generated by Django 4.2.14 on 2024-07-22 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_comment_approved'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on']},
        ),
    ]
