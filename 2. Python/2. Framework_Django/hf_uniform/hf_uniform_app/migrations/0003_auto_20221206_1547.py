# Generated by Django 3.2.3 on 2022-12-06 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hf_uniform_app', '0002_alter_uniform_orgnizationname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uniform',
            old_name='back_length',
            new_name='Back_length',
        ),
        migrations.RenameField(
            model_name='uniform',
            old_name='center_back',
            new_name='Center_back',
        ),
        migrations.RenameField(
            model_name='uniform',
            old_name='chest',
            new_name='Chest',
        ),
        migrations.RenameField(
            model_name='uniform',
            old_name='collar',
            new_name='Collar',
        ),
        migrations.RenameField(
            model_name='uniform',
            old_name='crotch',
            new_name='Crotch',
        ),
        migrations.RenameField(
            model_name='uniform',
            old_name='front_crotch',
            new_name='Front_crotch',
        ),
        migrations.RenameField(
            model_name='uniform',
            old_name='hip',
            new_name='Hip',
        ),
        migrations.RenameField(
            model_name='uniform',
            old_name='pants_length',
            new_name='Pants_length',
        ),
        migrations.RenameField(
            model_name='uniform',
            old_name='remark',
            new_name='Remark',
        ),
        migrations.RenameField(
            model_name='uniform',
            old_name='seat',
            new_name='Seat',
        ),
        migrations.RenameField(
            model_name='uniform',
            old_name='shirt_length',
            new_name='Shirt_length',
        ),
        migrations.RenameField(
            model_name='uniform',
            old_name='shoulder_width',
            new_name='Shoulder_width',
        ),
        migrations.RenameField(
            model_name='uniform',
            old_name='skirt_length',
            new_name='Skirt_length',
        ),
        migrations.RenameField(
            model_name='uniform',
            old_name='sleeve_length',
            new_name='Sleeve_length',
        ),
        migrations.RenameField(
            model_name='uniform',
            old_name='thigh',
            new_name='Thigh',
        ),
        migrations.RenameField(
            model_name='uniform',
            old_name='waist',
            new_name='Waist',
        ),
        migrations.RenameField(
            model_name='uniform',
            old_name='waist_belt',
            new_name='Waist_belt',
        ),
    ]