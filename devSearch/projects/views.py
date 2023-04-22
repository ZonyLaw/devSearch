from django.shortcuts import render
from django.http import HttpResponse

projectList = [
    {
        'id': '1',
        'title': "Ecommerce Website",
        'description': 'Fully functinoal ecommerce website'
    },
    {
        'id': '2',
        'title': "Portfolio Website",
        'description': 'This was a project where I built out my portfolio'
    },
    {
        'id': '3',
        'title': "Social Network",
        'description': 'Awersome open source project I am still working'
    },

]


def projects(request):
    msg = "Hello, yopu are on the projects page "
    context = {'message': msg, 'projects': projectList}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = None
    for i in projectList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project': projectObj})
