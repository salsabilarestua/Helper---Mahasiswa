from viewmodel.profilViewmodel import get_user_info
from utils.helper import load_user_data, clear

def display_user_info(username):
    try:
        user_info = get_user_info(username)
        if username == "admin":
            print(f"Welcome, {user_info['username']}!")
            print("Admin does not have tasks or schedules.")
        else:
            return user_info
            
    except ValueError as e:
        print(str(e))

def calculate_level(username, scaling_factor=100):
    database = load_user_data()
    for user in database["users"]:
        if user["username"] == username:
            exp = user["exp"]
            return int((exp / scaling_factor) ** 0.5)
    return 0  

def showProfile(username):
   
    while True:
        database = load_user_data()
        user_info = get_user_info(username)
        user = next((u for u in database["users"] if u["username"] == username), None)
        task_done =  sum(
                            1 for user in database["users"]
                            for task in user.get("scheduled_tasks", [])
                            if task.get("status") == "Belum Selesai"
                        )

        if not user:
            print(f"User '{username}' not found.")
            return


        clear()
        print("\n--- User Profile ---")
        print(f"Username: {username}")
        print(f"Kamu mempunyai {task_done} tugas pending.")
        print(f"Level: {calculate_level(username)}")  
        print(user_info["schedule_message"])
        print(user_info["week_hours"])
        print(user_info["tipe"])
        print("\nOptions:")
        print("1. Refresh Profile")
        print("0. Exit")

        
        choice = input("Pilih degan angka: ")
        if choice == '1':
            continue  
        elif choice == '0':
            return
        else:
            print("\n Invalid input! Silakan coba lagi.")