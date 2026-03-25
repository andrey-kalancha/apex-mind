from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
import json

from .models import PartnerRequest, SurveyResponse


def home(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'partner':
            partner = PartnerRequest.objects.create(
                name=request.POST.get('name', ''),
                company=request.POST.get('company', ''),
                position=request.POST.get('position', ''),
                phone=request.POST.get('phone', ''),
                email=request.POST.get('email', ''),
                message=request.POST.get('message', '')
            )

            try:
                send_mail(
                    subject='Новая заявка с сайта APEX MIND',
                    message=(
                        f'Имя: {partner.name}\n'
                        f'Компания: {partner.company}\n'
                        f'Должность: {partner.position}\n'
                        f'Телефон: {partner.phone}\n'
                        f'Email: {partner.email}\n'
                        f'Сообщение: {partner.message}\n'
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=['info@apexmind.ru'],
                    fail_silently=False,
                )
            except Exception:
                pass

            messages.success(
                request,
                'Спасибо! Заявка отправлена, мы свяжемся с вами.',
                extra_tags='partner'
            )
            return redirect('/#application')

        elif form_type == 'survey':
            SurveyResponse.objects.create(
                company=request.POST.get('company', ''),
                position=request.POST.get('position', ''),
                q1=int(request.POST.get('q1', 1)),
                q2=int(request.POST.get('q2', 1)),
                q3=int(request.POST.get('q3', 1)),
                q4=int(request.POST.get('q4', 1)),
                q5=int(request.POST.get('q5', 1)),
                q6=int(request.POST.get('q6', 1)),
                q7=int(request.POST.get('q7', 1)),
                q8=int(request.POST.get('q8', 1)),
                q9=int(request.POST.get('q9', 1)),
                q10=int(request.POST.get('q10', 1)),
            )

            messages.success(
                request,
                'Спасибо! Ответы опроса сохранены.',
                extra_tags='survey'
            )
            return redirect('/#survey')

    return render(request, 'core/index.html')


@login_required
def dashboard(request):
    responses = SurveyResponse.objects.all()

    avg_q1 = responses.aggregate(Avg('q1'))['q1__avg'] or 0
    avg_q2 = responses.aggregate(Avg('q2'))['q2__avg'] or 0
    avg_q3 = responses.aggregate(Avg('q3'))['q3__avg'] or 0
    avg_q4 = responses.aggregate(Avg('q4'))['q4__avg'] or 0
    avg_q5 = responses.aggregate(Avg('q5'))['q5__avg'] or 0
    avg_q6 = responses.aggregate(Avg('q6'))['q6__avg'] or 0
    avg_q7 = responses.aggregate(Avg('q7'))['q7__avg'] or 0
    avg_q8 = responses.aggregate(Avg('q8'))['q8__avg'] or 0
    avg_q9 = responses.aggregate(Avg('q9'))['q9__avg'] or 0
    avg_q10 = responses.aggregate(Avg('q10'))['q10__avg'] or 0

    context = {
        'total_responses': responses.count(),
        'avg_q1': avg_q1,
        'avg_q2': avg_q2,
        'avg_q3': avg_q3,
        'avg_q4': avg_q4,
        'avg_q5': avg_q5,
        'avg_q6': avg_q6,
        'avg_q7': avg_q7,
        'avg_q8': avg_q8,
        'avg_q9': avg_q9,
        'avg_q10': avg_q10,
        'chart_values_json': json.dumps([
            round(avg_q1, 2),
            round(avg_q2, 2),
            round(avg_q3, 2),
            round(avg_q4, 2),
            round(avg_q5, 2),
            round(avg_q6, 2),
            round(avg_q7, 2),
            round(avg_q8, 2),
            round(avg_q9, 2),
            round(avg_q10, 2),
        ]),  
    }

    return render(request, 'core/dashboard.html', context)