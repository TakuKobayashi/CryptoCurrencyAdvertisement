# Generated by Django 2.0.6 on 2018-06-04 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=32, null=True)),
                ('uid', models.CharField(max_length=255)),
                ('token', models.TextField(blank=True, null=True)),
                ('token_secret', models.TextField(blank=True, null=True)),
                ('expired_at', models.DateTimeField(blank=True, null=True)),
                ('options', models.TextField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=255)),
                ('host', models.CharField(max_length=255)),
                ('url', models.TextField()),
                ('daily_price', models.FloatField(default=0)),
                ('sum_price', models.FloatField(default=0)),
                ('min_price', models.FloatField(default=0)),
                ('start_at', models.DateTimeField()),
                ('end_at', models.DateTimeField()),
                ('title', models.TextField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('banner_url', models.CharField(blank=True, max_length=255, null=True)),
                ('show_order', models.IntegerField(default=0)),
                ('activate_state', models.IntegerField(default=0)),
                ('options', models.TextField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AdvertisementLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=255)),
                ('accessed_by_ipaddress', models.CharField(max_length=255)),
                ('accessed_by_user_token', models.CharField(max_length=255)),
                ('accessed_by_user_agent', models.TextField(blank=True, null=True)),
                ('impression_count', models.IntegerField(default=0)),
                ('click_count', models.IntegerField(default=0)),
                ('action_count', models.IntegerField(default=0)),
                ('options', models.TextField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('advertisement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adnem.Advertisement')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=255)),
                ('email_address', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('last_login_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_prefix', models.CharField(max_length=32)),
                ('currency_name', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=255)),
                ('amount', models.FloatField(default=0)),
                ('options', models.TextField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adnem.User')),
            ],
        ),
        migrations.AddField(
            model_name='advertisement',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adnem.User'),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adnem.User'),
        ),
    ]
