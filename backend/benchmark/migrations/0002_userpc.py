# Generated by Django 5.0.4 on 2024-04-23 18:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benchmark', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ram', models.IntegerField()),
                ('storage', models.IntegerField()),
                ('cpu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='benchmark.cpu')),
                ('gpu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='benchmark.gpu')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
