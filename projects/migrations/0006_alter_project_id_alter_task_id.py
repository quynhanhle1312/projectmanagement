# Generated by Django 4.1.3 on 2022-11-09 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "projects",
            "0005_alter_project_id_alter_project_status_alter_task_due_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="task",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]