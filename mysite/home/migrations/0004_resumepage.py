# Generated by Django 5.1.4 on 2024-12-12 20:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_body'),
        ('wagtail_resume', '0015_alter_baseresumepage_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResumePage',
            fields=[
                ('baseresumepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtail_resume.baseresumepage')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtail_resume.baseresumepage',),
        ),
    ]