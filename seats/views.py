from django.shortcuts import render
from django.db.models import Count, Max
from collections import defaultdict
from .models import Seats 

def index(request):
        data = Seats.objects.all().order_by('row_no')
        userip = get_client_ip(request)
        message= ''
        i_class= ''
        
        if Seats.objects.filter(ip=userip):
            message = "You have already booked your seat."
            i_class = 'info'
        elif request.method == 'POST':
            print(request.POST.get('seat_name'))
            if(request.POST.get('seat_name') == None):
                message = 'Please Select a seat first'
                i_class = 'info'
            else:
                t = Seats.objects.get(seat_name= request.POST.get('seat_name'))
                if(t.booked_by == ''):
                    t.booked_by = request.POST.get("booked_by")
                    t.ip = userip
                    t.save()
                    message = 'Congratulations you have successfully booked your seat!'
                    i_class = 'success'
                    print('success')
                else: 
                    message = 'This seat is already booked!'
                    i_class = 'danger'
                    print("error")
        else:
            message = 'This seat is already booked!' 

        context = {
            'seats_data': data,
            'message': message,
            'i_class': i_class
        }
        return render(request, 'seats/index.html', context)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
    
