#i hv created this python file
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
    #return HttpResponse ("HOME")
def analyze(request):
    #get the text
    djtext=request.POST.get('text', 'default')
    print(djtext)
    #Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    #check which checkbox is on
    if(removepunc == "on"):
        punctuations = '''!()-{}[];:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params ={'purpose':'Removed punctuations','analyzed_text':analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # analyze the text
        #return render(request, 'analyze.html', params)
    if(newlineremover=="on"):
        analyzed =""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed Newlines', 'analyzed_text': analyzed}
        djtext = analyzed
        # analyze the text
        #return render(request, 'analyze.html', params)
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index +1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra space remover', 'analyzed_text': analyzed}
        djtext = analyzed
        # analyze the text
        #return render(request, 'analyze.html', params)
    if (charcounter == "on"):
        analyzed = djtext
        params = {'purpose': 'Counting Characters', 'analyzed_text': len(analyzed)}
       # djtext = analyzed
        # analyze the text
        #return render(request, 'analyze.html', params)
    #else:
        #return HttpResponse("Error")
    if (removepunc != "on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover != "on" and charcounter != "on"):
        return HttpResponse("Please select any operation and try again")
    return render(request, 'analyze.html', params)
#def capfirst(request):
    #return HttpResponse('''<h1> CAPITALIZE FIRST </h1> <a href="http://127.0.0.1:8000/">click to go back</a>''')
#def newlineremove(request):
    #return HttpResponse('''<h1> NEWLINE REMOVE </h1> <a href="http://127.0.0.1:8000/">click to go back</a>''')
#def spaceremove(request):
    #return HttpResponse('''<h1> SPACE REMOVE </h1> <a href="http://127.0.0.1:8000/">click to go back</a>''')
#def charcount(request):
    #return HttpResponse('''<h1> CHAR COUNT </h1> <a href="http://127.0.0.1:8000/">click to go back</a>''')