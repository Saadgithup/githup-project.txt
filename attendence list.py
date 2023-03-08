# Initialize the attendance list
attendance = {}

# Function to mark attendance for a student
def mark_attendance(name):
    if name not in attendance:
        attendance[name] = True
        print(f"{name} is marked present.")
    else:
        print(f"{name} is already marked present.")

# Function to display attendance for all students
def display_attendance():
    print("Attendance:")
    for name, present in attendance.items():
        if present:
            print(f"{name}: Present")
        else:
            print(f"{name}: Absent")

# Main program loop
while True:
    print("Enter 1 to mark attendance")
    print("Enter 2 to display attendance")
    print("Enter 3 to exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        mark_attendance(name)
    elif choice == 2:
        display_attendance()
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 3.")