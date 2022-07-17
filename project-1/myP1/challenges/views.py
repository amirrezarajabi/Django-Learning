from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

MONTH_CHALLENGE = {
    "january": "Be strong in january",
    "february": "Be strong in february",
    "march": "Be strong in march",
    "april": "Be strong in april",
    "may": "Be strong in may",
    "june": "Be strong in june",
    "july": "Be strong in july",
    "august": "Be strong in august",
    "september": "Be strong in september",
    "october": "Be strong in october",
    "november": "Be strong in november",
    "december": "Be strong in december",
}

def monthly_challenge(request, month):
    try:
        challenge_text = MONTH_CHALLENGE[month]
    except:
        return HttpResponseNotFound("this month is not supported")
    return HttpResponse(challenge_text)

def monthly_challenge_by_number(request, month):
    months = list(MONTH_CHALLENGE.keys())

    if month > len(months):
        return HttpResponseNotFound("invalid month")
    
    forward_month = months[month - 1]
    # redirect_path = reverse("month-challenge") # /challenges/
    redirect_path = reverse("month-challenge", kwargs={"month": forward_month})
    print(redirect_path)
    return HttpResponseRedirect(redirect_path)