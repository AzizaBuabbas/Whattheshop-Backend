# Generated by Django 2.1 on 2019-09-15 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LanguageCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('course_overview', models.TextField()),
                ('logo', models.ImageField(blank=True, null=True, upload_to='Language_Course')),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]
