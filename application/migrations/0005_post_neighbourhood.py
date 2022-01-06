# Generated by Django 3.2.9 on 2022-01-06 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_remove_post_neighbourhood'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='neighbourhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='application.neighbourhood'),
        ),
    ]
