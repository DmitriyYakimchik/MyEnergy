import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Connector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connector_type', models.CharField(help_text='Output connector name', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(help_text='Full address (street, city, international code)', max_length=200)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(help_text='manufacturer name', max_length=150)),
                ('available', models.BooleanField(default=True, help_text='True - yes, False - no')),
                ('connectors', models.ManyToManyField(help_text='One station can have multiple connectors', to='locations.connector')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stations', to='locations.location')),
            ],
        ),
    ]
