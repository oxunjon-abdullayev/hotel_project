from django.shortcuts import render

from app.models import Room, Blog


def index(request):
    Rooms = Room.objects.all()
    return render(request=request,
                  template_name='app/index.html',
                  context={"Rooms": Rooms})


def about(request):
    return render(request, 'app/about.html')


def account(request):
    return render(request, 'app/account.html')


def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'app/blog.html',
                  {"blogs":blogs})


def blog_single(request):
    return render(request, 'app/blog-single.html')


def booking(request):
    return render(request, 'app/booking.html')


def contact(request):
    return render(request, 'app/contact.html')


def pricing(request):
    return render(request, 'app/pricing.html')


def room_details(request, room_id):
    rooom = Room.objects.filter(id=room_id).first()

    return render(request=request,
                  template_name='app/room-details.html',
                  context={"rooom": rooom})


def room_listing(request):
    Rooms = Room.objects.all()
    return render(request=request,
                  template_name='app/room-listing.html',
                  context={"Rooms": Rooms})


def service_details(request):
    return render(request, 'app/service-details.html')


def service_single(request):
    return render(request, 'app/service-details.html')


def services(request):
    return render(request, 'app/services.html')


def team(request):
    return render(request, 'app/team.html')


def team_single(request):
    return render(request, 'app/team-single.html')


def header(request):
    return render(request, 'base/header.html')
