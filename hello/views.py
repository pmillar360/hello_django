from django.shortcuts import redirect, render
from django.utils.timezone import datetime
from django.views.generic import ListView
from hello.forms import LogMessageForm
from hello.models import LogMessage

def hello_there(request, name):
    print(request.build_absolute_uri())
    
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now(),
        }
    )

# def home(request):
#     return render(request, "hello/home.html")

class HomeListView(ListView):
    """Render the home page with a list of all messages"""
    model = LogMessage

    def get_context_data(self, **kwargs):
        return super(HomeListView, self).get_context_data(**kwargs)
    

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "hello/log_message.html", {"form": form})