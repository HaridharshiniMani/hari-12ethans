# Generated by Django 5.0.4 on 2024-04-22 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISIN', models.IntegerField(max_length=20)),
                ('symbol', models.CharField(max_length=100)),
                ('date', models.IntegerField()),
                ('assetclass', models.CharField(max_length=15)),
                ('quantity', models.IntegerField(max_length=300)),
                ('marketprice', models.IntegerField(max_length=200)),
                ('costprice', models.IntegerField(max_length=200)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]