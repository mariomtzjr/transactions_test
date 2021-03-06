# Generated by Django 3.2.12 on 2022-05-08 04:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status_transaction', models.CharField(choices=[('closed', 'Closed'), ('reversed', 'Reversed'), ('pending', 'Pending')], default='pending', max_length=20)),
                ('status_approved', models.BooleanField(default=False)),
                ('final_payment', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.company')),
            ],
        ),
        migrations.AddConstraint(
            model_name='transaction',
            constraint=models.UniqueConstraint(fields=('id',), name='unique_transaction_id'),
        ),
    ]
