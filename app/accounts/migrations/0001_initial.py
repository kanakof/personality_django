# Generated by Django 4.2.1 on 2023-06-11 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', '男性'), ('F', '女性'), ('O', 'その他'), ('N', '回答しない')], default='N', max_length=1)),
                ('blood_type', models.CharField(choices=[('A', 'A型'), ('B', 'B型'), ('AB', 'AB型'), ('O', 'O型'), ('OTHER', 'その他')], default='OTHER', max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'ユーザー',
                'verbose_name_plural': 'ユーザー一覧',
            },
        ),
    ]
