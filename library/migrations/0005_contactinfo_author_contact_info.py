# Generated by Django 4.1.2 on 2022-11-28 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_alter_book_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'author_contact_info',
            },
        ),
        migrations.AddField(
            model_name='author',
            name='contact_info',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='library.contactinfo'),
        ),
    ]
