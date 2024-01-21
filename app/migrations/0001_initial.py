# Generated by Django 5.0 on 2024-01-02 09:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('blog_date', models.DateField()),
                ('poster', models.ImageField(upload_to='movie')),
                ('release_date', models.DateField()),
                ('story', models.TextField()),
                ('review', models.TextField()),
                ('movie_rating', models.DecimalField(decimal_places=1, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30)),
                ('comment', models.TextField()),
                ('comment_date', models.DateField(auto_now=True)),
                ('user_rating', models.DecimalField(decimal_places=1, max_digits=5)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.movie')),
            ],
        ),
    ]