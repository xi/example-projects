# Generated by Django 4.0.2 on 2022-02-09 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='Title')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='Title')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Title')),
                ('responsible_researcher', models.CharField(max_length=32, verbose_name='Responsible researcher')),
                ('identifier', models.CharField(blank=True, help_text='Identifier to a corresponding publication supported by Semantic Scholar (https://www.semanticscholar.org), e.g. DOI or ArXiv ID', max_length=32, verbose_name='Identifier')),
                ('data_type', models.ManyToManyField(to='main.DataType', verbose_name='Data type')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.department', verbose_name='Department')),
            ],
        ),
    ]
