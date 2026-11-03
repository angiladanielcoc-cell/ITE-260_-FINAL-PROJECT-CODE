import sys
import random
Admin_Username = "Admin123"
Admin_Password = "Admin123"

subject=[]
teachers_list = []  
custom_subjects = [] 
sections_list = []
student_records = {} 



def get_closest_subject(user_input):
    for valid in custom_subjects:
        if len(set(user_input) & set(valid)) >= len(valid) - 1 and abs(len(user_input) - len(valid)) <= 2:
            return valid
    return user_input



def get_valid_grade(subject_name):
    while True:
        try:
            grade_input = input(f"Enter grade for {subject_name.capitalize()} (0-100): ").strip()
            grade = float(grade_input)
            if 0 <= grade <= 100:
                return grade
            else:
                print("Invalid grade. Please enter a number from 0 to 100.")
        except ValueError:
            print("Invalid input. Please enter a numerical format.")


while True: 
    print("\n ========= MAIN MENU ==========")
    print("[1] Admin Login")
    print("[2] Teacher Login")
    print("[3] Student Login")
    print("[4] Exit")

    choice = input("\n Select an option (1-4): ").strip()

    if choice == "1":
        print("\n ======== ADMINISTRATIVE LOGIN ========")
        Username_Input = input("Enter Admin Username: ")
        Password_Input = input("Enter Password: ")

        if Username_Input != Admin_Username or Password_Input != Admin_Password:
            print("\n ACCESS DENIED. GO HOME.")
            continue  

        print("\n [+] Login Successful! Access Granted.")
        
        while True:
            print("\n ===== ADMIN OPTIONS =====")
            print("[1] Add new teacher account")
            print("[2] View registered teachers list")
            print("[3] Exit to Main Menu")

            admin_choice = input("\nSelect a management option (1-3): ").strip()

            if admin_choice == "1":
                print("\n ===== REGISTER NEW TEACHER ACCOUNT =====")
                teacher_name = input("Enter Teacher's Full Name: ").strip()
                
                exists = any(t['name'].lower() == teacher_name.lower() for t in teachers_list)
                
                if teacher_name == "":
                    print("Teacher name cannot be empty.")
                elif exists:
                    print(f"'{teacher_name}' is already registered.")
                else:
                    t_user = input("Create Teacher Username: ").strip()
                    user_exists = any(t['username'].lower() == t_user.lower() for t in teachers_list)
                    
                    if t_user == "" or user_exists:
                        print("Invalid or already taken username.")
                        continue
                        
                    t_pass = input("Create Teacher Password: ").strip()
                    if t_pass == "":
                        print("Password cannot be empty.")
                        continue
                    
                    teachers_list.append({
                        "name": teacher_name,
                        "username": t_user,
                        "password": t_pass
                    })
                    print(f"[+] Success: Teacher '{teacher_name}' registered successfully with username '{t_user}'.")

            elif admin_choice == "2":
                print("\n ======= REGISTERED TEACHERS DATABASE =======")
                if not teachers_list:
                    print("\n[No teachers have been registered by the admin yet.]")
                else:
                    print(f"Total Registered Accounts: {len(teachers_list)}")
                    print("+----------------------+----------------------+")
                    print(f"| {'Teacher Name':<20} | {'Registered Username':<20} |")
                    print("+----------------------+----------------------+")
                    for teacher in teachers_list:
                        print(f"| {teacher['name']:<20} | {teacher['username']:<20} |")
                    print("+----------------------+----------------------+")
                print("\nRETURNING TO ADMIN OPTIONS....")
                print("+-----------------------------------------------------+")
                continue

            elif admin_choice == "3":
                print("\nEXITING TO MAIN MENU....")
                break 
                
            else:
                print("\nInvalid choice. Please pick a number from 1 to 3.")

    
    elif choice == "2":
        print("\n ======== TEACHER LOGIN ========")
        t_user_input = input("Enter Teacher Username: ").strip()
        t_pass_input = input("Enter Teacher Password: ").strip()
        
        authenticated_teacher = None
        for teacher in teachers_list:
            if teacher['username'] == t_user_input and teacher['password'] == t_pass_input:
                authenticated_teacher = teacher
                break
                
        if authenticated_teacher is None:
            print("\n ACCESS DENIED. YOU ARE NOT REGISTERED BY THE ADMIN.")
            continue
            
        print(f"\n Login Successful! Greetings! Teacher {authenticated_teacher['name']}.")
        
        while True:
            print(f"\n ===== TEACHER MENU ({authenticated_teacher['name']}) =====")
            print("[1] Add New Subject to Database")
            print("[2] Add New Classroom Section")
            print("[3] Register / Add Student to Database")
            print("[4] Enter Student Grades")
            print("[5] View Database Summary")
            print("[6] Log out to Main Menu")
            
            teacher_choice = input("\nSelect an option (1-6): ").strip()
            
            if teacher_choice == "1":
                new_sub = input("\nEnter name of new subject: ").strip().lower()
                if new_sub == "":
                    print("Subject name cannot be empty.")
                elif new_sub in custom_subjects:
                    print(f"'{new_sub.capitalize()}' is already in the system.")
                else:
                    custom_subjects.append(new_sub)
                    print(f"[+] Success: '{new_sub.capitalize()}' stored in subjects database.")

            elif teacher_choice == "2":
                new_section = input("\nEnter New Classroom Section Name (e.g, Level ): ").strip()
                if new_section == "":
                    print("Section name cannot be empty.")
                elif new_section in sections_list:
                    print(f"Section '{new_section}' already exists.")
                else:
                    sections_list.append(new_section)
                    print(f"[+] Success: Section '{new_section}' created.")

            elif teacher_choice == "3":
                print("\n ======= REGISTER STUDENT PROFILE =======")
                if not sections_list:
                    print("Error: You must create at least one Classroom Section (Option 2) first.")
                    input("\nPress Enter to return.")
                    continue
                    
                student_name = input("Enter Student's Full Name: ").strip()
                if student_name == "":
                    print("Student name cannot be empty.")
                    input("\nPress Enter to return.")
                    continue
                    
                if student_name in student_records:
                    print(f"'{student_name}' is already registered in the student database.")
                    input("\nPress Enter to return.")
                    continue
                
                print(f"Available Sections: {sections_list}")
                assigned_section = input("Assign to Section: ").strip()
                
                if assigned_section not in sections_list:
                    print("Section choice unrecognized. Student registration cancelled.")
                else:
                    #vvv This generates random password for the student vvv
                    generated_password = str(random.randint(1000, 9999))
                    
                    student_records[student_name] = {
                        "section": assigned_section,
                        "password": generated_password,
                        "grades": {}
                    }
                    print(f"[+] Success: Student '{student_name}' registered under '{assigned_section}'.")
                    print(f"[!] IMPORTANT: Student Password is: {generated_password}")
                    
                input("\nPress Enter to return to Menu.")

        
            elif teacher_choice == "4":
                print("\n ------ WELCOME TO GRADING SYSTEM -----")
                
                if not custom_subjects:
                    print("Error: You must add subjects in Option 1 before entering grades.")
                    input("\nPress Enter to return to Menu.")
                    continue
                
                if not student_records:
                    print("Error: No students are currently registered in the database. Use Option 3 first.")
                    input("\nPress Enter to return to Menu.")
                    continue
                    
                student_name = input("Enter student name to grade: ").strip()
                if student_name not in student_records:
                    print("Student profile not found in database. Please register the student first.")
                    input("\nPress Enter to return to Menu.")
                    continue

                print(f"\nYou must enter grades for all {len(custom_subjects)} subjects.")
                grades = []
                
                while True:
                    if len(student_records[student_name]["grades"]) == len(custom_subjects):
                        print("\n[!] All available subjects have now been graded for this student.")
                        break

                    subject = input ("Enter subject: ").strip().lower()
                    if subject in custom_subjects:
                        
                        if subject in student_records[student_name]["grades"]:
                            print(f"You already entered a grade for {subject.capitalize()}.")

                        while True:
                            try:
                                grade = float(input(f"Enter grade {subject.capitalize()} (0-100): "))
                                if 0 <= grade <= 100:
                                    print("\n+----------------------+----------------------+--------+")
                                    print(f"| {'Student Name':<20} | {'Subject':<20} | {'Grade':<6} |")
                                    print("+----------------------+----------------------+--------+")
                                    print(f"| {student_name:<20} | {subject.capitalize():<20} | {grade:<6} |")
                                    print("+----------------------+----------------------+--------+")
                                    
                                    (student_records[student_name]["grades"][subject]) = grade
                                    grades.append(grade)
                                    break
                                
                                else:
                                    print("Invalid grade. Please enter a number from 0 to 100.")
                            except ValueError:
                                print("Invalid input. Please enter a numerical format.")
                        
                            break 
                        
                        if len(student_records[student_name]) == len(custom_subjects):
                            break
                    else:
                        print(f"Subject not recognized. Current list: {[s.capitalize() for s in custom_subjects]}")

                if grades:
                    average_grade = sum(grades) / len(grades)
                    print("\n ======= Final Summary ======")
                    print("\n--------------------------------")
                    print(f"| {'Student Name':<20} |", student_name)
                    print(f"| {'Average grade':<10} |", round(average_grade, 2))
                
                input("\nPress Enter to return to (Options).")

            elif teacher_choice == "5":

                print("\n ======= CENTRAL STUDENT DATABASE ROSTER =======")
                if not student_records:
                    print("Error: The school database is currently empty.")
                    input("\nPress Enter to return to Menu.")
                    continue
                    
                print("\n+---------------------+----------------------+---------------------------------------+")
                print(f"| {'Student Name':<20} | {'Class Section':<20} | {'Passcode' :<4} | {'Final Average':<14} |")
                print("+-----------------------+----------------------+----------------------------------------+")
                
                for name, info in student_records.items():
                    if info["grades"]:
                        avg = sum(info["grades"].values()) / len(info["grades"])
                        avg_display = str(round(avg, 2))
                    else:
                        avg_display = "No Grades"
                        
                    print(f"| {name:<20} | {info['section']:<20} | {info['password'] :<4} | {avg_display:<14} |")
                    
                print("+----------------------+----------------------+----------------+")
                input("\nPress Enter to return to Menu.")
            elif teacher_choice == "6":
                print("\n Logging out...")
                break

    elif choice == "3":
        print("\n ======= STUDENT MENU =======")
        
        if not student_records:
            print("Error: No student records exist in the system database yet.")
            input("\nPress Enter to return.")
            continue
            
        student_name = input("Enter your Registered Full Name: ").strip()
        
        if student_name not in student_records:
            print("Access Denied: Student profile not found.")
            input("\nPress Enter to return.")
            continue
            
        input_password = input("Enter your 4-Digit Student Passcode: ").strip()
        
        if input_password != student_records[student_name]["password"]:
            print("Access Denied: Incorrect passcode configuration.")
            input("\nPress Enter to return.")
            continue
            
        profile = student_records[student_name]
        print("\n========================================================")
        print(f" STUDENT REPORT CARD: {student_name.upper()}")
        print(f" Classroom Section:  {profile['section']}")
        print("========================================================")
        
        if not profile["grades"]:
            print(" [!] No grades have been recorded for your profile yet.")
        else:
            print(f"| {'Subject':<25} | {'Grade':<10} |")
            print("--------------------------------------------------------")

            for subject, grade in profile["grades"].items():
                print(f"| {subject.capitalize():<25} | {grade:<10} |")
            print("--------------------------------------------------------")
            

            total_avg = sum(profile["grades"].values()) / len(profile["grades"])
            print(f"| {'OVERALL FINAL AVERAGE':<25} | {round(total_avg, 2):<10} |")


            #This project felt like forever to finish yet im so fasinated on how these work.-