# Generated by Django 3.0.8 on 2021-04-03 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20210403_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='package',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Package'),
        ),
    ]