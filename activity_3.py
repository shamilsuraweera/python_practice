# student_manager.py

# Step 1: Initialize an empty list to store student records
students = []

# Step 2: Define a function to display a menu
def display_menu():
    print("\n=== Student Record Manager ===")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search by Name")
    print("4. Save to File")
    print("5. Exit")

# Step 3: Define a function to add a student
def add_student():
    name = input("Enter student's name: ")
    age = input("Enter student's age: ")
    grade = input("Enter student's grade: ")
    
    student = {
        "name": name,
        "age": age,
        "grade": grade
    }
    students.append(student)
    print("✅ Student added!")

# Step 4: Define a function to view all students
def view_students():
    if not students:
        print("⚠️ No students added yet.")
        return
    
    for index, student in enumerate(students, start=1):
        print(f"{index}. {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

# Step 5: Define a function to search by name
def search_student():
    search_name = input("Enter name to search: ").lower()
    found = False
    for student in students:
        if search_name in student["name"].lower():
            print(f"🎯 Found: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
            found = True
    if not found:
        print("❌ No match found.")

# Step 6: Define a function to save to a file
def save_to_file():
    with open("students.txt", "w") as f:
        for student in students:
            f.write(f"{student['name']},{student['age']},{student['grade']}\n")
    print("💾 Saved to 'students.txt'")

# Step 7: Main loop
while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        save_to_file()
    elif choice == "5":
        print("👋 Exiting... Goodbye!")
        break
    else:
        print("❗ Invalid choice. Please select 1-5.")
