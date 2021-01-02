from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pandas as pd 
# Create your views here.
def home(request):
    return render(request,'html.html')