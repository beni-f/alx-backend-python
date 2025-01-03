# Generated by Django 5.1.2 on 2025-01-03 19:37

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_alter_conversation_conversation_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='conversation_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chats.conversation'),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='conversation_id',
            field=models.UUIDField(db_index=True, default=uuid.UUID('f1b8ea20-2ccf-47e0-836b-2555bc2e5855'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='message',
            name='message_id',
            field=models.UUIDField(db_index=True, default=uuid.UUID('2ec19c15-8911-4cdf-83f5-b13579605f22'), primary_key=True, serialize=False),
        ),
    ]