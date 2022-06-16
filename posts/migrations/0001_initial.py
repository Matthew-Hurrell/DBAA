# Generated by Django 4.0.5 on 2022-06-16 08:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djrichtextfield.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('did', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('body', djrichtextfield.models.RichTextField(max_length=10000)),
                ('image', models.ImageField(blank=True, upload_to='post_images')),
                ('time', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
