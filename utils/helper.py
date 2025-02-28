import os
import json
import time
import re
from datetime import datetime
from plyer import notification

DATA_FILE = "user_data.json"

def clear():
    # Cek OS dan clear terminal
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # MacOS/Linux
        os.system('clear')

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="Helper Mahasiswa", 
        timeout=5  # Durasi notifikasi
    )

def load_user_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_user_data(user_data):
    try:
        with open(DATA_FILE, 'w') as file:
            json.dump(user_data, file, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

def find_user(username):
    user_data = load_user_data()
    for user in user_data["users"]:
        if user["username"] == username:
            return user
    return None

def validate_nospace(prompt):
    while True:
        string = input(prompt).strip()
        if not string:
            print("Input tidak boleh kosong! Coba lagi.")
            time.sleep(1)
            clear()
        elif not re.match("^[a-zA-Z0-9_]+$", string):
            print("Input tidak valid! Hanya huruf, angka, dan underscore (_) yang diizinkan.")
            time.sleep(1)
            clear()
        else:
            return string

def validate_alpha(prompt):
    while True:
        string = input(prompt).strip()
        if not string:
            print("Input tidak boleh kosong! Coba lagi.")
            time.sleep(1)
            clear()
        elif not re.match("^[a-zA-Z _]+$", string):       
            print("Input tidak valid! Silakan coba lagi.")
            time.sleep(1)
            clear()
        else:
            return string

def validate_alnum(prompt):
    while True:
        string = input(prompt).strip()
        if not string:
            print("Input tidak boleh kosong! Coba lagi.")
            time.sleep(1)
            clear()
        elif not re.match("^[a-zA-Z0-9 _]+$", string):       
            print("Input tidak valid! Silakan coba lagi.")
            time.sleep(1)
            clear()
        else:
            return string

def get_valid_date(prompt):
        """
        Prompt the user for a valid date in the format YYYY-MM-DD.
        """
        while True:
            date_input = input(prompt)
            try:
                date = datetime.strptime(date_input, "%Y-%m-%d")
                return date.date()
            except ValueError:
                print("Format tanggal tidak valid! Harap masukkan dalam format YYYY-MM-DD.\n")

def validate_time(time):
    try:
        time_obj = datetime.strptime(time, "%H:%M")
        return time_obj
    except ValueError:
        return None