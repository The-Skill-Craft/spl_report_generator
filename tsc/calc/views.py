from django.shortcuts import render
from django.http import HttpResponse
from calc.models import user,gd,pt,pi,interviewer,apt,essay,resume
import numpy as np
import pandas as pd 
# Create your views here.
def home(request):
    use=user.objects.get(email='ravindrareddy1217@gmail.com')
    idc=use.id
    ap=apt.objects.get(id=idc)
    feeda=ap.feedback
    gfeed=feeda
    splindex=feeda
    feedp=feeda
    inter=interviewer.objects.all()
    gds=gd.objects.get(id=idc)
    feedg=gd.feedback
    interr1=gds.interviewer1
    interr2=gds.interviewer2
    resum=resume.objects.get(id=idc)
    essa=essay.objects.get(id=idc)
    pii=pi.objects.get(id=idc)
    interr11=pii.interviewer1
    interr22=pii.interviewer2
    return render(request,'html.html',{'use':use,'splindex':splindex,'gfeed':gfeed,'ap':ap,'feedp':feedp,'gds':gds,'interr1':interr1,'interr2':interr2,'resum':resum,'essa':essa,'pii':pii,'interr11':interr11,'interr22':interr22})
   