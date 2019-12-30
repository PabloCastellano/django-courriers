# Generated by Django 3.0.1 on 2019-12-30 04:26

import courriers.models.base
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('published_at', models.DateTimeField(null=True)),
                ('status', models.PositiveIntegerField(choices=[(1, 'Online'), (2, 'Draft')], db_index=True, default=2)),
                ('headline', models.TextField(blank=True, null=True)),
                ('conclusion', models.TextField(blank=True, null=True)),
                ('cover', models.ImageField(blank=True, null=True, upload_to=courriers.models.base.get_file_path)),
                ('sent', models.BooleanField(db_index=True, default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NewsletterList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('list_id', models.IntegerField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NewsletterSegment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('segment_id', models.IntegerField()),
                ('lang', models.CharField(blank=True, choices=[('af', 'Afrikaans'), ('ar', 'Arabic'), ('ast', 'Asturian'), ('az', 'Azerbaijani'), ('bg', 'Bulgarian'), ('be', 'Belarusian'), ('bn', 'Bengali'), ('br', 'Breton'), ('bs', 'Bosnian'), ('ca', 'Catalan'), ('cs', 'Czech'), ('cy', 'Welsh'), ('da', 'Danish'), ('de', 'German'), ('dsb', 'Lower Sorbian'), ('el', 'Greek'), ('en', 'English'), ('en-au', 'Australian English'), ('en-gb', 'British English'), ('eo', 'Esperanto'), ('es', 'Spanish'), ('es-ar', 'Argentinian Spanish'), ('es-co', 'Colombian Spanish'), ('es-mx', 'Mexican Spanish'), ('es-ni', 'Nicaraguan Spanish'), ('es-ve', 'Venezuelan Spanish'), ('et', 'Estonian'), ('eu', 'Basque'), ('fa', 'Persian'), ('fi', 'Finnish'), ('fr', 'French'), ('fy', 'Frisian'), ('ga', 'Irish'), ('gd', 'Scottish Gaelic'), ('gl', 'Galician'), ('he', 'Hebrew'), ('hi', 'Hindi'), ('hr', 'Croatian'), ('hsb', 'Upper Sorbian'), ('hu', 'Hungarian'), ('hy', 'Armenian'), ('ia', 'Interlingua'), ('id', 'Indonesian'), ('io', 'Ido'), ('is', 'Icelandic'), ('it', 'Italian'), ('ja', 'Japanese'), ('ka', 'Georgian'), ('kab', 'Kabyle'), ('kk', 'Kazakh'), ('km', 'Khmer'), ('kn', 'Kannada'), ('ko', 'Korean'), ('lb', 'Luxembourgish'), ('lt', 'Lithuanian'), ('lv', 'Latvian'), ('mk', 'Macedonian'), ('ml', 'Malayalam'), ('mn', 'Mongolian'), ('mr', 'Marathi'), ('my', 'Burmese'), ('nb', 'Norwegian Bokmål'), ('ne', 'Nepali'), ('nl', 'Dutch'), ('nn', 'Norwegian Nynorsk'), ('os', 'Ossetic'), ('pa', 'Punjabi'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pt-br', 'Brazilian Portuguese'), ('ro', 'Romanian'), ('ru', 'Russian'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('sq', 'Albanian'), ('sr', 'Serbian'), ('sr-latn', 'Serbian Latin'), ('sv', 'Swedish'), ('sw', 'Swahili'), ('ta', 'Tamil'), ('te', 'Telugu'), ('th', 'Thai'), ('tr', 'Turkish'), ('tt', 'Tatar'), ('udm', 'Udmurt'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('uz', 'Uzbek'), ('vi', 'Vietnamese'), ('zh-hans', 'Simplified Chinese'), ('zh-hant', 'Traditional Chinese')], max_length=10, null=True)),
                ('newsletter_list', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lists', to='courriers.NewsletterList')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NewsletterItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=courriers.models.base.get_file_path)),
                ('url', models.URLField(blank=True, null=True)),
                ('position', models.PositiveIntegerField(blank=True, null=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType')),
                ('newsletter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='courriers.Newsletter')),
            ],
            options={
                'ordering': ['position'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='newsletter',
            name='newsletter_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='newsletters', to='courriers.NewsletterList'),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='newsletter_segment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='segments', to='courriers.NewsletterSegment'),
        ),
    ]
