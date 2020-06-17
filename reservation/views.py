from django.shortcuts import render
from .models import Reservation
from reservation.models import Reservation
from project.forms import ReserveTableForm

# Create your views here.

def resrve_table(request):
    resrve_form = ReserveTableForm()

    if request.method =='POST':
        resrve_form = ReserveTableForm(request.POST)

        if resrve_form.is_valid():
            resrve_form.save()

    context ={'form':resrve_form}
    return render(request,'Reservation/reservation.html', context)
    pass
