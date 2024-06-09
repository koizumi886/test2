from django.urls import path
from . import views # 作成したビュー関数を読み込む
from . import views2

urlpatterns = [
    # path('', views.hello),
    # path('', views.omikuji),
    path('', views.weather),
    path('omikuji', views.t_omikuji),
    path('form', views2.form),
]