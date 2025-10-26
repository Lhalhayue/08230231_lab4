from django.shortcuts import render
from .models import TimelineEvent, Profile

# View for the home page (timeline)
def index(request):
    timeline_events = TimelineEvent.objects.all().order_by('year')  # Fetch all timeline events, sorted by year
    context = {
        'timeline_events': timeline_events
    }
    return render(request, 'index.html', context)

# View for the About Me page
def about_me(request):
    try:
        profile = Profile.objects.first()  # Assuming you have only one profile
    except Profile.DoesNotExist:
        profile = None

    context = {
        'profile': profile
    }
    return render(request, 'aboutMe.html', context)
