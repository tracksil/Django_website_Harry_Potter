from django.shortcuts import render
import requests

ALL_CHAR = 'https://hp-api.herokuapp.com/api/characters'
characters = requests.get(ALL_CHAR).json()

ALL_SPELLS = 'https://hp-api.herokuapp.com/api/spells'
spells = requests.get(ALL_SPELLS).json()


def index(request):
    return render(request, 'myapp/index.html', {'characters': characters})


def about(request, name):
    char = next(char for char in characters if char['name'] == name)
    return render(request, 'myapp/about.html', {'char': char})


def spell(request):
    if request.method == "POST":
        to_search = str(request.POST['query'])
        searched_spell = next(spel for spel in spells if spel['name'] == to_search.capitalize())
        return render(request, 'myapp/spells.html', {'spell': searched_spell})
    return render(request, 'myapp/spells.html', {'spells': spells})
