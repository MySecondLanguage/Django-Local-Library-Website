# Generated by Django 2.1.5 on 2019-03-02 17:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.UUID('322c8d80-aa4b-41d2-ac23-1f907fbf04f5'), primary_key=True, serialize=False),
        ),
    ]
