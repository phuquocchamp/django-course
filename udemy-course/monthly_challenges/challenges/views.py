from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "Eat no meat in the moring",
    "february": "Eat vegetable in the morning and in the evening!",
    "march": "Eat vegetable in the morning and in the evening!",
    "april": "Eat vegetable in the morning and in the evening!",
    "may": "Eat vegetable in the morning and in the evening!",
    "june": "Eat vegetable in the morning and in the evening!",
    "july": "Eat vegetable in the morning and in the evening!",
}


def index(request):
    months = list(monthly_challenges.keys())

    list_items = ""
    for month in months:
        capitalized_month = month.capitalize()
        path_item = reverse("monthly-challenges", args=[month])
        list_items += (
            f'<li><h1><a href="{path_item}">{capitalized_month} </a></h1></li>'
        )

    response_data = f"<ul>{list_items} </ul>"

    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    cur_month = months[month - 1]
    redirect_path = reverse("monthly_challenges", args=[cur_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(f"<h1>{challenge_text} </h1>")
    except:
        return HttpResponseNotFound("This month is not support !")
