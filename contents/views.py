from .models import Content
from .serializers import ContentSerializer
from rest_framework import generics


class ContentView(generics.ListCreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class ContentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = "content_id"


class ContentFilterView(generics.ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def get_queryset(self):
        title = self.request.query_params.get("title", None)
        contents = self.queryset.filter(title__icontains=title)

        return contents
