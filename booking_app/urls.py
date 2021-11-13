from django.contrib import admin
from django.urls import path
from booking_main.views import Room_view, allrooms, delete_room, Modify_room, Reservation_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', allrooms),
    path('room/new/', Room_view.as_view()),
    path('room/delete/<int:id_>/', delete_room),
    path('room/modify/<int:id_>/', Modify_room.as_view()),
    path('room/reserve/<int:id_>/', Reservation_view.as_view())
]
