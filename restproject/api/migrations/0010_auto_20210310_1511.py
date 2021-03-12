# Generated by Django 3.1.7 on 2021-03-10 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='type',
            field=models.CharField(choices=[('email', 'email'), ('phone', 'phone'), ('address', 'address')], default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='api.branch'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='info',
            field=models.CharField(default='phone', max_length=40),
        ),
    ]