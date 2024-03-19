from django.urls import path
from mainmenu.views import draw_menu

app_name = 'mainmenu'

urlpatterns = [
    path('<str:menu_name>/', draw_menu, name='draw_menu')
]