# Generated by Django 4.0.2 on 2022-02-03 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_alter_payable_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='method',
            field=models.CharField(choices=[('debit_card', 'debit card'), ('credit_card', 'credit card'), ('cash', 'cash')], max_length=15),
        ),
    ]
