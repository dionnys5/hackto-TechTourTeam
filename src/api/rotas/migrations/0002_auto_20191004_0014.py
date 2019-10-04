# Generated by Django 2.2.6 on 2019-10-04 03:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import rotas.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rotas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArquivoImagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.FileField(upload_to=rotas.models.diretorio_imagens_destino)),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('eh_sustentavel', models.NullBooleanField()),
                ('tem_bom_atendimento', models.NullBooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='AvaliacoesDeDestino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avaliacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rotas.Avaliacao')),
            ],
        ),
        migrations.CreateModel(
            name='Destino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250, verbose_name='Nome')),
                ('descricao', models.TextField()),
                ('custo_estimado', models.FloatField()),
                ('tempo_estimado', models.FloatField()),
                ('imagem_destaque', models.FileField(upload_to=rotas.models.diretorio_imagens_destino_destaque, verbose_name='Imagem destaque')),
                ('pontuacao_checkin', models.IntegerField()),
                ('avaliacoes', models.ManyToManyField(through='rotas.AvaliacoesDeDestino', to='rotas.Avaliacao', verbose_name='Avaliações')),
            ],
        ),
        migrations.CreateModel(
            name='ImagensDestino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rotas.ArquivoImagem')),
                ('destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rotas.Destino')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=300, verbose_name='Nome completo')),
                ('idade', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=11)),
                ('escolaridade', models.CharField(choices=[('fundamental_incompleto', 'Fundamental incompleto'), ('fundamental', 'Fundamental'), ('medio_incompleto', 'Ensino Médio incompleto'), ('media', 'Ensino Médio'), ('superior_incompleto', 'Superior incompleto'), ('Superior', 'Superior')], max_length=128, verbose_name='Escolaridade')),
                ('como_conheceu', models.CharField(choices=[('amigos', 'Amigos'), ('conta_propria', 'Conta Propria')], max_length=128, verbose_name='Como conheceu?')),
                ('pontuacao', models.IntegerField(verbose_name='Quantidade de pontos')),
            ],
        ),
        migrations.CreateModel(
            name='Rota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250, verbose_name='Titulo')),
                ('descricao', models.TextField()),
                ('imagens_rota', models.FileField(max_length=500, upload_to=rotas.models.diretorio_imagens_rota, verbose_name='Imagem de Destaque da Rota')),
                ('proprietario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
        ),
        migrations.DeleteModel(
            name='Rotas',
        ),
        migrations.AddField(
            model_name='destino',
            name='imagens_destino',
            field=models.ManyToManyField(through='rotas.ImagensDestino', to='rotas.ArquivoImagem', verbose_name='Imagens do Destino'),
        ),
        migrations.AddField(
            model_name='destino',
            name='proprietario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
        migrations.AddField(
            model_name='avaliacoesdedestino',
            name='destino',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rotas.Destino'),
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='pessoa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rotas.Pessoa', verbose_name='Quem avaliou'),
        ),
    ]
