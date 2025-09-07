classes = [
    ["Alice", "Bob", "Charlie"],
    ['Rick', "Eve", "Aldi"],
    ["Grace", "Heidi", "Avan"]
] #list of classes
checked_student= 0 #number of checked student
for current_class in classes:
  for student in current_class : #skipping students whose name starts with G
     if student[0] == "G": #making sure its not checked
      continue
     if student[0] == "A":
      print("Student", student, "is present")
     if student == "Eve" :
      print("Student Eve is found")
      break
     checked_student+=1 #add one for each student check
print("Total students checked :", checked_student)