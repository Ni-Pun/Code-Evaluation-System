from django.shortcuts import render, HttpResponse
from django.utils import timezone
from OJ import runcode
# Create your views here.

from .models import Problem,TestCase,Submission


def index(request):
    problem_list = Problem.objects.all()
    
    context = {
        'problem_list' : problem_list,
    }
    return render(request, 'OJ/index.html', context)
    

def detail(request, Id):

    problem = Problem.objects.get(Id=Id)
    context = {
        'problem' : problem,
    }
    return render(request, 'OJ/details.html', context)



def validate(request,Id):
    problem=Problem.objects.get(Id=Id)
    find=str(problem.Id) + '.   ' + problem.Name
    testcases=list(TestCase.objects.filter(problem=Id))
    inp=[]
    out=[]
    for d in testcases:
        inp.append(d.input)
        out.append(d.output)
    if request.method == 'POST':
        code = request.POST['code']
        typecode = request.POST['type']
        # typ = request.POST['type']
        # print(typecode)
        run = runcode.RunPyCode(typecode,inp, code)
        rescompil, resrun = run.run_py_code(typecode,inp)
        resrun=resrun
        rescomp=rescompil

        if not rescomp:
            if not resrun:
                resrun = 'No result!'
    else:
        code = default_py_code
        resrun = 'No result!'
        rescompil = "No compilation for "+ typecode
    fout=[]
    x=1
    check=0
    for i in range(0,len(out)):
        if(resrun!=None and out[i].rstrip()==resrun[i].rstrip()):
            fout.append([x,1])
        else:
            fout.append([x,0])
            check=1
        x=x+1
    verdict=""    
    if check==1:
        verdict="Failed"
    else:
        verdict="Success"
    p = Submission.objects.create(problem=problem, verdict=verdict, submittedAt=timezone.now())

    return render (request,'OJ/results.html', {'code':code,'resrun':resrun,'fout':fout,'rescomp':rescomp})     

