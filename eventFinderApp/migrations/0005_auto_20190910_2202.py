# Generated by Django 2.2 on 2019-09-10 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventFinderApp', '0004_auto_20190910_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='event',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='eventFinderApp.Event'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='venue',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
