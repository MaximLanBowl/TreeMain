from django import template
from mainmenu.models import MenuItem

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    menu = MenuItem.objects.filter(title=menu_name).first()

    if menu:
        return render_menu(menu)

    return ''


def render_menu(menu):
    menu_html = f'<ul><li><a href="{menu.url}">{menu.title}</a></li>'

    if menu.children.exists():
        menu_html += '<ul>'
        for child in menu.children.all():
            menu_html += f'<li>{render_menu(child)}</li>'
        menu_html += '</ul>'

    menu_html += '</ul>'

    return menu_html
