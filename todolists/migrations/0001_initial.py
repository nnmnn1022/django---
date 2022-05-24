# Generated by Django 3.2.13 on 2022-05-24 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoListModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='수정일시')),
                ('checkbox', models.BooleanField(verbose_name='완료 여부')),
                ('content', models.CharField(max_length=64, verbose_name='할 일')),
                ('content_detail', models.TextField(verbose_name='세부내용')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todolist_writer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
