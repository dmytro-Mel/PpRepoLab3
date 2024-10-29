# Generated by Django 5.1.2 on 2024-10-22 18:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('code', models.IntegerField()),
                ('price', models.FloatField()),
                ('last_update', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=45, unique=True)),
                ('password', models.CharField(max_length=45)),
                ('create_date', models.DateTimeField()),
                ('verif', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Chain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField()),
                ('create_date', models.DateTimeField()),
                ('last_update', models.DateTimeField()),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.asset')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_invoice', models.CharField(max_length=45)),
                ('deposit', models.FloatField(blank=True, null=True)),
                ('withdraw', models.FloatField(blank=True, null=True)),
                ('date', models.DateTimeField()),
                ('fees', models.FloatField()),
                ('chain_receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chain_receiver', to='myapp.chain')),
                ('chain_sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chain_sender', to='myapp.chain')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.status')),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
        migrations.AddField(
            model_name='chain',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.wallet'),
        ),
    ]