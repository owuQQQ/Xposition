# Generated by Django 2.2.4 on 2019-10-15 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0043_move_category_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supersense',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supersense', to='categories.ArticleCategory'),
        ),
    ]
