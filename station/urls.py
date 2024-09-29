from django.urls import path

from station.views import BusList, BusDetail

urlpatterns = [
    path("buses/", BusList.as_view(), name="bus-list"),
    path("buses/<int:pk>/", BusDetail.as_view(), name="bus-detail")
]

app_name = "station"
