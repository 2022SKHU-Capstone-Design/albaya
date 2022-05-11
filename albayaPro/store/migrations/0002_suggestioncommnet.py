# Generated by Django 4.0.3 on 2022-05-11 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuggestionCommnet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500)),
                ('notice_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='store.suggestionbox')),
            ],
        ),
    ]
