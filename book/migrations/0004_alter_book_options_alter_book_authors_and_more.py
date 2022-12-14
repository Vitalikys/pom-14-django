# Generated by Django 4.1 on 2022-09-08 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0004_alter_author_options_alter_author_name_and_more'),
        ('book', '0003_book_authors'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(blank=True, to='author.author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='book',
            name='count',
            field=models.IntegerField(default=10, verbose_name='Кількість'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(blank=True, max_length=256, verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(blank=True, max_length=128, verbose_name='Книги'),
        ),
    ]
