from rest_framework import serializers

from memorandum.models import Note


class NoteModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ["title", "text", "created_at"]
