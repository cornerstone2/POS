from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder
import mysql.connector
import hashlib


#Builder.load_file('singin/Signin.kv')

class SigninWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def validate_user(self):
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='Livingstone2#',
            database='pos'
        )
        self.mycursor = self.mydb.cursor()
        self.users = self.get_users()

        user = self.ids.username_field
        pwd = self.ids.pwd_field
        info = self.ids.info


  
        uname = user.text
        passw = pwd.text

        user.text = ''
        pwd.text = ''



        if uname == '' or passw == '':
            info.text = '[color=#FF0000]Username and Password required[/color]'
        else:
            user = self.users.find_one({'user_name': uname})

            if user == None:
                info.text = '[color=#0000FF]Logged In successfully!!![/color]'
            else:
                passw = hashlib.sha256(passw.encode()).hexdigest()
                if passw == user['password']:
                    des = user['designation']
                    #info.text = '[color=#0000FF]Logged In successfully!!![/color]'
                    info.text = ''
                    self.parent.parent.parent\
                        .ids.scrn_op.children[0]\
                        .ids.loggedin_user.text = uname
                    if des == 'Administrator':
                        self.parent.parent.current = 'scrn_admin'
                    else:
                        self.parent.parent.current = 'scrn_op'
                else:
                    info.text = '[color=#FF0000]Invalid Username or Password[/color]'


class SigninApp(App):
    def build(self):
        return SigninWindow()


if __name__ == '__main__':
    sa = SigninApp()
    sa.run()