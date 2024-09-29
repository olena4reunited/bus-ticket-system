from django.contrib.admin import action
from django.urls import path

from station.views import BusList, BusDetail

urlpatterns = [
    path(
        "buses/",
        BusList.as_view(
            actions={
                "get": "list",
                "post": "create"
            }
        ),
        name="bus-list"
    ),
    path(
        "buses/<int:pk>/",
        BusDetail.as_view(
            actions={
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy"
            }
        ),
        name="bus-detail"
    )
]

app_name = "station"
