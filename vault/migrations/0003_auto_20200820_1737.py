# Generated by Django 3.0.5 on 2020-08-20 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vault', '0002_movie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='Top',
            new_name='top',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='Toprated',
            new_name='toprated',
        ),
        migrations.AddField(
            model_name='series',
            name='top',
            field=models.BooleanField(default='False'),
        ),
    ]