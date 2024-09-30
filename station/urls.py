from django.contrib.admin import action
from django.urls import path, include
from rest_framework import routers

from station.views import BusViewSet


router = routers.DefaultRouter()

router.register("buses", BusViewSet, basename="bus")


urlpatterns = [
    path("", include(router.urls)),
]


# bus_list = BusViewSet.as_view(
#     actions={
#         "get": "list",
#         "post": "create"
#     }
# )
#
# bus_detail = BusViewSet.as_view(
#     actions={
#         "get": "retrieve",
#         "put": "update",
#         "patch": "partial_update",
#         "delete": "destroy"
#     }
# )
#
# urlpatterns = [
#     path("buses/", bus_list, name="bus-list"),
#     path("buses/<int:pk>/", bus_detail, name="bus-detail")
# ]

app_name = "station"
