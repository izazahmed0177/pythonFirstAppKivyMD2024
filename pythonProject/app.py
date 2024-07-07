# from kivy.app import App
from kivymd.app import MDApp
# from kivy.uix.label import Label
from kivy.uix.button import Button
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel


# class MainApp(App):
class MainApp(MDApp):
    def build(self):
        # layout=MDBoxLayout()
        # layout=MDBoxLayout(orientation="vertical")
        # texlavel=MDLabel(text="my app python")
        # textfild=MDTextField()
        #
        # but1=Button(text="Hello, World111")
        # but2=Button(text="Hello, World222")

        # return Label(text="Hello, World")
        # return Button(text="Hello, World")
        # return but1
        # layout.add_widget(texlavel)
        # layout.add_widget(but1)
        # layout.add_widget(textfild)
        # layout.add_widget(but2)
        # return layout
        return

    def myresult(self):
          # print("Success")
         m=self.root.ids.textfild.text
         # self.root.ids.label1.text=m
         self.root.ids.label1.text=f"my name is {m}"
         print(m)


MainApp().run()