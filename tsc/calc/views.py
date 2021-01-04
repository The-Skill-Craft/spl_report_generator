from django.shortcuts import render
from django.http import HttpResponse
from calc.models import user,gd,pt,pi,interviewer,apt,essay,resume
import numpy as np
import pandas as pd 
from django.views.generic import View
from io import BytesIO
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
# Create your views here.
def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None
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
data= {
'use':use,'splindex':splindex,'gfeed':gfeed,'ap':ap,'feedp':feedp,'gds':gds,'interr1':interr1,'interr2':interr2,'resum':resum,'essa':essa,'pii':pii,'interr11':interr11,'interr22':interr22
}
class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		
		pdf = render_to_pdf('app/pdf_template.html', data)

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Invoice_%s.pdf" %("12341231")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response
class Viewpdf(View):
	def get(self, request, *args, **kwargs):
		pdf = render_to_pdf('html.html', data)
		return HttpResponse(pdf, content_type='application/pdf')
def home(request):
    return render(request,'home.html')
def html(request):
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
   