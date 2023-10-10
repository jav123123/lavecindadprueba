# Generated by Django 4.2.4 on 2023-10-06 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vecindad', '0009_rename_fecha_solicitud_mensaje_solicitud_fecha_hora'),
    ]

    operations = [
        migrations.CreateModel(
            name='MensajeModal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asunto', models.TextField()),
                ('contenido', models.TextField()),
                ('fecha_envio', models.DateTimeField(auto_now_add=True)),
                ('emisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajes_enviados', to='vecindad.mensaje')),
                ('receptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajes_recibidos', to='vecindad.mensaje')),
            ],
        ),
    ]