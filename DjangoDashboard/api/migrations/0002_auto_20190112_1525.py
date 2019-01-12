# Generated by Django 2.1.4 on 2019-01-12 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpointrequest',
            name='body',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='endpointrequest',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='endpointrequest',
            name='header',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='endpointrequest',
            name='method',
            field=models.CharField(choices=[(0, 'GET'), (1, 'HEAD'), (2, 'POST'), (3, 'PUT'), (4, 'DELETE'), (5, 'CONNECT'), (6, 'OPTIONS'), (7, 'TRACE'), (8, 'PATCH')], default='GET', max_length=10),
        ),
    ]