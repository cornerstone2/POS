#from kivy.app import App
#from kivy.uix.boxlayout import BoxLayout
import mysql.connector

mydb = mysql.connector.connect(
    host="Localhost",
    user="root",
    passwd="Livingstone2#",
    database="pos"
)



if(mydb):
    print('Successful connection')
else:
    print('Unsuccessful connection')

print(mydb)



