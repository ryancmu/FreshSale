from django.shortcuts import render_to_response
#from django.template.loader import get_template
#from django.template import Template, Context
#from django.http import HttpResponse
import datetime

def current_datetime(request):
    current_date = datetime.datetime.now()
    ##t = Template("<html><body>It is now {{ current_date }}.</body></html>")
    #t = get_template('current_datetime.html')
    #html = t.render(Context({ 'current_date' : now}))
    #return HttpResponse(html)
    current_location = 'Madison'
    return render_to_response('current_datetime.html', locals())


