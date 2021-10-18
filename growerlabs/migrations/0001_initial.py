# Generated by Django 3.2.8 on 2021-10-08 14:52

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('bio', models.TextField(blank=True, null=True)),
                ('dp', models.ImageField(blank=True, default='/dp/luna.jpg', null=True, upload_to='dp')),
                ('github_link', models.URLField(null=True)),
                ('portfolio_link', models.URLField(null=True)),
                ('insta_link', models.URLField(null=True)),
                ('linkedin_link', models.URLField(null=True)),
                ('prof_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='project')),
                ('project_github_link', models.URLField(null=True)),
                ('website_link', models.URLField(null=True)),
                ('contributors', models.ManyToManyField(related_name='contributors', to='growerlabs.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.ManyToManyField(related_name='skills', to='growerlabs.Skill'),
        ),
    ]