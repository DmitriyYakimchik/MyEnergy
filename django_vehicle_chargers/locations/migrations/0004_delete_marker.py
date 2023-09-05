from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_marker_alter_location_address'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Marker',
        ),
    ]
