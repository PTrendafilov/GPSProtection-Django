# Generated by Django 4.1.3 on 2024-02-29 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StaffApp', '0005_child_device_parent_remove_research_tags_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='devices',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='StaffApp.device'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='children',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parents', to='StaffApp.child'),
        ),
    ]