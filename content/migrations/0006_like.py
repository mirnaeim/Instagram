# Generated by Django 4.2 on 2024-03-07 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_profile_options_alter_contact_user_from_and_more'),
        ('content', '0005_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='account.profile', verbose_name='Account')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='content.post', verbose_name='Post')),
            ],
            options={
                'ordering': ('pk',),
                'abstract': False,
            },
        ),
    ]
