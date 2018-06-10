# Generated by Django 2.0.6 on 2018-06-07 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0006_auto_20180607_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('F', 'First Player to Move'), ('L', 'Second Player Wins'), ('W', 'First Player Wins'), ('S', 'Second Player to Move'), ('D', 'Draw')], default='F', max_length=1),
        ),
    ]
