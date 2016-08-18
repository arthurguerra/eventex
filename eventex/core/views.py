from django.shortcuts import render


def home(request):
    speakers = [
        {'name': 'Gracie Hopper', 'photo': 'http://hbn.link/hopper-pic'},
        {'name': 'Alan Turing', 'photo': 'http://hbn.link/turing-pic'},
    ]

    return render(request, 'index.html', {'speakers': speakers})
