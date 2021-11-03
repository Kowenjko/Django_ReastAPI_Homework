# Generated by Django 3.2.8 on 2021-10-28 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_f', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('zip_code', models.IntegerField()),
                ('street', models.CharField(max_length=100)),
                ('house_num', models.IntegerField()),
                ('apartamenst', models.IntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='userlist',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='rest_f.address'),
        ),
    ]