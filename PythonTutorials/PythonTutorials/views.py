from django.shortcuts import *
import sys

def index(request):
    return render(request,'home.htm')

def About(request):
    return render(request,'About.htm')

def onlinecompiler(request):
    return render(request,'onlinecompiler.htm')

def pythonLanguageIntro(request):
    return render(request,'pythonLanguageIntro.htm')

def PythonAdv(request):
    return render(request,'PythonAdv.htm')
def downloadAndInstall(request):
    return render(request,'downloadAndInstall.htm')

def python3basics(request):
    return render(request,'python3basics.htm')
def runcode(request):

    if request.method == "POST":
        code_area_data = request.POST['codearea']

        try:
            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')

            exec(code_area_data)

            sys.stdout.close()

            sys.stdout = original_stdout
            output = open('file.txt', 'r').read()

        except Exception as e:
            sys.stdout = original_stdout
            output = e

    return render(request , 'onlinecompiler.htm', {"code":code_area_data , "output":output})

def tempRunner(request,page):
    return 