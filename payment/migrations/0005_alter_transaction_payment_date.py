# Generated by Django 4.0.2 on 2022-02-04 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_alter_transaction_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='payment_date',
            field=models.DateField(),
        ),
    ]
