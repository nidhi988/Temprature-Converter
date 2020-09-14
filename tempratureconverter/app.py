"""
tempratureconverter
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class tempratureconverter(toga.App):

    def startup(self):
        #adding two boxes for celsius and fahrenheit
        main_box=toga.Box()
        c_box=toga.Box()
        f_box=toga.Box()
        
        c_input=toga.TextInput(readonly=True)
        f_input=toga.TextInput()
        
        #creating labels
        
        c_label=toga.Label('Celsius',style=Pack(text_align="left"))
        f_label=toga.Label('Fahrenheit',style=Pack(text_align="left")) 
        join_label=toga.Label('is equivalent to',style=Pack(text_align="left"))
        
        def calculate(widget):
            try:
                c_input.value=(float(f_input.value)-32.0)*5.0/9.0
            except:
                pass
            
        button=toga.Button('Calculate',on_press=calculate)
        
        f_box.add(f_input)
        f_box.add(f_label)
        
        c_box.add(join_label)
        c_box.add(c_input)
        c_box.add(c_label)
        
        main_box.add(f_box)
        main_box.add(c_box)
        main_box.add(button)
        
        main_box.style.update(direction=COLUMN,padding_top=10)
        f_box.style.update(direction=ROW,padding_top=5)
        c_box.style.update(direction=ROW,padding_top=5)
        
        c_input.style.update(flex=1)
        f_input.style.update(flex=1,padding_left=160)
        c_label.style.update(width=100,padding_left=10)
        f_label.style.update(width=100,padding_left=10)
        join_label.style.update(width=140,padding_left=10)
        
        button.style.update(padding=15,flex=1)
        
        

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return tempratureconverter()
