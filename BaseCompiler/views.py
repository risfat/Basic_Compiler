import sys

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from BaseCompiler.src.execute import BasicExecute
from BaseCompiler.src.lexer import BasicLexer
from BaseCompiler.src.parser import BasicParser


def index(request):
    return render(request, 'index.html')


def runcode(request):
    if request.method == "POST":
        codeAreaData = request.POST['code']

        print(codeAreaData)

        try:

            lexer = BasicLexer()
            parser = BasicParser()
            env = {}

            text = codeAreaData

            if text:

                splitCode = text.splitlines(True)

                print(splitCode)
                for x in splitCode:
                    tree = parser.parse(lexer.tokenize(x.replace("\r\n", "")))
                    executeObject = BasicExecute(tree, env)
                    output = executeObject.returnResult

        except Exception as e:
            # to return error in the code
            output = e

    # finally return and render index page and send codeData and output to show on page

    return render(request, 'index.html', {"code": codeAreaData, "output": output})


def ajax_runcode(request):
    if request.method == "POST":
        codeAreaData = request.POST['code']

        print(codeAreaData)

        try:

            lexer = BasicLexer()
            parser = BasicParser()
            env = {}

            text = codeAreaData

            if text:

                splitCode = text.splitlines(True)

                print(splitCode)
                for x in splitCode:
                    tree = parser.parse(lexer.tokenize(x.replace("\r\n", "")))
                    executeObject = BasicExecute(tree, env)
                    output = executeObject.returnResult

        except Exception as e:
            # to return error in the code
            output = e

    # finally return and render index page and send codeData and output to show on page

    print("------------------------")
    print(output)
    print("------------------------")

    return JsonResponse({'result': output})
