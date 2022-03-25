# Generated by Django 4.0.3 on 2022-03-25 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0005_remove_comment_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='ekko',
            name='liked',
            field=models.ManyToManyField(blank=True, default=None, related_name='liked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ekko',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=10)),
                ('ekko', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.ekko')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
