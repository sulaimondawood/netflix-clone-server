# Generated by Django 5.0.1 on 2024-02-15 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(default=1, to='base.category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(default=1, to='base.tag'),
        ),
    ]
