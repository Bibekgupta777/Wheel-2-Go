from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from CustomerHome.models import Customer
from Owner.models import Owner
from Manager.models import Manager
from Vehicles.models import Vehicle
from RentVehicle.models import RentVehicle
from .models import Contact
from .models import Feedback
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from .models import Feedback


from datetime import datetime
from datetime import date

isLogin = False
isLogout = False

# Create your views here.
def index(request):
    global isLogin
    global isLogout

    if('user_email' in request.session):
        email = request.session.get('user_email')

        result_customer = Customer.objects.filter(customer_email=email)
        result_owner = Owner.objects.filter(Owner_email=email)
        result_manager = Manager.objects.filter(Manager_email=email)

        if result_customer.exists():
            request.session['user_email'] = email
            isLogin = True
            return redirect('/Home/')
        elif result_owner.exists():
            request.session['user_email'] = email
            isLogin = True
            return redirect('/Owner/')
        elif result_manager.exists():
            request.session['user_email'] = email
            isLogin = True
            return redirect('/Manager/')
        return redirect('/Home/')

    vehicle = Vehicle.objects.all()
    if('user_email' not in request.session and isLogout):
        isLogin = False
        isLogout = False
        Message = "Successfully Logged Out!!"
        return render(request,'index.html',{'Message':Message,'vehicle':vehicle})
    return render(request,'index.html',{'vehicle':vehicle})

def signin(request):
    return render(request,'SignIn.html')

def register(request):
    return render(request,'register.html')

def LoginAuthentication(request):
    global isLogin
    login_email=request.POST.get('login_email','')
    login_password=request.POST.get('login_password','')
    # customer = Customer.objects.all()

    result_customer = Customer.objects.filter(customer_email=login_email,customer_password=login_password)
    result_owner = Owner.objects.filter(Owner_email=login_email,Owner_password=login_password)
    result_manager = Manager.objects.filter(Manager_email=login_email,Manager_password=login_password)

    if result_customer.exists():
        request.session['user_email'] = login_email
        isLogin = True
        return redirect('/Home/')
    elif result_owner.exists():
        request.session['user_email'] = login_email
        isLogin = True
        return redirect('/Owner/')
    elif result_manager.exists():
        request.session['user_email'] = login_email
        isLogin = True
        return redirect('/Manager/')
    else:
        Message = "Invalid Email or password!!"
        return render(request,'SignIn.html',{'Message':Message})

def RegisterCustomer(request):
    global isLogin

    customer_firstname=request.POST.get('customer_firstname','')
    customer_lastname=request.POST.get('customer_lastname','')
    customer_dob=request.POST.get('customer_dob','')
    customer_gender=request.POST.get('customer_gender','')
    customer_mobileno=request.POST.get('customer_mobileno','')
    customer_email=request.POST.get('customer_email','')
    customer_password=request.POST.get('customer_password','')
    customer_address=request.POST.get('customer_address','')
    customer_city=request.POST.get('customer_city','')
    customer_state=request.POST.get('customer_state','')
    customer_country=request.POST.get('customer_country','')
    customer_pincode=request.POST.get('customer_pincode','')
    customer_license=request.FILES['customer_license']

    result_customer = Customer.objects.filter(customer_email=customer_email)
    result_owner = Owner.objects.filter(Owner_email=customer_email)
    result_manager = Manager.objects.filter(Manager_email=customer_email)

    if result_customer.exists() or result_owner.exists() or result_manager.exists():
        Message = "This Email address already exist!!"
        return render(request,'register.html',{'Message':Message})
    else:
        customer=Customer(customer_firstname=customer_firstname,customer_lastname=customer_lastname,
        customer_dob=customer_dob,customer_gender=customer_gender,customer_mobileno=customer_mobileno,
        customer_email=customer_email,customer_password=customer_password,customer_address=customer_address,
        customer_city=customer_city,customer_state=customer_state,customer_country=customer_country,
        customer_pincode=customer_pincode,customer_license=customer_license)
        
        customer.save()
        request.session['user_email'] = customer_email
        isLogin = True
        return redirect('/Home/')

def Logout(request):
    global isLogout
    del request.session['user_email']
    isLogout = True
    Message = "Successfully Logged Out!!"
    return redirect('/')

def Home(request):
    if('user_email' not in request.session):
        return redirect('/signin/')
    customer_email = request.session.get('user_email')
    customer = Customer.objects.get(customer_email=customer_email)
    vehicle = Vehicle.objects.all()
    Message="Welcome Aboard!!"
    return render(request,'Home.html',{'vehicle':vehicle,'Message':Message,'customer':customer})

def Profile(request):
    if('user_email' not in request.session):
        return redirect('/signin/')
    customer_email = request.session.get('user_email')
    customer = Customer.objects.get(customer_email=customer_email)
    return render(request,'Profile.html',{'customer':customer})

def showdetails(request,Vehicle_license_plate):
    vehicle = Vehicle.objects.get(Vehicle_license_plate=Vehicle_license_plate)
    if('user_email' not in request.session):
        return render(request,'showdetails_not_login.html',{'vehicle':vehicle})
    else:
        customer_email = request.session.get('user_email')
        customer = Customer.objects.get(customer_email=customer_email)
        return render(request,'showdetails_loggedin.html',{'vehicle':vehicle,'customer':customer})

def CheckAvailability(request,Vehicle_license_plate):
    if('user_email' not in request.session):
        return redirect('/signin/')

    RentVehicle_Date_of_Booking=request.POST.get('RentVehicle_Date_of_Booking','')
    RentVehicle_Date_of_Return=request.POST.get('RentVehicle_Date_of_Return','')
    
    RentVehicle_Date_of_Booking = datetime.strptime(RentVehicle_Date_of_Booking, '%Y-%m-%d').date()
    RentVehicle_Date_of_Return = datetime.strptime(RentVehicle_Date_of_Return, '%Y-%m-%d').date()

    rentvehicle = RentVehicle.objects.filter(Vehicle_license_plate=Vehicle_license_plate)
    vehicle = Vehicle.objects.get(Vehicle_license_plate=Vehicle_license_plate)

    customer_email = request.session.get('user_email')
    customer = Customer.objects.get(customer_email=customer_email)

    if RentVehicle_Date_of_Booking < date.today():
        Incorrect_dates = "Please give proper dates"
        return render(request,'showdetails_loggedin.html',{'Incorrect_dates':Incorrect_dates,'vehicle':vehicle,'customer':customer})

    if RentVehicle_Date_of_Return < RentVehicle_Date_of_Booking:
        Incorrect_dates = "Please give proper dates"
        return render(request,'showdetails_loggedin.html',{'Incorrect_dates':Incorrect_dates,'vehicle':vehicle,'customer':customer})
    
    days=(RentVehicle_Date_of_Return-RentVehicle_Date_of_Booking).days+1
    total=days*vehicle.Vehicle_price
    
    rent_data = {"RentVehicle_Date_of_Booking":RentVehicle_Date_of_Booking, "RentVehicle_Date_of_Return":RentVehicle_Date_of_Return,"days":days, "total":total}
    
    for rv in rentvehicle:

        if (rv.RentVehicle_Date_of_Booking >= RentVehicle_Date_of_Booking and RentVehicle_Date_of_Return >= rv.RentVehicle_Date_of_Booking) or (RentVehicle_Date_of_Booking >= rv.RentVehicle_Date_of_Booking and RentVehicle_Date_of_Return <= rv.RentVehicle_Date_of_Return) or (RentVehicle_Date_of_Booking <= rv.RentVehicle_Date_of_Return and RentVehicle_Date_of_Return >= rv.RentVehicle_Date_of_Return):
            if rv.isAvailable:
                Available = True
                Message = "Note that somebody has also requested for this vehicle from " + str(rv.RentVehicle_Date_of_Booking) + " to " + str(rv.RentVehicle_Date_of_Return)
                return render(request,'showdetails_loggedin.html',{'Message':Message,'Available':Available,'vehicle':vehicle,'customer':customer,'rent_data':rent_data})

            NotAvailable = True
            return render(request,'showdetails_loggedin.html',{'NotAvailable':NotAvailable,'dates':rv,'vehicle':vehicle,'customer':customer})

      
    Available = True
    return render(request,'showdetails_loggedin.html',{'Available':Available,'vehicle':vehicle,'customer':customer,'rent_data':rent_data})

def SentRequests(request):
    if('user_email' not in request.session):
        return redirect('/signin/')

    customer_email = request.session.get('user_email')
    customer = Customer.objects.get(customer_email=customer_email)

    rentvehicle = RentVehicle.objects.filter(customer_email=customer_email)
    if rentvehicle.exists():
        vehicle = Vehicle.objects.all()
        return render(request,'SentRequests.html',{'customer':customer,'rentvehicle':rentvehicle,'vehicle':vehicle})
    else:
        Message = "You haven't rented any vehicle yet!!"
        return render(request,'SentRequests.html',{'customer':customer,'rentvehicle':rentvehicle,'Message':Message})

def about_us(request):
    return HttpResponse('About Us')
    
# def contact_us(request):
#     return HttpResponse('Contact Us')

def search(request):
    return HttpResponse('search')


def aboutus(request):
    return render(request,"aboutUs.html")


def contact(request):
    if request.method=="POST":
      contact=Contact()
      name=request.POST.get('name')
      email=request.POST.get('email')
      subject=request.POST.get('subject')
      contact.name=name
      contact.email=email
      contact.subject=subject
      contact.save()
    #   return HttpResponse("<h1>Thanks for contact</h1>")


    return render(request,"contactus.html")




from django.shortcuts import render

def privacy_policy(request):
    return render(request, 'privacy_policy.html')




def terms(request):
    return render(request, 'termsofuse.html')





def aboutwithout(request):
    return render(request, 'aboutuswithoutlogin.html')




def aprivacy(request):
    return render(request, 'aprivacy.html')



def aterms(request):
    return render(request, 'aterms.html')







def feedrating(request):
    if request.method == "POST":
        feedback = Feedback()
        email = request.POST.get('email')
        rating = request.POST.get('rating')
        feedback_text = request.POST.get('feedback')  # Use a different variable name

        feedback.email = email
        feedback.rating = rating
        feedback.feedback = feedback_text  # Use the correct variable

        feedback.save()
        # return HttpResponse("<h1>Thanks for your feedback</h1>")

    return render(request, 'feedback.html')