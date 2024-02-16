"""
my first app
"""
import toga

class tictactoe(toga.App):
    def result(self):
        if (self.button00.text == '0' and self.button01.text == '0' and self.button02.text == '0') or (self.button00.text == 'x' and self.button01.text == 'x' and self.button02.text == 'x'):
            return True
        elif (self.button10.text == '0' and self.button11.text == '0' and self.button12.text == '0') or (self.button10.text == 'x' and self.button11.text == 'x' and self.button12.text == 'x'):
            return True
        elif (self.button20.text == '0' and self.button21.text == '0' and self.button22.text == '0') or (self.button20.text == 'x' and self.button21.text == 'x' and self.button22.text == 'x'):
            return True
        elif (self.button00.text == '0' and self.button10.text == '0' and self.button20.text == '0') or (self.button00.text == 'x' and self.button10.text == 'x' and self.button20.text == 'x'):
            return True
        elif (self.button01.text == '0' and self.button11.text == '0' and self.button21.text == '0') or (self.button01.text == 'x' and self.button11.text == 'x' and self.button21.text == 'x'):
            return True
        elif (self.button02.text == '0' and self.button12.text == '0' and self.button22.text == '0') or (self.button02.text == 'x' and self.button12.text == 'x' and self.button22.text == 'x'):
            return True
        elif (self.button00.text == '0' and self.button11.text == '0' and self.button22.text == '0') or (self.button00.text == 'x' and self.button11.text == 'x' and self.button22.text == 'x'):
            return True
        elif (self.button02.text == '0' and self.button11.text == '0' and self.button20.text == '0') or (self.button02.text == 'x' and self.button11.text == 'x' and self.button20.text == 'x'):
            return True
        return False
    
    def reset(self):
        self.user = '0'
        self.button00.text = ' '
        self.button01.text = ' '
        self.button02.text = ' '
        self.button10.text = ' '
        self.button11.text = ' '
        self.button12.text = ' '
        self.button20.text = ' '
        self.button21.text = ' '
        self.button22.text = ' '

    def clickMe(self, button):
        if button.text == '0' or button.text == 'x':
            return
        button.text = self.user
        if self.result():
            self.main_window.info_dialog('You won', f'User {self.user} has won this game!')
            self.reset()

        if self.user == '0':
            self.user = 'x'
        else:
            self.user = '0'
        
        

    def startup(self):
        self.user = '0'
        main_box = toga.Box()
        row0 = toga.Box()
        self.button00 = toga.Button("", id='b00', on_press=self.clickMe)
        self.button01 = toga.Button("", id='b01', on_press=self.clickMe)
        self.button02 = toga.Button("", id='b02', on_press=self.clickMe)
        row0.add(self.button00)
        row0.add(self.button01)
        row0.add(self.button02)
        row1 = toga.Box()
        self.button10 = toga.Button("", id='b10', on_press=self.clickMe)
        self.button11 = toga.Button("", id='b11', on_press=self.clickMe)
        self.button12 = toga.Button("", id='b12', on_press=self.clickMe)
        row1.add(self.button10)
        row1.add(self.button11)
        row1.add(self.button12)
        row2 = toga.Box()
        self.button20 = toga.Button("", id='b20', on_press=self.clickMe)
        self.button21 = toga.Button("", id='b21', on_press=self.clickMe)
        self.button22 = toga.Button("", id='b22', on_press=self.clickMe)
        row2.add(self.button20)
        row2.add(self.button21)
        row2.add(self.button22)
        main_box.add(row0)
        main_box.add(row1)
        main_box.add(row2)
        main_box.style.direction='column'
        row0.style.margin=5
        row1.style.margin=5
        row2.style.margin=5

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return tictactoe()
