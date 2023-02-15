import time
import random
import tkinter
import my_search
import find_keywords

id = ""  # id of the Spotify
password = ""
driver_path = 'D:\edgedriver\msedgedriver.exe'


def print_entry():
    url = entry.get()
    print(url)
    keys = find_keywords.findKeywords(url)
    key = random.choices(keys.Keywords)
    print(key[0][0])
    search = my_search.searchFromSpotify(random.choices(
        keys.Keywords)[0][0], id, password, driver_path)


top = tkinter.Tk()
top.title('Search From Spotify')
top.geometry('600x200')

text = tkinter.Label(top, text="Input The URL:", font=20, width=30, height=5,)
text.pack()

entry = tkinter.Entry(top, width=80)
entry.pack()

button = tkinter.Button(top, text="Search", font=15,
                        width=10, height=2, command=print_entry)
button.pack()

top.mainloop()
