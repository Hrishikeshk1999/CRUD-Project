from django.shortcuts import render,redirect
from clickit.models import Cam

# Create your views here.
def home(request):
    return render(request,'index.html')

def orders(request):
    context={}
    data = Cam.objects.all()
    print(type(data))
    context['cams']=data
    return render(request,'list.html',context)

def buy(request):
    return render(request,'add.html')

def savecam(request):
    print(request.method)
    c= request.POST['Camera']
    l= request.POST['Lens']
    p= int(request.POST['Price'])
    # print(c, l, p)
    # print(type(c), type(l), type(p))
    b = Cam.objects.create(camera=c, lens=l, price=p)
    print('Equipment added')
    b.save()
    # return render(request,'index.html')
    return redirect('/list')

def vanhish(request,rid):
    cam = Cam.objects.filter(id = rid)
    print(type(cam))
    cam.delete()
    context = {'success':'Equipment removed from cart!'}
    # return render(request,'list.html',context)
    return redirect('/list')

def editorder(request,rid):
    cam = Cam.objects.filter(id=rid)
    context={}
    if request.method == "GET":
        context['cam']=cam[0]
        return render(request, 'editorder.html',context)
    else:
        c=request.POST['Camera']
        l=request.POST['Lens']
        p=int(request.POST['Price'])
        cam.update(camera=c, lens=l, price=p)
        return redirect('/list')

