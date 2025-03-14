# Generated by Django 5.1.2 on 2025-02-18 09:33

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0010_alter_conversation_conversation_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='conversation_id',
            field=models.UUIDField(db_index=True, default=uuid.UUID('064c14bf-f58d-43a1-9774-50b835de8c7c'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='message',
            name='message_id',
            field=models.UUIDField(db_index=True, default=uuid.UUID('8817a4a8-e99d-4d66-bbc3-51b5b784dafd'), primary_key=True, serialize=False),
        ),
    ]
