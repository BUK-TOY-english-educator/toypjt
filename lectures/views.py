import requests
from django.conf import settings
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from youtube_transcript_api import YouTubeTranscriptApi

def index(request):
    return render(request, 'lectures/index.html')


def loading(request):
    return render(request, 'lectures/loading.html')


def study(request):
    pass


def writing(request):
    pass


def speaking(request):
    pass


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