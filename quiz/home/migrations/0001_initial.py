# Generated by Django 4.2.8 on 2023-12-06 08:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=100)),
                ('marks', models.IntegerField(default=5)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='home.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('answer', models.CharField(max_length=100)),
                ('is_correst', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_answer', to='home.question')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]