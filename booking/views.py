from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import ast
from django.http import HttpResponse
# Create your views here.

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            print('lol', request.POST)
            user = form.save()
            Booker.objects.create(user = user,)
            
            user = authenticate(username = form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
            login(request, user)
            return redirect('accountsettings')

    context = {'form':form}

    return render(request,'booking/register.html',context)
    
def logIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print('uuuuuuu', username)
        print('pppppppp', password)
        print('dsfs',user)
        if user is not None:
            login(request, user)
            return redirect('dashboard')

        else:
            messages.info(request, 'Enter correct credentials')
            return render(request, 'booking/login.html')

    context ={}

    return render(request,'booking/login.html', context)

def logOut(request):
    logout(request)
    return redirect('login')
@login_required(login_url='login') 
def createTrain(request):
    rp = request.POST
    tr = Train()
    tr.train_name = rp.get('train_name')
    tr.train_number = rp.get('train_number')
    train_rows = rp.get('train_rows')
    if request.method == 'POST':
        avl_seats = [i for i in range(1,(int(train_rows)*6)+1)]
        tr.available_seats = avl_seats
        tr.rows_available = int(train_rows)
        window_seats =[]
        middle_seats =[]
        aisle_seats =[]

        # for each in  range(0,(int(train_rows)*6)+1):
        #     if each%6 == 0:
        #         ll = [each,each+1]
        #         window_seats.extend(ll)

        for x in range(int(train_rows)):
            a = 2+(x*6)
            b = 5+(x*6)
            c = 3+(x*6)
            d = 4+(x*6)
            ee = 1+(x*6)
            q = 6+(x*6)
            window_seats.append(ee)
            window_seats.append(q)
            middle_seats.append(a)
            middle_seats.append(b)
            aisle_seats.append(c)
            aisle_seats.append(d)
        tr.middle_seats = middle_seats
        tr.aisle_seats = aisle_seats
        # window_seats.remove(0)        
        tr.window_seats= window_seats
        tr.booked_seats = []
        tr.seat_agent = {}
        tr.save()
    context = {'form':{}}
    return render(request, 'booking/createe.html',context)

@login_required(login_url='login') 
def dashboard(request):

    trains = Train.objects.all()
    # print('sdfas',trains)

    context = {'trains':trains}
    return render(request,'booking/dashboard.html',context)

@login_required(login_url='login') 
def book(request,pk):
    train = Train.objects.get(id=pk)
    # if request.method == 'POST':
    tas = train.available_seats
    tws = ast.literal_eval(train.window_seats)
    tms = ast.literal_eval(train.middle_seats)
    tais = ast.literal_eval(train.aisle_seats)
    uid = request.user.id
    print(uid)
    booker = Booker.objects.get(user_id=uid)
    print(booker.user.username)
    if request.method == "POST":
        rp = request.POST
        print(request.POST)
        tas = ast.literal_eval(train.available_seats)
        tws = ast.literal_eval(train.window_seats)
        tsa = ast.literal_eval(train.seat_agent)
        tbs = ast.literal_eval(train.booked_seats)
        
        age = int(rp.get('age'))
        gender = rp.get('gender')
        passenger_name = rp.get('passenger_name')
        seat_numb = int(rp.get('seat_number'))
        print(tas)
        print(seat_numb)
        if seat_numb in tas:
            print('hi')
            adjacent_seats=[]
            if seat_numb in tws:
                if seat_numb%2==0:
                    nex_seat= seat_numb-1
                    adjacent_seats.append(nex_seat)
                    print(nex_seat)
                else:
                    nex_seat = seat_numb+1
                    adjacent_seats.append(nex_seat)

            elif seat_numb in tms:
                nex_seat = seat_numb +1
                nex_seat1 = seat_numb -1
                adjacent_seats.append(nex_seat)
                adjacent_seats.append(nex_seat1)
            elif seat_numb in tais:
                if seat_numb%3==0:
                    nex_seat= seat_numb-1
                    adjacent_seats.append(nex_seat)
                else:
                    nex_seat = seat_numb+1
                    adjacent_seats.append(nex_seat)
            print(adjacent_seats)
            
        #     for nex_seat in adjacent_seats:                    
        #         if nex_seat in tas:
        #             tas.remove(seat_numb)
        #             tbs.append(seat_numb)
        #             tsa[seat_numb]=uid
        #             print(tas)
        #             print(tsa)
        #             train.available_seats = tas
        #             train.seat_agent = tsa
        #             train.booked_seats = tbs
        #             train.save()
        #             Passengers.objects.create(booker = booker, train =train, p_name = passenger_name, age =age, gender = gender, seat_number= seat_numb )
        #             return redirect('dashboard')
                    

        #         else:
        #             # print('dfgrytry',tsa[nex_seat])
        #             if tsa[nex_seat]== uid:
        #                 tas.remove(seat_numb)
        #                 tbs.append(seat_numb)
        #                 tsa[seat_numb]=uid
        #                 train.available_seats = tas
        #                 train.seat_agent = tsa
        #                 train.booked_seats = tbs
        #                 train.save()
        #             else:
        #                 np = Passengers.objects.get(seat_number=nex_seat)
        #                 if np.gender == 'Male':
        #                     tas.remove(seat_numb)
        #                     tbs.append(seat_numb)
        #                     tsa[seat_numb]=uid
        #                     train.available_seats = tas
        #                     train.seat_agent = tsa
        #                     train.booked_seats = tbs
        #                     train.save()

        #                 else :
        #                     if gender == 'Female':
        #                         tas.remove(seat_numb)
        #                         tbs.append(seat_numb)
        #                         tsa[seat_numb]=uid
        #                         train.available_seats = tas
        #                         train.seat_agent = tsa
        #                         train.booked_seats = tbs
        #                         train.save()
        #                     else :
        #                         messages.info(request, "Please try another seat to book ")
        #                         return render(request,'booking/book.html',context)
        # else :
        #     messages.info(request, "Please try another seat to book ")
            # return render(request,'booking/book.html',context)       
            check = False
            for nex_seat in adjacent_seats:                    
                if nex_seat in tas:
                    check = True
                    

                else:
                    # print('dfgrytry',tsa[nex_seat])
                    if tsa[nex_seat]== uid:
                        check = True
                    else:
                        np = Passengers.objects.get(seat_number=nex_seat)
                        if np.gender == 'Male':
                            check = True

                        else :
                            if gender == 'Female':
                                check = True
                            else :
                                check = False
                                messages.info(request, "Please try another seat to book ")
                                return render(request,'booking/book.html',context)

            if check == True:
                tas.remove(seat_numb)
                tbs.append(seat_numb)
                tsa[seat_numb]=uid
                print(tas)
                print(tsa)
                train.available_seats = tas
                train.seat_agent = tsa
                train.booked_seats = tbs
                train.save()
                Passengers.objects.create(booker = booker, train =train, p_name = passenger_name, age =age, gender = gender, seat_number= seat_numb )
                return redirect('dashboard')

        else :
            messages.info(request, "Please try another seat to book ")



        # if tas:
        #     age = int(rp.get('age'))
        #     gender = rp.get('gender')
        #     passenger = rp.get('passenger_name')
        #     if age > 60:
        #         if tws:
        #             window = min(tws)
        #             tws.remove(window)
        #             seat_agent = {window:uid}
        #             tsa.append(seat_agent)
        #         elif tas:
        #             normal = min(tas)
        #             if normal not in tsa:
        #                 seat_agent = {normal:uid}                        



        # form = passengerForm(request.POST)
        # form.save()
        # ii = form.cleaned_data.get('seat_number')
        # tas.remove(ii) 
    context= {'train':train,'pk':pk,'ra':tas,'tws':tws,'tms':tms, 'tais':tais}

    return render(request,'booking/book.html',context)


def accountsettings(request):
    form1 = extraForm()
    uid = request.user.id
    booker = Booker.objects.get(user_id=uid)
    if request.method == 'POST':
        print(request.POST)
        form1 = extraForm(request.POST, instance= booker)
        print(form1.is_valid())
        if form1.is_valid():
            print('Llolll')
            form1.save()
            return redirect('dashboard')

    context={'form1':form1,}
    return render(request,'booking/settings.html',context)

def history(request):
    uid = request.user.id
    booker = Booker.objects.get(user_id=uid)
    pss = booker.passengers_set.all()
    # for p in pss:
    context = {'pss':pss}
    return render(request, 'booking/history.html', context)