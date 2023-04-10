from django.http import HttpResponseNotFound, HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


def home(request):
    if request.method == 'GET':
        name_man = request.GET.get('name_man')
        name_woman = request.GET.get('name_woman')
    context = {
        'name_man': name_man,
        'name_woman': name_woman,
    }
    return render(request, 'main/index.html', context)


def checking_form(request):
    if request.method == 'POST':
        r1 = request.POST['radiobutton']
        print(r1)

        name_man = request.POST['name_man']
        name_woman = request.POST['name_woman']

        allergies = request.POST['allergies']
        night = request.POST['night']
        tomorrow = request.POST['tomorrow']
        print(name_man, name_woman, allergies, night, tomorrow)

        return HttpResponse(f"""<a id="form-send" hx-get="/send_mails/?name_man={name_man}&name_woman={name_woman}&allergies={allergies}&night={night}&tomorrow={tomorrow}" 
                                    hx-trigger="click" hx-target="#form-result" href="#" hidden>Отправить!
                                </a>""")


def send_mails(request):
    try:
        man = request.GET.get('name_man')
        woman = request.GET.get('name_woman')
        subject = 'Отправка формы'

        if man and woman:
            message = f'Форма отправлена от {man} и {woman}'
        elif man is None and woman:
            message = f'Форма отправлена от {woman}'
        elif woman is None and man:
            message = f'Форма отправлена от {man}'
        else:
            message = f'Форма отправлена от incognito'

        print(man, woman)

        mail = 'alexander_misyuta@mail.ru'
        send_mail(subject, message, 'sanja081107@gmail.com', [mail])

        return HttpResponse("")
    except:
        return HttpResponse("")


def not_will_be(request):
    return HttpResponse("""<div class="u-form-send-error u-form-send-message" style="display: block;">Thank you! Your message has been sent.<a href="#" class="u-form-send-message-close">x</a></div>""")


# def check_form_name(request):
#     if request.method == 'GET':
#         u = request.GET.get('name')
#     if u == '' or u is None:
#         return HttpResponse("""<button type="submit" class="u-btn u-button-style">Отправить</button>""")
#
#
# def check_form_email(request):
#     if request.method == 'GET':
#         u = request.GET.get('email')
#     if u == '' or u is None:
#         return HttpResponse("""<button type="submit" class="u-btn u-button-style">Отправить</button>""")
#
#
# def check_form_address(request):
#     if request.method == 'GET':
#         u = request.GET.get('address')
#     if u == '' or u is None:
#         return HttpResponse("""<button type="submit" class="u-btn u-button-style">Отправить</button>""")
