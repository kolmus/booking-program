from django.shortcuts import render, redirect
from django.views import View
from booking_main.models import Rooms, Reservations
from django.db import IntegrityError
from datetime import date


class New_Room_view(View):
    """View for adding new room into database

    Args:
        View (parent class): from django
    """

    def post(self, request):
        """Own POST metod for Room_view

        Args:
            name (str): name of new room
            capacity (str): number of sits in new room
            projector (str): request from checkbox from html

        Returns:
            response (str): answers for exceptions
            redirect to main page after save changes
        """

        name_new = request.POST["name"]
        capacity = int(request.POST["capacity"])
        projector = bool(request.POST.get("projector"))
        new_room = Rooms()

        if name_new == "":
            return render(request, "add_room.html", {"response": "Name can't be empty!"})
        if capacity <= 0:
            return render(request, "add_room.html", {"response": "Capacity has to be grater than 0!"})

        try:
            new_room.name = name_new
            new_room.capacity = capacity
            new_room.projector = projector
            new_room.save()
        except IntegrityError:
            return render(request, "add_room.html", {"response": "{} already exists. Try other name".format(name_new)})

        return redirect("/")

    def get(self, request):
        """Own GET metod of Room_view

        Returns:
            connection to add_room.html template
        """
        return render(request, "add_room.html")


def allrooms(request):
    """View of main page.
    Included checking of every room availability during checking.

    Returns:
        connection to index.html
        all_rooms: Query Set with objects of Rooms model
    """
    rooms = Rooms.objects.all().order_by("id")
    for room in rooms:
        reservations = room.reservations.all()
        room.available = True
        for reservation in reservations:
            if reservation.date == date.today():
                room.available = False
        room.save()
    return render(request, "index.html", {"all_rooms": rooms})


def delete_room(request, id_):
    """View for deleting rooms from database

    Args:
        id_ (int): id of room

    Returns:
        redirect to main page
    """
    room = Rooms.objects.get(id=id_)
    room.delete()
    return redirect("/")


class Modify_room(View):
    """View created to modify rooms.

    Args:
       View (parent class): from django
    """

    def get(self, request, id_):
        """Own get metod for Modify_room class

        Args:
            request : from django
            id_ (int): id of object in Rooms class / of room

        Returns:
            render to template modify_room.html
            room : object with id: id_ in Rooms model
        """
        room = Rooms.objects.get(id=id_)
        return render(request, "modify_room.html", {"room": room})

    def post(self, request, id_):
        """Own get metod for Modify_room class

        Args:
            request : from django
            id_ (int): id of object in Rooms class / of room

        Returns:
            render to main page or
            response : message afcer catching exeptions
        """
        room = Rooms.objects.get(id=id_)
        name_new = request.POST["name"]
        capacity_new = int(request.POST["capacity"])
        projector_new = bool(request.POST.get("projector"))

        if name_new == "":
            return render(request, "modify_room.html", {"response": "Name can't be empty!"})
        if capacity_new <= 0:
            return render(request, "modify_room.html", {"response": "Capacity has to be grater than 0!"})

        try:
            room.name = name_new
            room.capacity = capacity_new
            room.projector = projector_new
            room.save()
        except IntegrityError:
            return render(
                request, "modify_room.html", {"response": "{} already exists. Try other name".format(name_new)}
            )

        return redirect("/")


class Reservation_view(View):
    """View of reservating rooms

    Args:
        View : from Django
    """

    def get(self, request, id_):
        """Own get metod for Reservation_view class

        Args:
            request : from django
            id_ (int): id of object in Rooms class / of room

        Returns:
            render to template modify_room.html
            reservations : Query set of Reservatios model
        """
        reservations_all = Reservations.objects.all()
        return render(request, "reservation.html", {"reservations": reservations_all})

    def post(self, request, id_):
        """Own post metod for Reservation_view class

        Args:
            request : from django
            id_ (int): id of object in Rooms class / of room

        Returns:
            rdeirect to main page
            reservations_all : Query set of Reservatios model
            response : message after cathing exeption
        """
        date_of_reservation = request.POST["date"]
        room = Rooms.objects.get(id=id_)
        reservations_all = Reservations.objects.all()

        if str(date.today()) > date_of_reservation:
            return render(
                request,
                "reservation.html",
                {"response": "Date is in the past. Try again", "reservations": reservations_all},
            )

        try:
            new_reservation = Reservations()
            new_reservation.date = date_of_reservation
            new_reservation.room = room
            new_reservation.comment = request.POST["comment"]
            new_reservation.save()
        except IntegrityError:
            return render(
                request,
                "reservation.html",
                {
                    "response": "This room already has reservation for this day. Try another date or another room.",
                    "reservations": reservations_all,
                },
            )
        return redirect("/")


def room_details(request, id_):
    """View created to shof details of room

    Args:
        request : fro django
        id_ (int): id of room object of Romms model

    Returns:
        room: object of Rooms model
        reservations: Guery Set of Reservations model
    """
    room = Rooms.objects.get(id=id_)
    reservations = room.reservations.filter(date__gte=str(date.today()))  # później odfiltrować daty z przeszłości
    return render(request, "room_details.html", {"room": room, "reservations": reservations})
