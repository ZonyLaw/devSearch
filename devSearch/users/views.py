from django.shortcuts import render
from .models import Profile
# Create your views here.


def profiles(request):
    Profiles = Profile.objects.all()
    context = {'profiles': Profiles}
    return render(request, 'users/profiles.html', context)


def userprofile(request, pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = {'profile': profile, 'topSkills': topSkills,
               'otherSkills': otherSkills}
    return render(request, 'users/user-profile.html', context)
