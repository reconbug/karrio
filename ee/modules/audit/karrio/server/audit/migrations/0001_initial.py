# Generated by Django 3.2.13 on 2022-06-24 14:50

from django.db import migrations
import karrio.server.core.models.base


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auditlog', '0009_alter_logentry_additional_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuditLogEntry',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auditlog.logentry', karrio.server.core.models.base.ControlledAccessModel),
        ),
    ]
