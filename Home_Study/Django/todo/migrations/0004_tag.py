# Generated by Django 5.1.1 on 2024-10-04 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('projects', models.ManyToManyField(related_name='tags', to='todo.project')),
            ],
        ),
    ]
