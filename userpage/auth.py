from django.shortcuts import redirect

# check if user is logged in or not
def unauthenticated_user(view_function):
    def wrapper_function (request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_function(request,*args,**kwargs)
    return wrapper_function

# redirect user according to role if user is admin then redirect to admin dashboard otherwise redirect to normal user page

def admin_only(view_function):
    def wrapper_function(request,*args,**kwargs):
        if request.user.is_satff:
            return view_function(request,*args,**kwargs)
        else:
            return redirect('/')
    return wrapper_function