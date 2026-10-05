students = {
    "STU001": {
        "name": "Alice",
        "grade": "A+",
        "physics": 80,
        "chemistry": 75,
        "maths": 90,
        "roll": 29,
        "section": "A",
        "class": "KG",
        "contact": "015643265484",
        "blood_group": "A+"
    }
}

def main():
    print("------Main Menu------")
    print("1. Show All Students")
    print("2. Add New Students")
    print("3. Remove Students")
    print("4. Search Students")
    print("5. Edit Students")
    print("6. Show Top Scorer")
    print("7. Show Students By Grade")
    print("8. Exit")

def all_students():
    print("ID        Name    Class Sec  Roll Phy Chem Maths Avg Grade     Contact     Blood")
    print("----------------------------------------------------------------------------------")
    for student_id, data in students.items():
        avg = (data['physics'] + data['chemistry'] + data['maths']) / 3
        avg = int(avg)
        print(student_id,  " "  ,data['name'], " " ,data['class'], "   " ,data['section'], " " ,data['roll'], " " ,data['physics'], " ", data['chemistry'], " " , data['maths'], " " ,  avg, " " , data['grade'], "   ",  data['contact'], "  " , data['blood_group'])

def calculate_grade(physics, chemistry, maths):
    avg = (physics + chemistry + maths) / 3
    if avg >= 80: return "A+"
    elif avg >= 70: return "A"
    elif avg >= 60: return "B"
    elif avg >= 50: return "C"
    elif avg >= 40: return "D"
    else: return "F"

def generate_id():
    if len(students) == 0:
        return "STU001"
    all_keys = list(students.keys())
    last_id = all_keys[-1]
    number_text = last_id[3:]
    next_number = int(number_text) + 1 
    if next_number < 10:
        return "STU00" + str(next_number)
    elif next_number < 100:
        return "STU0" + str(next_number)
    else:
        return "STU" + str(next_number)   


def add_students():
    print("--- Add a New Student ---")
    
    print("Enter The Student Name: ")
    name = input() 
    if name == "":
        print("Name Cannot Be Empty")
        print("Enter The Student Name")
        name = input()
        
    print("Enter The Physics Mark:")
    physics = int(input())
    if physics < 0 or physics > 100:
        print("Invalid Mark! Try Again.")
        print("Enter The Physics Mark: ")
        physics = int(input())
        
    print("Enter Chemistry marks (0-100): ")    
    chemistry = int(input())
    if chemistry < 0 or chemistry > 100:
        print("Invalid Marks! Try Again.")
        print("Enter Chemistry marks (0-100): ")
        chemistry = int(input())
        
    print("Enter Maths marks (0-100): ")    
    maths = int(input())
    if maths < 0 or maths > 100:
        print("Invalid Marks! Try Again.")
        print("Enter Maths marks (0-100): ")
        maths = int(input())
        
    print("Enter The Class: ")
    student_class = input()
    if student_class == "":
        print("Class Cannot Be empty!")
        print("Enter The Class: ")
        student_class = input()
        
    print("Enter Section: ")    
    section = input()
    if section == "":
        print("Section Cannot Be Empty!")
        print("Enter Section: ")
        section = input()
        
    print("Enter Roll Number: ")    
    roll = int(input())
    
    for student_id, data in students.items():
        if data['roll'] == roll and data['class'] == student_class and data['section'] == section:
            print("Roll Already Exists In This Class And Section!")
            return

    contact = input("Enter Contact: ")
    if contact == "":
        print("Contact Cannot Be Empty!")
        print("Enter Contact: ")
        contact = input()
        
    print("Enter Blood Group: ")        
    blood = input()
    if blood == "":
        print("Blood Group cannot be empty!")
        print("Enter Blood Group: ")
        blood = input()

    new_id = generate_id()
    new_grade = calculate_grade(physics, chemistry, maths)

    students[new_id] = {
        "name": name,
        "grade": new_grade,
        "physics": physics,
        "chemistry": chemistry,
        "maths": maths,
        "roll": roll,
        "section": section,
        "class": student_class,
        "contact": contact,
        "blood_group": blood
    }

    print("Student Added Successfully! ID: ", new_id)
def remove_students():
    print("--- Remove a Student ---")
    print("Enter The Name To Search:")
    search_name = input()
    
    count = 0
    for student_id, data in students.items():
        if search_name in data['name']:
            print("ID:", student_id, " | Name:", data['name'])
            count = count + 1
            
    if count == 0:
        print("Student not found!")
    else:
        print("Enter The Student ID You Want To Remove:")
        student_id_to_remove = input()
        
        if student_id_to_remove in students:
            print("Student found:", students[student_id_to_remove]['name'])
            print("Are You Sure? (y/n)")
            confirm = input()
            
            if confirm == "y":
                del students[student_id_to_remove]
                print("Student removed successfully!")
            else:
                print("Removal cancelled.")
        else:
            print("Invalid Student ID!")
def search_student():
    print("1. Search By Name")
    print("2. Search By Roll")
    choice = int(input())
    
    if choice == 1:
        print("Please Provide The Name Of The Student")
        search_name = input()
        for student_id, data in students.items():
            if search_name in data['name']:
                avg = int((data['physics'] + data['chemistry'] + data['maths']) / 3)
                print(student_id, '-', data['name'], '-', data['class'], '-', data['section'], '-', data['roll'], '-', data['physics'], '-', data['chemistry'], '-', data['maths'], '-', avg, '-', data['grade'], '-', data['contact'],  '-', data['blood_group'])

    elif choice == 2:
        print("Please Provide The Roll Of The Student")
        search_roll = int(input())
        for student_id, data in students.items():
            if data['roll'] == search_roll:
                avg = int((data['physics'] + data['chemistry'] + data['maths']) / 3)
                print(student_id, '-', data['name'], '-', data['class'], '-', data['section'], '-', data['roll'], '-', data['physics'], '-', data['chemistry'], '-', data['maths'], '-', avg, '-', data['grade'], '-', data['contact'],  '-', data['blood_group'])

def edit_student():
    print("Enter Student ID to edit:")
    all_students()
    student_id = input()
    if student_id not in students:
        print("Student not found!")
        return

    print("--- Edit The Following Stuffs ---")
    print("1. Name")
    print("2. Physics marks")
    print("3. Chemistry marks")
    print("4. Maths marks")
    print("5. Roll")
    print("6. Section")
    print("7. Class")
    print("8. Contact")
    print("9. Blood group")
    print("10. Cancel")
    
    choice = int(input())

    if choice == 1:
        print("Enter New Name:")
        name = input()
        if name == "":
            print("Name Cannot Be Empty")
            print("Enter New Name:")
            name = input()
        students[student_id]['name'] = name

    elif choice == 2:
        print("Enter New Physics Marks (0-100):")
        physics = int(input())
        if physics < 0 or physics > 100:
            print("Invalid Marks! Try Again.")
            print("Enter New Physics Marks (0-100):")
            physics = int(input())
        students[student_id]['physics'] = physics
        students[student_id]['grade'] = calculate_grade(physics, students[student_id]['chemistry'], students[student_id]['maths'])

    elif choice == 3:
        print("Enter New Chemistry Marks (0-100):")
        chemistry = int(input())
        if chemistry < 0 or chemistry > 100:
            print("Invalid Marks! Try Again.")
            print("Enter New Chemistry Marks (0-100):")
            chemistry = int(input())
        students[student_id]['chemistry'] = chemistry
        students[student_id]['grade'] = calculate_grade(students[student_id]['physics'], chemistry, students[student_id]['maths'])

    elif choice == 4:
        print("Enter New Maths marks (0-100):")
        maths = int(input())
        if maths < 0 or maths > 100:
            print("Invalid Marks! Try Again.")
            print("Enter New Maths Marks (0-100):")
            maths = int(input())
        students[student_id]['maths'] = maths
        students[student_id]['grade'] = calculate_grade(students[student_id]['physics'], students[student_id]['chemistry'], maths)

    elif choice == 5:
        print("Enter New Roll Number:")
        roll = int(input())
        for s_id, data in students.items():
            if s_id != student_id and data['roll'] == roll and data['class'] == students[student_id]['class'] and data['section'] == students[student_id]['section']:
                print("Roll Already Exists In This Class And Section!")
                return
        students[student_id]['roll'] = roll

    elif choice == 6:
        print("Enter new Section:")
        section = input()
        if section == "":
            print("Section Cannot Be Empty!")
            print("Enter New Section:")
            section = input()
        students[student_id]['section'] = section

    elif choice == 7:
        print("Enter New Class:")
        student_class = input()
        if student_class == "":
            print("Class Cannot Be empty!")
            print("Enter New Class:")
            student_class = input()
        students[student_id]['class'] = student_class

    elif choice == 8:
        print("Enter New Contact:")
        contact = input()
        if contact == "":
            print("Contact Cannot Be Empty!")
            print("Enter New Contact:")
            contact = input()
        students[student_id]['contact'] = contact

    elif choice == 9:
        print("Enter New Blood Group:")
        blood = input()
        if blood == "":
            print("Blood Group Cannot Be Empty!")
            print("Enter New Blood Group:")
            blood = input()
        students[student_id]['blood_group'] = blood

    elif choice == 10:
        return
    print("Student updated successfully!")
def show_top_scorer():
    if len(students) == 0:
        print("No students found!")
        return
    top_avg = 0

    for student_id, data in students.items():
        avg = (data['physics'] + data['chemistry'] + data['maths']) / 3
        if avg > top_avg:
            top_avg = avg

    print("ID         Name       Avg   Grade")
    print("---------------------------------")
    for student_id, data in students.items():
        avg = (data['physics'] + data['chemistry'] + data['maths']) / 3
        if avg == top_avg:
            avg_int = int(avg)
            print(student_id, "   ", data['name'], "    ", avg_int, " ", data['grade'])
def show_students_by_grade():
    print("Enter Grade to search (A+, A, B, C, D, F):")
    search_grade = input()
    
    count = 0
    for student_id, data in students.items():
        if data['grade'] == search_grade:
            if count == 0:
                print("ID        Name    Class Sec  Roll Phy Chem Maths Avg Grade     Contact     Blood")
                print("----------------------------------------------------------------------------------")
            avg = (data['physics'] + data['chemistry'] + data['maths']) / 3
            avg = int(avg) 
            print(student_id,  " "  ,data['name'], "   " ,data['class'], " " ,data['section'], "  " ,data['roll'], " " ,data['physics'], " ", data['chemistry'], " " , data['maths'], " " ,  avg, "   " , data['grade'], "   ",  data['contact'], " " , data['blood_group'])
            count = count + 1
            
    if count == 0:
        print("No students found with grade " + search_grade + "!")            
def exit():
	print("Thank You For Using Our Service")
	
while True:
    main()
    choice = int(input())
    if choice == 1:
        all_students()
    elif choice == 2:
        add_students()
    elif choice == 3:
    	remove_students()  
    elif choice == 4:
    	search_student()
    elif choice == 5:
    	edit_student()		  
    elif choice == 6:
    	show_top_scorer()	
    elif choice == 7:
    	show_students_by_grade()
    elif choice == 8:
    	exit()
    	break		