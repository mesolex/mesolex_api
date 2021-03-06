# Generated by Django 3.2.8 on 2021-10-22 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lexicon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlantThesaurus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genus_species', models.CharField(db_index=True, max_length=256)),
                ('synonym', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Plant Thesaurus',
            },
        ),
    ]
