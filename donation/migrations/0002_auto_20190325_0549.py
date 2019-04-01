# Generated by Django 2.1.2 on 2019-03-25 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='pblood_group',
            new_name='patient_blood_group',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='pgender',
            new_name='patient_gender',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='phospital',
            new_name='patient_hospital',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='pname',
            new_name='patient_name',
        ),
    ]