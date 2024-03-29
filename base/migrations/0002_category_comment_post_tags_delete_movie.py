# Generated by Django 5.0.1 on 2024-02-01 12:07

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(blank=True, max_length=255)),
                ('content', models.TextField()),
                ('excerpt', models.TextField()),
                ('draft_status', models.CharField(choices=[('DRAFT', 'Draft'), ('PUBLISHED', 'Published')], default='PUBLISHED', max_length=255)),
                ('publish_date', models.DateTimeField(auto_now=True)),
                ('likes', models.IntegerField(default=0)),
                ('views', models.IntegerField(blank=True, default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(to='base.category')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.comment')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
    ]
