# Generated by Django 4.0.4 on 2022-05-15 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('afisha', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='afisha',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afisha.afisha', verbose_name='фильм'),
        ),
    ]