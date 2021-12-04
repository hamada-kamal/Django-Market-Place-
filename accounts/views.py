from django.shortcuts import render , redirect , get_object_or_404
# from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm
from django.contrib.auth import login , authenticate
from .models import Profile
from .forms import UserForm , ProfileForm, EditUserForm, CustomerForm
from django.contrib.auth.decorators import login_required
from products.models import Customer, Product
from products.utils import CartData



def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.customer.name = form.cleaned_data.get('first_name') + ' ' + form.cleaned_data.get('last_name')
            user.customer.phone = form.cleaned_data.get('phone')
            user.customer.email = form.cleaned_data.get('email')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)

            login(request, user)
            return redirect('/products')

    else:
        form = UserForm()

    context = {'form': form}
    return render(request , 'registration/signup.html' , context)


@login_required(login_url='/accounts/login/')
def profile(request):
    profile = get_object_or_404(Profile , user=request.user)
    customer = request.user.customer
    liked_products = Product.objects.filter(like=customer)
    data = CartData(request)
    cartItems = data['cartItems']
    context = {'profile' : profile,'cartItems': cartItems, 'customer': customer,'liked_products':liked_products,}
    return render(request , 'profile.html' , context)


def editProfile(request):
    profile = Profile.objects.get(user=request.user)
    customer = Customer.objects.get(user=request.user)
    liked_products = Product.objects.filter(like=customer)
    if request.method == 'POST':
        userform = EditUserForm(request.POST , instance=request.user)
        profile_form = ProfileForm(request.POST,request.FILES ,instance=profile)
        customer_form = CustomerForm(request.POST ,instance=customer)
        if userform.is_valid() and profile_form.is_valid():
            userform.save()
            
            myform, myform2 = profile_form.save(commit=False), customer_form.save(commit=False)
            myform.user, myform2.user= request.user, request.user
            myform.save()
            myform2.save()
            # messages.success(request,'Your Profile Updated Successfully')
            return redirect('/accounts/profile')
        pass
    else:  ## show
        userform = EditUserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
        customer_form = CustomerForm(instance=customer)
    data = CartData(request)
    cartItems = data['cartItems']
    return render(request,'profile_edit.html',
    {'userform' : userform ,
     'profile_form' : profile_form,
     'customer_form':customer_form,
     'profile':profile,
     'liked_products':liked_products,
     'cartItems': cartItems,
       })


def AccountSettings(request):
    data = CartData(request)
    cartItems = data['cartItems']
    return render(request,'settings.html',{'cartItems':cartItems})