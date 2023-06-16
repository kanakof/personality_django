# Generated by Django 4.2.1 on 2023-06-15 02:35

from django.db import migrations, models
import questions.models


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="btypechoice",
            field=models.IntegerField(
                choices=[(1, "A型"), (2, "B型"), (3, "O型"), (4, "AB型")],
                default=questions.models.BtypeChoices,
            ),
        ),
        migrations.AddField(
            model_name="answer",
            name="genderchoices",
            field=models.IntegerField(
                choices=[(1, "女性"), (2, "男性"), (3, "無回答")], default=3
            ),
        ),
        migrations.AlterField(
            model_name="answer",
            name="choice",
            field=models.IntegerField(
                choices=[
                    (1, "とても同意する"),
                    (2, "まあ同意する"),
                    (3, "どちらでもない"),
                    (4, "あまり同意しない"),
                    (5, "全く同意しない"),
                ],
                default=3,
            ),
        ),
    ]