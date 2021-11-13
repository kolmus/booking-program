from django import http
from django.shortcuts import render, redirect
from django.views import View
from booking_main.models import Rooms
from django.db import IntegrityError

class Room(View):
    def post(self, request):
        name_new = request.POST['name']
        capacity = int(request.POST['capacity'])
        projector = bool(request.POST.get('projector'))
        new_room = Rooms()
        
        if name_new == '':
            return render(request, 'add_room.html', {'response': "Name can't be empty!"})
        if capacity <= 0:
            return render(request, 'add_room.html', {'response': 'Capacity has to be grater than 0!'})
        
        rooms = Rooms.objects.all()
        names = []
        for room in rooms:
            names.append(room)
        try:
            new_room.name = name_new
            new_room.capacity = capacity
            new_room.projector = projector
            new_room.save()
        except IntegrityError:
            return render(request, 'add_room.html', {'response': '{} already exists. Try other name'.format(name_new)})
            
        return render(request, 'add_room.html', {'response': 'udało się'})
    
    def get(self, request):
        return render(request, 'add_room.html')


def allrooms(request):
    rooms = Rooms.objects.all()
    return render(request, 'index.html', {'all_rooms': rooms})

def delete_room(request, id_):
    room = Rooms.objects.get(id=id_)
    room.delete()
    return redirect('/')
    