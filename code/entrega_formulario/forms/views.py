from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "index.html")


def form(request):
    return render(request, "form.html")


def validateForm(request):
    from models import userLogin
    import json

    username = request.GET.get("username")
    password = request.GET.get("password")
    web_server = request.GET.get("webServer")
    role = request.GET.get("role")
    mail = request.GET.get("mail")
    payroll = request.GET.get("payroll")
    self_service = request.GET.get("selfService")
    try:
        user = userLogin(
            username,
            password,
            web_server,
            role,
            {"mail": mail, "payroll": payroll, "selfService": self_service},
        )

        return render(request, "index.html", {"userLogin": user})
    except Exception as e:
        return render(request, "form.html", {"error": e})
