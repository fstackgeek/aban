# Generated by Django 4.2.16 on 2024-11-29 12:20
from django.db import migrations

"""
Initialize the database with a user with id = 1, and a wallet with 100$ initial balance, for demo purposes.
"""


def populate_initial_data(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    user = User.objects.create_user(username='demo-user', password='P@ssw0rd')
    Wallet = apps.get_model('exchange', 'Wallet')
    Wallet.objects.create(user=user, dollar_balance=100)


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_initial_data),
    ]
