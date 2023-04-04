from rest_framework import viewsets


from apii.memorandum.serializers import NoteModelSerializer
from memorandum.models import Note


class NoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed.
    """

    queryset = Note.objects.all().order_by("-created_at")
    serializer_class = NoteModelSerializer
    permission_classes = []
