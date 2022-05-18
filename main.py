
# A simple Python script for converting unicode Tamil
# characters to TACE16 format suitable for pasting
# Affinity programs. You will have to reformat all the
# text in Affinity after pasting and toggling to unicode.

from tkinter import *
import sys
import clipboard
import tkinter.font as font

#if sys.version_info.major == 3:
#    import tkinter as tk, tkinter.font as tk_font
#else:
#    import Tkinter as tk, tkFont as tk_font

inputValue4 = ""  # global return value

# open and read the file after the appending:
f = open("tafe", "r")
var = f.read()
var = var.split()
# print some test values
#print(var[110],var[111])
#print(len(var))
f.close()

# open Tk window
root=Tk()
root.title('A simple Unicode to TACE16 format converter for Affinity programs')

# create Font object
myFont = font.Font(family='Helvetica')

# copy some sample text into clipboard for testing
#clipboard.copy("தமிழ் மொழி Mathiazhagan \n மதியழகன்")  # now the clipboard content will be string "abc"
#text = clipboard.paste()  # text will have the content of clipboard

# print available fonts
# print(tk_font.families())
# print(tk_font.names())

def clear_all():
    inputValue4 = ""
    clipboard.copy(inputValue4)  # now the clipboard content will be string "abc"
    text = clipboard.paste()  # text will have the content of clipboard
    textBox.delete("1.0", END) # clear text boxes
    textBox2.delete("1.0", END)
    print('screen and clipboard cleared')

def copy_clipboard():
    clipboard.copy(inputValue4)  # now the clipboard content will be string "abc"
    text = clipboard.paste()  # text will have the content of clipboard
    print('copy to clipboard done')

def retrieve_input():

    global inputValue4

    inputValue = textBox.get("1.0","end-1c")
    inputValue2 = inputValue.encode("unicode-escape", "replace")
    inputValue3 = str(inputValue2).replace("\\u", "")
    inputValue3a = str(inputValue3).replace("\\n", "u+20")
    inputValue3b = str(inputValue3a).replace("\\r", "u+20")
    inputValue3c = str(inputValue3b).replace("\\", "")
    inputValue3c = str(inputValue3c).replace("\\u+", "u+")
    inputValue3d = inputValue3c.rstrip(inputValue3c[-1])  # strip end
    inputValue4 = "//\r\nU+0020U+0020U+0020" + inputValue3d[2:] + "U+0020U+0020U+0020\r\n\r\n//"  # strip beginning

#    print(inputValue)
#    print(inputValue2)
#    print(inputValue3)
    print(inputValue4)

    for i in range(int(len(var)/2)):
        #print(i)
        inputValue4 = str(inputValue4).replace(str(var[2*i]).lower(), 'u+'+str(var[2*i+1]).lower())

    #print(ascii(inputValue))
    #print(inputValue4)
    print('conversion done')
    textBox2.insert(INSERT, inputValue4)

# display first text box using std font
textBox=Text(root, height=10, width=100, font = myFont)
textBox.pack()

# display second text box using target font
textBox2 = Text(root, height=10, width=100, font= myFont)
textBox2.pack(pady=20)

# button clicks section
buttonCommit = Button(root, height=1, width=10, text="Convert", font=myFont,
                    command=lambda: retrieve_input())
# command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit.pack()

buttonCommit2 = Button(root, height=1, width=10, text="Copy", font=myFont,
                    command=lambda: copy_clipboard())
# command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit2.pack()

buttonCommit3 = Button(root, height=1, width=10, text="Clear", font=myFont,
                    command=lambda: clear_all())
# command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit3.pack()

mainloop()