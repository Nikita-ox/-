from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView

from auction.models import Product, Purchase

menu = [
    {"title": "О нас", "url_name": "home"},
    {"title": "Правила", "url_name": "#"},
    {"title": "Поддержка", "url_name": "podd"},
    {"title": "Регистрация", "url_name": "home"},
]

#
# def user_enter():
#     # user_input = float(input("Enter integer\n"))
#
#     start = 0.0
#
#     while 1:
#         start += 0.25
#         if start == 2:
#             break
#         # elif "Поставить" != 0.25:
#         #     raise ValueError
#
#         return str(start)
#
#
# user_enter()

a = ["cat/1"]


def home(request):
    post = Product.objects.all()
    context = {
        "post": post,
        "title": "Главная",
        "user_enter": a
    }
    return render(request, "auction/home.html", context=context)


def podderjka(request):
    return render(request, "auction/podd.html")


def category(request, cat):
    context = {
        cat: cat
    }
    return render(request, "auction/cat.html", context=context)


def about(request):
    return render(request, "auction/about.html", {"menu": menu})
