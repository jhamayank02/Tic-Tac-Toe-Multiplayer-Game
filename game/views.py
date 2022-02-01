from django.shortcuts import render, redirect, HttpResponse
from .models import Game
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'home.html')

def gamepage(request):
    if request.method == 'POST':
        username = request.POST['username']
        room_name = request.POST['room_name']
        option = request.POST['option']
        print(option)

        # If all the fields are non empty
        if username != '' and room_name != '' and option != '':

            # If the user selects the option 'create a room'
            if option == '2':
                # If the room does not exists then create a room
                if(Game.objects.filter(room_name=room_name).exists()):
                    messages.error(request, "This room name is not available. Please try with another name!")
                    return render(request, 'home.html')  
                else:
                    newGame = Game.objects.create(room_creator=username, game_over=False, room_name=room_name)
                    # newGame.save()
                    messages.success(request, "Room created successfully!")
                
            # If the user selects 'Have a room name'
            elif option == '1':
                # Check whether the room exists or not
                if(Game.objects.filter(room_name=room_name).exists()):
                    newGame = Game.objects.filter(room_name=room_name).first()
                    newGame.game_opponent = username
                    newGame.save()
                    messages.success(request, "Entered in the room!")
                else:
                  messages.error(request, "Room does not exists!")
                  return render(request, 'home.html')  
            
            # If the user does not select any option
            else:
               messages.error(request, "Please choose an option!")
               return render(request, 'home.html')
                
            return render(request, 'gamepage.html', {
                'username': username, 'room_name': room_name
            })

        else:
            messages.error(request, "Please fill all the fields!")
            return render(request, 'home.html')

    else:
        return HttpResponse("404 Not Found")