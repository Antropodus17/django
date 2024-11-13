from django.shortcuts import render
from clases.validation import userLogin


def validate(request):
    servers = ["Apache", "Nginx", "LiteSpeed", "Microsoft IIS"]
    username = request.GET.get("username")
    password = request.GET.get("password")
    web_server = servers[int(request.GET.get("webServer"))]
    city = request.GET.get("city")
    role = request.GET.get("role")
    mail = request.GET.get("mail")
    payroll = request.GET.get("payroll")
    self_service = request.GET.get("selfService")
    try:
        user = userLogin(
            username,
            password,
            city,
            web_server,
            role,
            {"mail": mail, "payroll": payroll, "selfService": self_service},
        )

        return render(
            request,
            "index.html",
            {
                "user": vars(user),
            },
        )
    except Exception as e:
        return render(request, "form.html", {"error": e})
