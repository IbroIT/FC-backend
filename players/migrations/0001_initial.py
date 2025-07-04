# Generated by Django 5.2.1 on 2025-06-24 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('position', models.CharField(choices=[('goalkeeper', 'Вратарь'), ('defender', 'Защитник'), ('midfielder', 'Полузащитник'), ('forward', 'Нападающий')], max_length=20)),
                ('positionName', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('nationality', models.CharField(max_length=100)),
                ('matches', models.IntegerField()),
                ('goals', models.IntegerField()),
                ('assists', models.IntegerField()),
                ('rating', models.FloatField()),
                ('image', models.URLField()),
                ('height', models.CharField(max_length=20)),
                ('weight', models.CharField(max_length=20)),
                ('birthDate', models.CharField(max_length=50)),
            ],
        ),
    ]
