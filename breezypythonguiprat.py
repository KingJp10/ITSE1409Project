from breezypythongui import EasyFrame # type: ignore
from tkinter import PhotoImage
from tkinter.font import Font
import math
class ImageDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Image Demo")
        self.setResizable(False);
        imageLabel = self.addLabel(text = "", row = 0, column = 0,
                                   sticky = "NSEW")
        textLabel = self.addLabel(text = "He was in the air for 4 minutes", row = 1, column = 0, sticky = "NSEW")
        self.image = PhotoImage(file = "")
        imageLabel["image"] = self.image
        font = Font(family = "Verdana", size = 20, slant = "italic")
        textLabel["font"] = font
        textLabel["foreground"] = "blue"
class LabelDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, width = 300, height = 200, title = "Label Demo")
        self.addLabel(text = "Wsp", row = 0, column = 0)
        self.setBackground("#00FFFF")
        self.addLabel(text = "(0, 0)", row = 0, column = 0, sticky ="NSEW")
        self.addLabel(text = "(0, 1)", row = 0, column = 1, sticky ="NSEW")
        self.addLabel(text = "(1, 0)", row = 1, column = 0, sticky ="NSEW", columnspan = 2)
        self.addLabel(text = "(1, 0)", row = 1, column = 1, sticky ="NSEW")


class ButtonDemo(EasyFrame):
    def __init__(self): 
        EasyFrame.__init__(self)
        self.label = self.addLabel(text = "Hello world", row = 0, column = 0,  sticky = "NSEW")
        self.clearBtn = self.addButton(text = "Clear",row = 1, column = 0)
        self.restoreBtn = self.addButton(text = "Clear",row = 1, column = 1, state = "disabled")
class TextFieldDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Text field Demo")
        self.addLabel(text = "Input", row = 0, column = 0)
        self.inputField = self.addTextField(text = "", row = 0, column = 1)
        self.addLabel(text = "Output", row = 1, column = 0)
        self.outputField = self.addTextField(text = "", row = 1, column = 1, state = "readonly")
        self.addButton(text = "Convert", row = 2, column = 0, columnspan = 2, command = self.convert)
    def convert(self):
        text = self.inputField.getText()
        result = text.upper()
        self.outputField.setText(result)
class NumberFieldDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Number Field Demo")
        self.addLabel(text = "An integer", row = 0, column = 0)
        self.inputField = self.addIntegerField(value = 0, row = 1, column = 1, width = 10)
        self.addLabel(text = "Square root", row = 1, column = 0)
        self.outputField = self.addFloatField(value = 0.0, row = 1, column = 1, width = 8, precision = 2, state = "readonly")
        self.addButton(text = "Compute", row = 2, column = 0, columnspan = 2, command = self.computeSqrt)
    def computeSqrt(self):
        number = self.inputField.getNumber()
        result = math.sqrt(number)
        self.outputField.setNumber(result)
def main():
    NumberFieldDemo().mainloop()

if __name__ == "__main__":
    main()

