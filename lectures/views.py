from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from .models import Essay
from .forms import EssayForm


def index(request):
    return render(request, 'lectures/index.html')


def loading(request):
    pass


def study(request):
    pass


@require_http_methods(['GET', 'POST'])
def writing(request, video_pk):
    '''
    설명을 적자
    '''
    # 로그인 안된 사용자
    if not request.user.is_authenticated:
        # accounts 앱 만들고 나면 로그인 페이지로 연결하기!
        return render(request, 'lectures/index.html')
    # POST 일 때
    if request.method == 'POST':
        # 이미 작성한 것 수정
        if Essay.objects.filter(video=video_pk, user=request.user.pk).exists():
            essay = Essay.objects.get(video=video_pk, user=request.user.pk)
            essay_form = EssayForm(request.POST, instance=essay)
            if essay_form.is_valid():
                essay_form.save()
            return redirect('lectures:writing', video_pk)
        # 새로 등록
        else:
            essay_form = EssayForm(request.POST)
            if essay_form.is_valid():
                new_essay = essay_form.save(commit=False)
                new_essay.user = request.user
                new_essay.video_id=video_pk
                new_essay.save()
            return redirect('lectures:writing', video_pk)

    # GET 일 때
    if request.method == 'GET':
        if Essay.objects.filter(video=video_pk, user=request.user.pk).exists():
            essay = Essay.objects.get(video=video_pk, user=request.user.pk)
            essay_form = EssayForm(instance=essay)
            context = {
                'essay_form': essay_form,
                'video_pk': video_pk,
            }
            return render(request, 'lectures/writing.html', context)
        else:
            essay_form = EssayForm()
        context = {
            'essay_form': essay_form,
            'video_pk': video_pk,
        }
        return render(request, 'lectures/writing.html', context)


def speaking(request):
    pass


def dashboard(request):
    pass


def save(request):
    pass

