# Generated by Django 3.0.9 on 2020-09-07 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_article_origin_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='origin_content',
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parentArticle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.TranslatedArticle')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parentArticle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.TranslatedArticle')),
            ],
        ),
    ]
