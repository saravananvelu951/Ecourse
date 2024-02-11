from django.shortcuts import render, HttpResponse , redirect

from .models import *

from django.contrib.auth.hashers import make_password,check_password


# Create your views here.
def home(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        remove = request.POST.get('remove')
       # print("courseid",course_id)

        cart_id = request.session.get('cart')
        #print("cartid",cart_id)

        if cart_id:
            quantity = cart_id.get(course_id)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart_id.pop(course_id)
                    else:
                        cart_id[course_id] = quantity - 1
                else:
                    cart_id[course_id] = quantity   + 1
            else:
                cart_id[course_id] = 1
        else:
            cart_id = {}
            cart_id[course_id] =1
        request.session['cart'] = cart_id
        #print("requs," , request.session['cart'] )
    

     #category 
    category_obj = Category.objects.all()
    course_obj = Course.objects.all()

    category_id = request.GET.get("category_id")

    search = request.GET.get("search")

    if category_id:
        course_obj = Course.objects.filter(course_category=category_id)
    elif search:
        course_obj = Course.objects.filter(course_name__icontains=search)
    else:
        course_obj = Course.objects.all()

    context = {
        'category' : category_obj,
        'course_obj' : course_obj,
          
    }

    
    return render(request,'home.html',context=context)

def help(request):
    return render(request,'help.html')

def signup(request):

    if request.method == "POST":
        f_name = request.POST.get('fname')
        l_name = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile = request.POST.get('number')
        gender = request.POST.get('gender')
        f_name = request.POST.get('fname')

        class_obj = Registration(
            First_name = f_name,
            Last_name = l_name,
            Email = email,
            Password = make_password(password),
            Mobile = mobile,
            Gender = gender,

        )
        class_obj.save()

        return redirect('homepage')

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
    try:
        email_id = Registration.objects.get(Email=email)
        if check_password(password,email_id.Password):
            request.session['name'] = email_id.First_name
            request.session['customer_id'] = email_id.id



            return redirect('homepage')
        else:
             return HttpResponse("password wrong")
    
    except:
        return HttpResponse("mail id not match")
        
def logout(request):
    request.session.clear()
    return redirect('homepage')

def cart(request):
    cart_id = list(request.session.get('cart').keys())
    course = Course.objects.filter(id__in = cart_id)

    context ={
        'course' : course
    }

    return render(request,'cart.html', context=context)

def checkout(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        customer_id = request.session.get('customer_id')
        error = None
        if not customer_id:

            error = 'none'
            return render(request, 'home.html', {'error': error})
        
        cart_id = request.session.get('cart')
        course = Course.objects.filter(id__in= list(cart_id.keys()))

        for cor in course:
            order_obj = Order(

                address  = address,
                mobile = mobile,
                customer = Registration(id=customer_id),
                course = cor,
                quantity = cart_id.get(str(cor.id)),
                price = cor.course_price
                
                
            )
            order_obj.save()
        return redirect('order')

def order(request):
    customer_id =request.session.get('customer_id')
    order = Order.objects.filter(customer=customer_id)
    total_price = 0
    for i in order:
        total_price = total_price + i.price * i.quantity

    context ={
        "order": order,
        "total_price": total_price
    }
    
    return render(request,"order.html",context=context)

def video(request):
    customer_id = request.session.get('customer_id')
    error = None
    if not customer_id:
        error = 'none'
        return render(request, 'home.html', {'error': error})


    if not error:
        course_video = Videos.objects.all()
            
        context = {
                "course_video":course_video,
                "error":error
            }

        return render(request,"video.html",context=context)

    

from rest_framework import  viewsets

from.models import *

from .serializers import RegistrationSerializer

class registrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer 

from .serializers import OrderSerializer

class orderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer 
        

