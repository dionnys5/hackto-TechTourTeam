# Generated by Django 2.2.6 on 2019-10-04 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import rotas.models


class Migration(migrations.Migration):

    dependencies = [
        ('rotas', '0006_auto_20191004_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arquivoimagem',
            name='arquivo',
            field=models.FileField(upload_to=rotas.models.diretorio_imagens_destino),
        ),
        migrations.AlterField(
            model_name='rota',
            name='destinos',
            field=models.ManyToManyField(related_name='destinos', through='rotas.DestinoDeRota', to='rotas.Destino', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='rota',
            name='proprietario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]
