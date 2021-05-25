from django.shortcuts import render, HttpResponse
from .models import Coffee
from .forms import CoffeeForm
# Create your views here.
# 먼저 함수를 구현해야합니다.

def index(request):
    name = "Micheal"

    nums = [1,2,3,4,5]

    return render(request, 'index.html', {"my_name":name, "my_list":nums})

def me(request):
    nums = [i for i in range(1,11)]
    idx = [i+1 for i in range(1,10)]

    return render(request, 'me.html', {"game_num":nums, "idx":idx})

def coffee_view(request):
    coffee_all = Coffee.objects.all()
    # 만약 request가 POST라면:
        # POST를 바탕으로 Form을 완성하고
        # Form이 유효하면 -> 저장!
    if request.method == "POST":
        form = CoffeeForm(request.POST)
        if form.is_valid():
            form.save()
    
    form = CoffeeForm()
    return render(request, 'coffee.html', {"coffee_list":coffee_all, "coffee_form":form})

def eda(request):
    return render(request, 'eda.html',{})