# Generated by Django 5.1.4 on 2024-12-06 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioHome', '0003_alter_mainpageimage_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoGrid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('project_url', models.URLField()),
            ],
        ),
    ]
