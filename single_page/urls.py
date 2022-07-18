from django.urls import path
from single_page.views import HomeView

urlpatterns = [
    path('', HomeView.as_view())
]