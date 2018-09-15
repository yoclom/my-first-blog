from django.contrib import admin
from .models import Post

admin.site.register(Post) # 관리자 페이지에서 만든 모델 보기
# Register your models here.
# $ 리눅스 커맨드 라인 시작점 자동표시