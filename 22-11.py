import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
global a 
a = 0
class MyApp(App):
    
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.win = Label(text="NR :0")
        self.win1 = Label(text="")
        self.window.add_widget(self.win)
        self.window.add_widget(self.win1)
        self.user = TextInput(multiline=False)
        self.window.add_widget(self.user)
        self.button1 = Button(text="+")
        self.button2 = Button(text="-")
        self.button3 = Button(text="*")
        self.button4 = Button(text="/")
        self.button5 = Button(text="%")
        self.button6 = Button(text="cc")
        self.window.add_widget(self.button1)
        self.window.add_widget(self.button2)
        self.window.add_widget(self.button3)
        self.window.add_widget(self.button4)
        self.window.add_widget(self.button5)
        self.window.add_widget(self.button6)
        self.button1.bind(on_press=self.addb)
        self.button2.bind(on_press=self.scb)
        self.button3.bind(on_press=self.inb)
        self.button4.bind(on_press=self.imb)
        self.button5.bind(on_press=self.modb)
        self.button6.bind(on_press=self.cc)
        return self.window
    def addb(self,instance):
        i = False
        global a
        sa = self.user.text
        try:
            float(sa)
            i = True
        except:
            self.win1.text ="Error"
        if(i):
            a = a + float(self.user.text)
            self.win.text = "NR:" + str(a)
            self.user.text =" "
            self.win1.text =" "
    def scb(self,instance):
        i = False
        global a
        sa = self.user.text
        try:
            float(sa)
            i = True
        except:
            self.win1.text ="Error"
        if(i):
            a = a - float(self.user.text)
            self.win.text = "NR:" + str(a)
            self.user.text =" "
            self.win1.text =" "
    def inb(self,instance):
        i = False
        global a
        sa = self.user.text
        try:
            float(sa)
            i = True
        except:
            self.win1.text ="Error"
        if(i):
            a = a * float(self.user.text)
            self.win.text = "NR:" + str(a)
            self.user.text =" "
            self.win1.text =" "
    def imb(self,instance):
        i = False
        global a
        sa = self.user.text
        try:
            float(sa)
            i = True
        except:
            self.win1.text ="Error"
        if(i and a != 0):
            a = a / float(self.user.text)
            self.win.text = "NR:" + str(a)
            self.user.text =" "
            self.win1.text =" "
    def modb(self,instance):
        i = False
        global a
        sa = self.user.text
        try:
            float(sa)
            i = True
        except:
            self.win1.text ="Error"
        if(i):
            a = a % float(self.user.text)
            self.win.text = "NR:" + str(a)
            self.user.text =" "
            self.win1.text =" "
    def cc(self,instance):
        global a
        a = 0
        self.win.text = "NR:" + str(a)
        self.user.text =" "
        self.win1.text =" "

        
if __name__ == '__main__':
    MyApp().run()     






