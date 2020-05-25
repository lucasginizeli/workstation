# Generated by Django 3.0.6 on 2020-05-25 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True)),
                ('editado', models.DateField(auto_now=True)),
                ('nome', models.CharField(max_length=255)),
                ('info', models.TextField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=9)),
                ('imagem', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'produtos',
            },
        ),
    ]