# Generated by Django 3.2.18 on 2023-03-16 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_app', '0002_alter_dish_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='category',
            field=models.CharField(choices=[('Супы', 'Супы'), ('Гарниры', 'Гарниры'), ('Главное блюдо', 'Главное блюдо'), ('Напитки', 'Напитки'), ('Закуски', 'Закуски'), ('Салаты', 'Салаты')], default='Супы', max_length=14),
        ),
    ]