# Generated by Django 3.1.7 on 2021-03-09 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210309_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(choices=[('email', 'email'), ('phone', 'phone'), ('address', 'address')], default='phone', max_length=40)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.branch')),
            ],
        ),
    ]