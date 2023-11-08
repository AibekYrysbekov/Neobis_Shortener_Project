from django.urls import path
from .views import LinkCreateView, LinkRedirectView, ListAllLinksView

urlpatterns = [
    path('list/', ListAllLinksView.as_view(), name='list-all-links'),
    path('create/', LinkCreateView.as_view(), name='link-create'),
    path('<str:short_url>/', LinkRedirectView.as_view(), name='link-redirect'),
]
