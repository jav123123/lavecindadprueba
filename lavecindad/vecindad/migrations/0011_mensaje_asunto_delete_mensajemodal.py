# Generated by Django 4.2.4 on 2023-10-06 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vecindad', '0010_mensajemodal'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje',
            name='asunto',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='MensajeModal',
        ),
    ]