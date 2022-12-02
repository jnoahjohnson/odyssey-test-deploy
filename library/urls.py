from django.urls import path
from .views import indexPageView, aboutPageView, bookPageView, listsPageView

urlpatterns = [
    path('', indexPageView, name="index"),
    path('aboutpage/', aboutPageView, name="about"),
    path('lists/', listsPageView, name="lists"),
    path('book/<book_id>/', bookPageView, name="book_detail")
]