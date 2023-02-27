# Generated by Django 4.1.5 on 2023-01-25 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('small_app', '0005_alter_calc_img'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='calc',
            options={'ordering': ['completed']},
        ),
        migrations.RemoveField(
            model_name='calc',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='calc',
            name='img',
        ),
        migrations.RemoveField(
            model_name='calc',
            name='num1',
        ),
        migrations.RemoveField(
            model_name='calc',
            name='num2',
        ),
        migrations.RemoveField(
            model_name='calc',
            name='total',
        ),
        migrations.AddField(
            model_name='calc',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='calc',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='calc',
            name='title',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='calc',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
