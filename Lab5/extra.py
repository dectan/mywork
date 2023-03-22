#source code chat gpt

student_data = {}

name = input("Enter the student's name: ")

# Loop to read in the module names and grades
while True:
    
    module_name = input("Enter a module name (or leave blank to finish): ")
    
    if module_name == '':
        break
    
    # Read in the grade for the module
    grade = input("Enter the grade for module:")
    
    # Add the module name and grade to the student's data
    student_data[module_name] = grade
    
# Print the student's data
print("Student Name: {}".format(name))
for module, grade in student_data.items():
    print("{}: {}".format(module, grade))