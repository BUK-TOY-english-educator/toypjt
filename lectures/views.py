import requests, json
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from .models import Essay
from .forms import EssayForm
from youtube_transcript_api import YouTubeTranscriptApi

def index(request):
    return render(request, 'lectures/index.html')


def loading(request):
    return render(request, 'lectures/loading.html')


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


def speaking(request, video_pk):
    return render(request, 'lectures/speaking.html')


def dashboard(request):
    pass


def save(request):
    pass

# 유튜브 영상을 가져오는 뷰 함수
def youtube(request):
    # url = 'https://www.youtube.com/watch?v=r9lDDetKMi4'
    # url = 'https://www.googleapis.com/youtube/v3/search'
    # params = {
    #     'key': settings.YOUTUBE_API_KEY,        
    #     'part': 'content',
    #     'id': 'r9lDDetKMi4',
    #     # 'type': 'video',
    #     # 'maxResults': '1',
    #     # 'q': 'ted',
    # }
    # #print(params['key'])
    # response = requests.get(url, params)
    # response_dict = response.json()
    # print(response_dict)

    # video_id = response_dict['items'][1]['id']['videoId']
    video_id = 'r9lDDetKMi4'

    # 자막 가져오기    
    caption_lst = YouTubeTranscriptApi.get_transcript(video_id)
    print(caption_lst[0])
    # 자막 text_lst, 시간 리스트 만들기
    text_lst = [' ',' ',' ',' ']
    time_lst = [-3, -2, -1, -0.5]
    for caption in caption_lst:
        text_lst.append(caption['text'])
        time_lst.append(caption['start'])    
    # text_lst = simplejson.dumps(text_lst)
    # time_lst = simplejson.dumps(time_lst)
    # print(text_lst)
    # print(time_lst)
    context = {
        # 'youtube_items': response_dict['items'],
        'video_id': video_id,
        'text_lst': text_lst,
        'time_lst': time_lst,
    }
    

    # print(response_dict['items'][0])
    return render(request, 'lectures/youtube.html', context)

# 사전 api view
# https://developer.oxforddictionaries.com/
def find_word(request, word):   
    # ToDo: replace with your own app_id and app_key
    # api parameter
    app_id = '81e0600d'
    app_key = 'd702b292b062920dc24252a551252a5b'
    language = 'en-gb'
    word_id = word  # 검색할 단어
    
    print(word)
    # url, requests
    url = 'https://od-api.oxforddictionaries.com/api/v2/entries/'  + language + '/'  + word_id.lower()
    print(url)
    r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})
    print("code {}\n".format(r.status_code))
    result = r.json()
    senses = result["results"][0]["lexicalEntries"][0]['entries'][0]['senses'][0]
    # print(result)
    #print(senses)   
    # 정의
    word_definition = senses['definitions'][0]
    # 예문
    try:
        word_example = senses['examples'][0]['text']
    except:
        word_example = '예문이 없어요..'    
    # 문장 성분
    lexical_category = result["results"][0]["lexicalEntries"][0]["lexicalCategory"]["text"]

    #print(word_definition, word_example, lexical_category)

    data = {
        # 'youtube_items': response_dict['items'],
        'word_definition': word_definition,
        'word_example': word_example,
        'lexical_category': lexical_category,
    }

    return JsonResponse(data)    