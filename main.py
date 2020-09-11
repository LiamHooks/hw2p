# Author: Liam Hooks lrh5428@psu.edu
# Collaborator: Seulki Kim svk6271@psu.edu
# Collaborator: Angela Bao ymb5072@psu.edu
# Collaborator:
# Section: 2
# Breakout: 2
def getGradePoint(letter):
    if letter == "A":
      return 4.0
    elif letter == "A-":
      return 3.67
    elif letter == "B+":
      return 3.33
    elif letter == "B":
      return 3.0
    elif letter == "B-":
      return 2.67
    elif letter == "C+":
      return 2.33
    elif letter == "C":
     return 2.0
    elif letter == "D":
      return 1.0
    else:
      return 0.0

def run():
  letter1 = input("Enter your course 1 letter grade: ")
  gradePoint1 = getGradePoint(letter1)
  credit1 = float(input("Enter your course 1 credit: "))
  print(f"Grade point for course 1 is: {gradePoint1}")

  letter2 = input("Enter your course 2 letter grade: ")
  gradePoint2 = getGradePoint(letter2)
  credit2 = float(input("Enter your course 2 credit: "))
  print(f"Grade point for course 2 is: {gradePoint2}")

  letter3 = input("Enter your course 3 letter grade: ")
  gradePoint3 = getGradePoint(letter3)
  credit3 = float(input("Enter your course 3 credit: "))
  print(f"Grade point for course 3 is: {gradePoint3}")

  gpa = ((gradePoint1 * credit1) + (gradePoint2 * credit2) + (gradePoint3 * credit3)) / (credit1 + credit2 + credit3)

  print(f"Your GPA is: {gpa}")

if __name__ == "__main__":
  run()