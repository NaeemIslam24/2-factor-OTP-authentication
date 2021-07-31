from django.shortcuts import redirect, render
from codes.forms import CodeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from users.models import CustomUser


def auth(request):
    template = "auth.html"

    form = AuthenticationForm()

    if request.method == "POST":
        use = request.POST.get("username")
        passw = request.POST.get("password")

        user = authenticate(request, username=use, password=passw)

        if user is not None:
            request.session["pk"] = user.pk

            return redirect("varify")

    context = {"form": form}

    return render(request, template_name=template, context=context)


def varify_view(request):

    codeForm = CodeForm(request.POST or None)

    pk = request.session.get("pk")
    if pk:
        user = CustomUser.objects.get(id=pk)

        code = user.code

        print(code)

        code_user = f"{user.username}: {user.code}"
        if not request.POST:
            pass
        if codeForm.is_valid():
            num = codeForm.cleaned_data.get("number")
            if str(code) == num:
                code.save()
                login(request, user)
                return redirect("home")
            else:
                return redirect("login")
    context = {
        "form": codeForm,
    }

    return render(request, "varify.html", context=context)


@login_required
def home(request):

    return render(request, "index.html")
