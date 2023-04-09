from django.http import HttpResponseNotFound, HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


def home(request):
    if request.method == 'GET':
        name_man = request.GET.get('name_man')
        name_woman = request.GET.get('name_woman')
        print(f'имя парня: {name_man}, имя девушки: {name_woman}')
    context = {
        'name_man': name_man,
        'name_woman': name_woman,
    }
    return render(request, 'main/index.html', context)


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

        return HttpResponse("""<div class="alert alert-dismissible fade show u-form-send-message u-form-send-success" style="display: block;" role="alert">
                                    <strong>Holy guacamole!</strong> Thank you! Your message has been sent.
                                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                                        <span aria-hidden="true">&times;</span>
                                    </button>
                                </div>""")
    except:
        return HttpResponse("""<div class="alert alert-dismissible fade show u-form-send-error u-form-send-message" style="display: block;" role="alert">
                                    <strong>Holy guacamole!</strong> You should check in on some of those fields below.
                                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                                        <span aria-hidden="true">&times;</span>
                                    </button>
                                </div>""")


def checking_form(request):
    if request.method == 'POST':
        name_man = request.POST['name_man']
        name_woman = request.POST['name_woman']

        name = request.POST['name']
        mail = request.POST['email']
        address = request.POST['address']

        if name and mail and address:
            return HttpResponse(f"""<button hx-get="/send_mails/?name_man={name_man}&name_woman={name_woman}" hx-trigger="click" hx-target="#result-main-form" class="u-btn u-button-style">Отправить!</button>""")
        else:
            return HttpResponse("""<button type="submit" class="u-btn u-button-style">Отправить</button>""")


def check_form_name(request):
    if request.method == 'GET':
        u = request.GET.get('name')
    if u == '' or u is None:
        return HttpResponse("""<button type="submit" class="u-btn u-button-style">Отправить</button>""")


def check_form_email(request):
    if request.method == 'GET':
        u = request.GET.get('email')
    if u == '' or u is None:
        return HttpResponse("""<button type="submit" class="u-btn u-button-style">Отправить</button>""")


def check_form_address(request):
    if request.method == 'GET':
        u = request.GET.get('address')
    if u == '' or u is None:
        return HttpResponse("""<button type="submit" class="u-btn u-button-style">Отправить</button>""")
