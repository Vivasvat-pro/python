import os
def shutdown():
    choice = input("Are you sure you want to shutdown the system? (yes/no): ")
    if choice.lower() == 'yes':
        print("Shutting down the system...")
        os.system('shutdown /s /t 1')  # For Windows
    else:
        print("Shutdown canceled.")
shutdown()        