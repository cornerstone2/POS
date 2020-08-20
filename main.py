from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import multiprocessing
#from Admin.admin import AdminWindow
from LOGIN.signin import SigninWindow
from API.operator import OperatorWindow





class MainWindow(BoxLayout):

    #admin_widget = AdminWindow()
    signin_widget = SigninWindow()
    operator_widget = OperatorWindow()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ids.scrn_si.add_widget(self.signin_widget)
        #self.ids.scrn_admin.add_widget(self.admin_widget)
        #self.ids.scrn_op.add_widget(self.operator_widget)





class MainApp(App):
    def build(self):
        return MainWindow


MainApp().run()
