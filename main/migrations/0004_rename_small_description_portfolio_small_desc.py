# Generated by Django 5.1.7 on 2025-03-15 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_portfolio_small_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='small_description',
            new_name='small_desc',
        ),
    ]
