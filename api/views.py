from django.http import HttpResponse
from rest_framework import generics
from django.shortcuts import redirect
from .models import Link
from .serializers import LinkSerializer


class ListAllLinksView(generics.ListAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class LinkCreateView(generics.CreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class LinkRedirectView(generics.RetrieveAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

    def get(self, request, short_url):
        try:
            link = Link.objects.get(short_url=short_url)
            return redirect(link.original_url)
        except Link.DoesNotExist:
            return HttpResponse("Короткая ссылка не найдена", status=404)


