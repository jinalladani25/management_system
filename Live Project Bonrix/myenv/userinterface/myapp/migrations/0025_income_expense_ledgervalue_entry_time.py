# Generated by Django 3.2.7 on 2021-10-19 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_alter_income_expense_ledgervalue_category_header'),
    ]

    operations = [
        migrations.AddField(
            model_name='income_expense_ledgervalue',
            name='entry_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]