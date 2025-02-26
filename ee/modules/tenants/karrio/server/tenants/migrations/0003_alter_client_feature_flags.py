# Generated by Django 3.2.14 on 2022-07-19 22:23

from django.db import migrations, models
import functools
import karrio.server.core.fields
import karrio.server.core.models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0002_client_feature_flags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='feature_flags',
            field=karrio.server.core.fields.MultiChoiceField(
                choices=[('AUDIT_LOGGING', 'AUDIT_LOGGING'), ('ALLOW_SIGNUP', 'ALLOW_SIGNUP'), ('ALLOW_ADMIN_APPROVED_SIGNUP', 'ALLOW_ADMIN_APPROVED_SIGNUP'), ('ALLOW_MULTI_ACCOUNT', 'ALLOW_MULTI_ACCOUNT'), ('ORDERS_MANAGEMENT', 'ORDERS_MANAGEMENT'), ('APPS_MANAGEMENT', 'APPS_MANAGEMENT'), ('DOCUMENTS_MANAGEMENT', 'DOCUMENTS_MANAGEMENT'), ('DATA_IMPORT_EXPORT', 'DATA_IMPORT_EXPORT'), ('CUSTOM_CARRIER_DEFINITION', 'CUSTOM_CARRIER_DEFINITION'), ('PERSIST_SDK_TRACING', 'PERSIST_SDK_TRACING')],
                default=functools.partial(karrio.server.core.models._identity, *(), **{'value': ['AUDIT_LOGGING', 'ALLOW_SIGNUP', 'ALLOW_ADMIN_APPROVED_SIGNUP', 'ALLOW_MULTI_ACCOUNT', 'ORDERS_MANAGEMENT', 'APPS_MANAGEMENT', 'DOCUMENTS_MANAGEMENT', 'DATA_IMPORT_EXPORT', 'CUSTOM_CARRIER_DEFINITION', 'PERSIST_SDK_TRACING']}),
                help_text='The list of feature flags.'
            ),
        ),
    ]
