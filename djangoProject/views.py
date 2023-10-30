from  django.shortcuts import render


def bmi_calculator(request):
    if request.method == "POST":
        name = request.POST.get('jina')
        weight= request.POST.get('uzito')
        height= request.POST.get('urefu')
        bmi=float(weight) /( float (height) *  float(height))
        bmi_result = ""
        if bmi <= 18:
            bmi_result="Underweight"
        elif bmi <= 29:
            bmi_result="Normal Weight"
        elif bmi <=34:
            bmi_result ="Overweight"
        else:
            bmi_result = "Obese"
        context = {"name": name, "bmi": bmi, "bmi_result": bmi_result}
        return render(request, 'bmi-calculator.html', context)
    return render (request, 'bmi-calculator.html')


def home(request):
    return render (request,'index.html')

def verify(request):
    if request.method =="POST":
        age = request.POST.get('userAge')
        email = request.POST.get('userEmail')
        password = request.POST.get('userPassword')

        if email == "emobilis@test.com"  and password == "test123":
            if int(age) < 18:
                age_result = "Underage"
            else:
                age_result = "Adult"
            context = {"age_result": age_result }
            return render(request,'form.html',context)
    return render(request, 'form.html')

