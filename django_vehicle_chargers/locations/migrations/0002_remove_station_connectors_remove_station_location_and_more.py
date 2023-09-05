from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='station',
            name='connectors',
        ),
        migrations.RemoveField(
            model_name='station',
            name='location',
        ),
        migrations.DeleteModel(
            name='Connector',
        ),
        migrations.DeleteModel(
            name='Station',
        ),
    ]
