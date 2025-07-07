import tkinter as tk
from ttkbootstrap import Style, ttk
import requests

def get_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data:
                meanings = data[0]['meanings']
                definitions = []
                for meaning in meanings:
                    definitions.append(f"Part of Speech: {meaning['partOfSpeech']}\nDefinition: {meaning['definitions'][0]['definition']}\n")
                return '\n'.join(definitions)
            return 'No definition found.'
        else:
            return f"Error: {response.status_code} - Unable to fetch data"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def search_definition():
    word = entry_word.get().strip()
    if word:
        definition = get_definition(word)
    else:
        definition = 'Please enter a valid word.'
    
    output.configure(state='normal')
    output.delete('1.0', tk.END)
    output.insert(tk.END, definition)
    output.configure(state='disabled')


root = tk.Tk()
style = Style(theme='flatly')
root.title('Dictionary')
root.geometry('500x300')

frame_search = ttk.Frame(root)
frame_search.pack(padx=20, pady=20)

label_word = ttk.Label(frame_search, text='Enter a word:', font=('TkDefaultFont', 15, 'bold'))
label_word.grid(row=0, column=0, padx=5, pady=5)

entry_word = ttk.Entry(frame_search, width=20, font=('TkDefaultFont', 15))
entry_word.grid(row=0, column=1, padx=5, pady=5)

button_search = ttk.Button(frame_search, text='Search', command=search_definition)
button_search.grid(row=1, column=2, padx=5, pady=5)

frame_output = ttk.Frame(root)
frame_output.pack(padx=20, pady=10)

output = tk.Text(frame_output, height=10, state='disabled', font=('TkDefault', 15))
output.pack()

root.mainloop()
