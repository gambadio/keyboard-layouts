import winreg
import tkinter as tk
from tkinter import messagebox, ttk
import win32api
import win32con
import ctypes
import ctypes.wintypes
import time

layout_names = {
    "d0010409": "English (United States-International)",
    "00000401": "Arabic (101)",
    "00000402": "Bulgarian (Typewriter)",
    "00000404": "Chinese (Traditional) - Bopomofo",
    "00000405": "Czech",
    "00000406": "Danish",
    "00000407": "German",
    "00000408": "Greek",
    "00000409": "English (United States)",
    "0000040A": "Spanish (Spain)",
    "0000040B": "Finnish",
    "0000040C": "French (Standard)",
    "0000040D": "Hebrew",
    "0000040E": "Hungarian",
    "0000040F": "Icelandic",
    "00000410": "Italian",
    "00000411": "Japanese",
    "00000412": "Korean",
    "00000413": "Dutch",
    "00000414": "Norwegian",
    "00000415": "Polish (Programmers)",
    "00000416": "Portuguese (Brazil ABNT)",
    "00000418": "Romanian (Legacy)",
    "00000419": "Russian",
    "0000041A": "Croatian",
    "0000041B": "Slovak",
    "0000041C": "Albanian",
    "0000041D": "Swedish",
    "0000041E": "Thai Kedmanee",
    "0000041F": "Turkish Q",
    "00000420": "Urdu",
    "00000422": "Ukrainian",
    "00000423": "Belarusian",
    "00000424": "Slovenian",
    "00000425": "Estonian",
    "00000426": "Latvian",
    "00000427": "Lithuanian IBM",
    "00000428": "Tajik",
    "00000429": "Persian",
    "0000042A": "Vietnamese",
    "0000042B": "Armenian Eastern",
    "0000042C": "Azerbaijani Latin",
    "0000042E": "Sorbian Standard",
    "0000042F": "Macedonian (FYROM)",
    "00000432": "Setswana",
    "00000437": "Georgian",
    "00000438": "Faeroese",
    "00000439": "Devanagari - INSCRIPT",
    "0000043A": "Maltese 47-Key",
    "0000043B": "Norwegian with Sami",
    "0000043F": "Kazakh",
    "00000440": "Kyrgyz Cyrillic",
    "00000442": "Turkmen",
    "00000444": "Tatar",
    "00000445": "Bengali",
    "00000446": "Punjabi",
    "00000447": "Gujarati",
    "00000448": "Oriya",
    "00000449": "Tamil",
    "0000044A": "Telugu",
    "0000044B": "Kannada",
    "0000044C": "Malayalam",
    "0000044D": "Assamese - INSCRIPT",
    "0000044E": "Marathi",
    "00000450": "Mongolian Cyrillic",
    "00000451": "Tibetan (PRC)",
    "00000452": "United Kingdom Extended",
    "00000453": "Khmer",
    "00000454": "Lao",
    "0000045A": "Syriac",
    "0000045B": "Sinhala",
    "0000045C": "Cherokee Nation",
    "00000461": "Nepali",
    "00000463": "Pashto (Afghanistan)",
    "00000465": "Divehi Phonetic",
    "00000468": "Hausa",
    "0000046A": "Yoruba",
    "0000046C": "Sesotho sa Leboa",
    "0000046D": "Bashkir",
    "0000046E": "Luxembourgish",
    "0000046F": "Greenlandic",
    "00000470": "Igbo",
    "00000474": "Guarani",
    "00000475": "Hawaiian",
    "00000480": "Uyghur",
    "00000481": "Maori",
    "00000485": "Sakha",
    "00000488": "Wolof",
    "00000492": "Central Kurdish",
    "00000804": "Chinese (Simplified) - US Keyboard",
    "00000807": "Swiss German",
    "00000809": "United Kingdom",
    "0000080A": "Latin American",
    "0000080C": "Belgian French",
    "00000813": "Belgian (Period)",
    "00000816": "Portuguese",
    "0000081A": "Serbian (Latin)",
    "0000082C": "Azerbaijani Cyrillic",
    "0000083B": "Swedish with Sami",
    "00000843": "Uzbek Cyrillic",
    "00000850": "Mongolian (Mongolian Script)",
    "0000085D": "Inuktitut - Latin",
    "00000C0C": "Canadian French (Legacy)",
    "00000C1A": "Serbian (Cyrillic)",
    "00001009": "Canadian French",
    "0000100C": "Swiss French",
    "0000201A": "Bosnian (Cyrillic)",
    "00010402": "Bulgarian (Latin)",
    "00010405": "Czech (QWERTY)",
    "00010407": "German (IBM)",
    "00010408": "Greek (220)",
    "00010409": "United States-Dvorak",
    "0001040A": "Spanish Variation",
    "0001040E": "Hungarian 101-key",
    "00010410": "Italian (142)",
    "00010415": "Polish (214)",
    "00010416": "Portuguese (Brazil ABNT2)",
    "00010418": "Romanian (Standard)",
    "00010419": "Russian (Typewriter)",
    "0001041B": "Slovak (QWERTY)",
    "0001041E": "Thai Pattachote",
    "0001041F": "Turkish F",
    "00010426": "Latvian (QWERTY)",
    "00010427": "Lithuanian",
    "0001042B": "Armenian Western",
    "0001042C": "Azerbaijani Cyrillic",
    "0001042E": "Sorbian Extended",
    "0001042F": "Macedonian (FYROM) - Standard",
    "00010437": "Georgian (QWERTY)",
    "00010439": "Hindi Traditional",
    "0001043A": "Maltese 48-Key",
    "0001043B": "Sami Extended Norway",
    "00010444": "Tatar (Legacy)",
    "00010445": "Bengali - INSCRIPT (Legacy)",
    "00010451": "Tibetan (PRC) - Updated",
    "00010453": "Khmer (NIDA)",
    "0001045A": "Syriac Phonetic",
    "0001045B": "Sinhala - Wij 9",
    "0001045C": "Cherokee Nation Phonetic",
    "0001045D": "Inuktitut - Naqittaut",
    "00010465": "Divehi Typewriter",
    "00010480": "Uyghur (Legacy)",
    "00011009": "Canadian Multilingual Standard",
    "00011809": "Scottish Gaelic",
    "00020401": "Arabic (102)",
    "00020402": "Bulgarian (Phonetic)",
    "00020405": "Czech Programmers",
    "00020408": "Greek (319)",
    "00020409": "United States-International",
    "0002040D": "Hebrew (Standard)",
    "00020418": "Romanian (Programmers)",
    "00020419": "Russian - Mnemonic",
    "0002041E": "Thai Kedmanee (non-ShiftLock)",
    "00020422": "Ukrainian (Enhanced)",
    "00020426": "Latvian (Standard)",
    "00020427": "Lithuanian Standard",
    "0002042E": "Sorbian Standard (Legacy)",
    "00020437": "Georgian (Ergonomic)",
    "00020445": "Bengali - INSCRIPT",
    "00020449": "Tamil 99",
    "0002083B": "Sami Extended Finland-Sweden",
    "00030402": "Bulgarian",
    "00030408": "Greek (220) Latin",
    "00030409": "United States-Dvorak for left hand",
    "0003041E": "Thai Pattachote (non-ShiftLock)",
    "0003042E": "Sorbian Standard (Legacy)",
    "00040402": "Bulgarian (Phonetic Traditional)",
    "00040408": "Greek (319) Latin",
    "00040409": "United States-Dvorak for right hand",
    "00050408": "Greek Latin",
    "00050409": "US English Table for IBM Arabic 238_L",
    "00060408": "Greek Polytonic",
    "00070408": "Greek (220) Latin",
    "00080408": "Greek (319) Latin",
    "00090408": "Greek Latin",
    "000A0408": "Greek (220) Latin",
    "000B0408": "Greek (319) Latin",
    "000C0408": "Greek Latin",
    "000D0408": "Greek (220) Latin",
    "000E0408": "Greek (319) Latin",
    "000F0408": "Greek Latin",
}

def get_layout_name(layout_id):
    return layout_names.get(layout_id, f"Unknown ({layout_id})")

def get_current_layouts():
    layouts = []
    GetKeyboardLayoutList = ctypes.windll.user32.GetKeyboardLayoutList
    GetKeyboardLayoutList.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.wintypes.HKL)]
    GetKeyboardLayoutList.restype = ctypes.c_int
    
    num_layouts = GetKeyboardLayoutList(0, None)
    buf = (ctypes.wintypes.HKL * num_layouts)()
    GetKeyboardLayoutList(num_layouts, buf)
    
    for hkl in buf:
        layout_id = f"{hkl & 0xFFFF:08x}"
        layouts.append(layout_id)
    
    return layouts

def add_layout(layout):
    try:
        layout_code = int(layout, 16)
        result = ctypes.windll.user32.LoadKeyboardLayoutW(layout, 1)
        if result:
            messagebox.showinfo("Success", f"Added layout: {get_layout_name(layout)}")
            time.sleep(1)  # Give Windows some time to process the change
            refresh_layout_list()
        else:
            messagebox.showerror("Error", f"Failed to add layout: {get_layout_name(layout)}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add layout: {e}")

def remove_layout(layout):
    try:
        layout_code = int(layout, 16)
        result = ctypes.windll.user32.UnloadKeyboardLayout(layout_code)
        if result:
            messagebox.showinfo("Success", f"Removed layout: {get_layout_name(layout)}")
            time.sleep(1)  # Give Windows some time to process the change
            refresh_layout_list()
        else:
            messagebox.showerror("Error", f"Failed to remove layout: {get_layout_name(layout)}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to remove layout: {e}")

def refresh_layout_list():
    layout_listbox.delete(0, tk.END)
    for layout in get_current_layouts():
        layout_listbox.insert(tk.END, f"{get_layout_name(layout)} ({layout})")

def add_selected_layout():
    layout = layout_combobox.get().split('(')[-1].strip(')')
    add_layout(layout)

# GUI setup
root = tk.Tk()
root.title("Keyboard Layout Manager")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

layout_listbox = tk.Listbox(frame, width=40)
layout_listbox.pack(side=tk.LEFT)

refresh_layout_list()

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

layout_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=layout_listbox.yview)

input_frame = tk.Frame(root)
input_frame.pack(pady=5)

available_layouts = [f"{v} ({k})" for k, v in layout_names.items()]
layout_combobox = ttk.Combobox(input_frame, values=available_layouts, width=30)
layout_combobox.pack(side=tk.LEFT, padx=5)
layout_combobox.set("Select a layout to add")

add_button = tk.Button(input_frame, text="Add Layout", command=add_selected_layout)
add_button.pack(side=tk.LEFT)

remove_button = tk.Button(root, text="Remove Selected Layout", command=lambda: remove_layout(layout_listbox.get(tk.ACTIVE).split('(')[-1].strip(')')))
remove_button.pack(pady=5)

refresh_button = tk.Button(root, text="Refresh List", command=refresh_layout_list)
refresh_button.pack(pady=5)

root.mainloop()