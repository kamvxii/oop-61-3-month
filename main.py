import flet as ft

def main(page: ft.Page):
    page.title='ve first app'
    page.theme_mode=ft.ThemeMode.LIGHT
    text_hello= ft.Text(value='Hello world')
    greeting_history=[]
    history_text=ft.Text('история приветсвий:')




    def text_name():
        name=name_imput.value.strip()
        if name:
            text_hello.color=None
            text_hello.value=f'Hello{name}'
            greeting_history.append(name)
            print(greeting_history)
            history_text.value=f'История приветсвий :'+''.join(greeting_history)
        else:

            text_hello.value='Введите имя!'
            text_hello.color= ft.Colors.RED    
             



 
    elevated_button=ft.ElevatedButton('send', on_click=text_name, icon=ft.Icons.SEARCH,color=ft.Colors.BLUE, icon_color=ft.Colors.RED)
    name_imput=ft.TextField(label='Введите чо нибудь', on_submit=text_name)
    def thememode(_):
        if page.theme_mode==ft.ThemeMode.DARK:
            page.theme_mode==ft.ThemeMode.LIGHT
        else:
            page.theme_mode==ft.ThemeMode.DARK
    thememode_button=ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=thememode) 
   
    
    #дбавление на сайт
    page.add(text_hello,elevated_button,name_imput,thememode_button,greeting_history)
    

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
