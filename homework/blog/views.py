from django.shortcuts import render

items = {
    "Smartphone": {
        "id": 1,
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
    },
    "Laptop": {
        "id": 2,
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
    },
    "Keyboard": {
        "id": 3,
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
    },
    "Mouse": {
        "id": 4,
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
    },
}


def items_list(request):
    return render(request, "index.html")