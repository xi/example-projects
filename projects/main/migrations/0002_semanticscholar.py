# Generated by Django 4.0.2 on 2022-02-09 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='identifier',
            new_name='paper_identifier',
        ),
        migrations.AddField(
            model_name='project',
            name='paper_title',
            field=models.CharField(blank=True, max_length=64, verbose_name='Paper'),
        ),
        migrations.AddField(
            model_name='project',
            name='paper_url',
            field=models.URLField(blank=True, verbose_name='Paper URL'),
        ),
        migrations.AddField(
            model_name='project',
            name='paper_citations',
            field=models.IntegerField(default=0, verbose_name='Citations'),
        ),
        migrations.AddField(
            model_name='project',
            name='paper_timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]