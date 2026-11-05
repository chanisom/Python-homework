import os


#1.
def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print("התיקייה נוצרה בהצלחה.")
    else:
        print("התיקיה כבר קיימת")
#2.
def delete_folder(path):
    if not os.path.isdir(path):
        print("הנתיב אינו תיקיה")
        return
    elif os.listdir(path):
        print("אין אפשרות למחוק תיקיה לא ריקה")
    else:
        os.rmdir(path)
        print("נמחקה תיקיה ריקה")
#3.
def create_file(folder, filename):
    if not os.path.isdir(folder):
        print("הניתוב אינו תיקיה!")
        return
    full_path = os.path.join(folder, filename)
    if os.path.exists(full_path):
        print("הקובץ כבר קיים")
        return
    with open(full_path, 'w', encoding='utf-8'):
        pass
    print("הקובץ נוצר")
#4.
def write_to_file(path, text, append):
    if not os.path.isfile(path):
        print("הניתוב אינו קובץ טקסט")
        return
    if append:
        mode = 'a'
    else:
        mode = 'w'

    with open(path, mode, encoding='utf-8') as f:
        f.write(text+"\n")
    print("נכתב טקסט לקובץ")
#5.
def delete_file(path):
    if os.path.isfile(path):
        os.remove(path)
        print("הקובץ נמחק.")
    else:
        print("הקובץ לא נמצא.")

#6.
def all_files_in_the_folder(path):
    if not os.path.isdir(path):
        print("הניתוב אינו תיקיה")
        return
    if not os.listdir(path):
        print("התיקיה ריקה")
        return
    for item in os.listdir(path):
        print(item)

#7.
def show_current_path():
    print("הנתיב הנוכחי:", os.getcwd())


flag = True
while flag:
    print("ליציאה בכל שלב לחץ 0")
    print("ליצירת תיקיה חדשה לחץ 1")
    print("למחיקת תיקיה (רק אם היא ריקה) לחץ 2")
    print("ליצירת קובץ חדש בתיקיה לחץ 3")
    print("לכתיבה או הוספה תוכן לקובץ לחץ 4")
    print("למחיקת קובץ לחץ 5")
    print("לקבלת רשימת כל הקבצים בתיקיה הנוכחית לחץ 6")
    print("להצגת הניתוב הנוכחי המלא לחץ 7")
    num = (input())
    if num == "0":
        flag = False
    elif num == "1":
        path = input("איפה ליצור את התיקיה? מה שם המיקום?")
        create_folder(path)
    elif num == "2":
        path = input("איזה תיקיה למחוק?")
        delete_folder(path)
    elif num == "3":
        folder = input("באיזה תיקייה ליצור? ")
        name = input("מה שם הקובץ? ")
        create_file(folder, name)
    elif num == "4":
        path = input("לאיזה קובץ ברצונך להוסיף טקסט?")
        append = input("להוסיף לסוף הקובץ? (כן/לא)")
        while append != "לא" and append != "כן":
            append = input("להוסיף לסוף הקובץ? (כן/לא)")
        text = input("הכנס את הטקסט כאן:")
        write_to_file(path, text, append=="כן")
    elif num == "5":
        file_path = input("איזה קובץ למחוק?")
        delete_file(file_path)
    elif num == "6":
        path = input("איזה תיקייה להציג?")
        all_files_in_the_folder(path)
    elif num == "7":
        show_current_path()
    else:
        print("בחירה לא תקינה")


