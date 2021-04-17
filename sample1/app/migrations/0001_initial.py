# Generated by Django 3.2 on 2021-04-17 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('emp_name', models.CharField(max_length=200)),
                ('emp_designation', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]