from django.contrib import admin
from django.urls import path
from booking_main.views import New_Room_view, allrooms, delete_room, Modify_room, Reservation_view, room_details

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", allrooms),
    path("room/new/", New_Room_view.as_view()),
    path("room/delete/<int:id_>/", delete_room),
    path("room/modify/<int:id_>/", Modify_room.as_view()),
    path("room/reserve/<int:id_>/", Reservation_view.as_view()),
    path("room/<int:id_>/", room_details),
]
