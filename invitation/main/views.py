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

        name_man = request.POST['name_man']
        name_woman = request.POST['name_woman']
        if name_man == 'None' and name_woman == 'None':
            name = request.POST['name']
        else:
            name = None
        radiobutton = request.POST['radiobutton']
        allergies = request.POST['allergies']
        night = request.POST['night']
        tomorrow = request.POST['tomorrow']
        arrive = request.POST['arrive']
        print(name_man, name_woman, name, radiobutton, allergies, night, tomorrow, arrive)

        return HttpResponse(f"""<a id="form-send" hx-get="/send_mails/?name_man={name_man}&name_woman={name_woman}&name={name}&radiobutton={radiobutton}&allergies={allergies}&night={night}&tomorrow={tomorrow}&arrive={arrive}" 
                                    hx-trigger="click" hx-target="#form-result" href="#" hidden>Отправить!
                                </a>""")


def send_mails(request):
    try:
        man = request.GET.get('name_man')
        woman = request.GET.get('name_woman')
        name = request.GET.get('name')
        radiobutton = request.GET.get('radiobutton')
        allergies = request.GET.get('allergies')
        night = request.GET.get('night')
        arrive = request.GET.get('arrive')

        if man != 'None' and woman != 'None':
            subject = f'Ответ от {man} и {woman}'
        elif man == 'None' and woman != 'None':
            subject = f'Ответ от {woman}'
        elif woman == 'None' and man != 'None':
            subject = f'Ответ от {man}'
        else:
            subject = f'Ответ от {name}'

        message = f'Ответ: {radiobutton} \n' \
                  f'Аллергии: {allergies} \n' \
                  f'Ночевка: {night} \n' \
                  f'Прибытие: {arrive}'

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
