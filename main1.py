import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = 'Мое первое приложение!'
    page.theme_mode = ft.ThemeMode.LIGHT

    text_hello = ft.Text(value='Hello world')

    greeting_history = []
    history_text = ft.Text('История приветствий:')

    def text_name(_):
        name = name_input.value.strip()
        if name:
            now=datetime.now().strftime('%Y:%m:%d-%h:%m:%s')
            text_hello.color = None
            text_hello.value = f'Hello {name}'
            name_input.value = ""

            greeting_history.append(name)
            history_text.value = 'История приветствий:\n' + '\n'.join(greeting_history)
        else:
            text_hello.value = "Введите имя!"
            text_hello.color = ft.Colors.RED
        page.update()

    elevated_button = ft.ElevatedButton('send',on_click=text_name,icon=ft.Icons.SEARCH)

    name_input = ft.TextField(label='Введите что-нибудь',on_submit=text_name,expand=True)

    def thememode(_):
        page.theme_mode = (ft.ThemeMode.LIGHT
            if page.theme_mode == ft.ThemeMode.DARK
            else ft.ThemeMode.DARK)
        page.update()

    thememode_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=thememode)

    def clear_history(_):
        greeting_history.clear()
        history_text.value = 'История приветствий:'
        page.update()

    clear_button = ft.IconButton(icon=ft.Icons.DELETE,
        on_click=clear_history)
    
    def delete_last():
        if greeting_history:
            greeting_history.pop()
            history_text.value = 'История приветствий:\n' + '\n'.join(greeting_history)
        else:
            history_text.value='здесь пусто '    
    page.update()        
    delete_last_button=ft.ElevatedButton('удалить последнее',icon=ft.Icons.DELETE,on_click=delete_last)

    def sort_history():
        if greeting_history:
            greeting_history.sort(key=str.lower)
            history_text.value = 'История приветствий:\n' + '\n'.join(greeting_history)
        else:
            history_text.value='здесь ничего нет'    
    page.update()        
    sort_history_button=ft.IconButton(icon=ft.Icons.SORT_BY_ALPHA, on_click=sort_history)

    

    main_object = ft.Row([ name_input,elevated_button,thememode_button,clear_button,delete_last_button,sort_history_button ])

    page.add(text_hello, main_object, history_text)

ft.app(target=main,view=ft.AppView.WEB_BROWSER)