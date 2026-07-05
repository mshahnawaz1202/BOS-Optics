from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils import timezone

from .models import Appointment, Service


def book_appointment(request):
    services = Service.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        date = request.POST.get('date')
        service_id = request.POST.get('service')
        message = request.POST.get('message', '').strip()

        if name and email and phone and date:
            service = Service.objects.filter(pk=service_id).first()
            Appointment.objects.create(
                name=name, email=email, phone=phone,
                date=date, service=service, message=message,
            )
            messages.success(request, 'Your appointment has been booked! We will contact you shortly.')
            return redirect('services:book')
        messages.error(request, 'Please fill in all required fields.')

    return render(request, 'services/book.html', {
        'services': services,
        'min_date': timezone.now().date().isoformat(),
    })
