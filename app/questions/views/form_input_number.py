from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def form_input_number(request):
    if request.method == "POST":
        num1 = int(request.POST["num1"])
        num2 = int(request.POST["num2"])
        result = num1 + num2
        print("num1:", num1)
        print("num2:", num2)
        print("result:", result)
    return render(request, "questions/form_input_number.html")
