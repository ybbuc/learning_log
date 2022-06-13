import imp
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


def register(request):
    if request.method != "POST":
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to the home page.
            login(request, new_user)
            return redirect("learning_logs:index")

    # Display a blank or invalid form.
    context = {"form": form}
    return render(request, "registration/register.html", context)
