# Generated by Django 5.1.1 on 2024-10-02 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('station', '0005_alter_ticket_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
