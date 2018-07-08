from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
@csrf_exempt
def index(request):
    try:
        with open("save.txt","r") as f:
            text=f.read()
    except:
        text=None
    if request.method == "POST":
        if not text:
            text=json.dumps(request.POST)
        else:
            text+="\n\n"+json.dumps(request.POST)
        with open("save.txt","w") as f:
            f.write(text)
    if not text:
        return HttpResponse("Hello, world. You're at the polls index.")
    else:
        return HttpResponse(text)
