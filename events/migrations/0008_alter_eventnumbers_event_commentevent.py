# Generated by Django 4.0.5 on 2022-06-19 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0007_alter_event_fee_alter_event_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventnumbers',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_numbers', to='events.event'),
        ),
        migrations.CreateModel(
            name='CommentEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', djrichtextfield.models.RichTextField(max_length=10000)),
                ('time', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_event', to='events.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
