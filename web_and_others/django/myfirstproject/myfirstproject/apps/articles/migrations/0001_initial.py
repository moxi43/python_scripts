# Generated by Django 3.0.1 on 2019-12-22 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200, verbose_name='Название статьи')),
                ('article_text', models.TextField(verbose_name='Текст статьи')),
                ('pub_date', models.DateTimeField(verbose_name='Дата Публикации')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50, verbose_name='Имя Автора')),
                ('comment_text', models.CharField(max_length=200, verbose_name='Текст комментария')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
            ],
        ),
    ]