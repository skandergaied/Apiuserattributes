# Generated by Django 5.1.3 on 2024-11-22 17:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attributes', models.JSONField(default=list)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
