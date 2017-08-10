class Student():
    def averageScore(self):
        total = 0
        for score in self.testScore:
            total += score
        total = total / len(self.testScore)
        return total

    def __init__(self, n, i):
        self.name = n
        self.idNum = i
        self.testScore = []
        self.average = 0

    def __str__(self):
        nameInfo = "Name: " + self.name
        idInfo = "ID Number: " + str(self.idNum)
        scoreInfo = "Scores: "
        if len(self.testScore) > 0:
            length = len(self.testScore) - 1
            for score in range(length):
                scoreInfo += str(self.testScore[score]) + ", "
            scoreInfo += str(self.testScore[length])
        else:
            scoreInfo += "0"
        avgInfo = "Average Score: " + str(self.average)
        return nameInfo + "\n" + idInfo + "\n" + scoreInfo + "\n" + avgInfo

    def addScore(self, s):
        self.testScore.append(s)
        self.average = self.averageScore()

class Roster():
    def __init__(self):
        self.studentList = []

    def addStudent(self, newStudent):
        self.studentList.append(newStudent)

    def isStudentThere(self, student_id):
        for student in self.studentList:
            studentID = student.idNum
            if studentID == student_id:
                return True
        return False

    def deleteStudent(self, student_id):
        if self.isStudentThere(student_id):
            for student in range(len(self.studentList)):
                studentID = self.studentList[student].idNum
                if studentID == student_id:
                    self.studentList.pop(student)
                    return True
        else:
            return False

    def viewRecord(self, student_id):
        for student in range(len(self.studentList)):
            studentID = self.studentList[student].idNum
            if studentID == student_id:
                return self.studentList[student]

Bill = Student("Bill Frank", 123456788)

Joe = Student("Joe Bob", 123456789)
print("")
print("Prints Joe's record:")
print("")
print(Joe)
print("")

Joe.addScore(60)
Joe.addScore(100)
Joe.addScore(95)
Joe.addScore(88)
print("Prints Joe's record (added scores)")
print("")
print(Joe)
print("")

roster = Roster()
roster.addStudent(Bill)
roster.addStudent(Joe)
print("Prints true if student is in the list:")

print(roster.isStudentThere(123456788))
print("")
roster.deleteStudent(123456788)
print("Deleted Bill:")
print(roster.isStudentThere(123456788))
print("")
print("Prints Joe's record:")
print(roster.viewRecord(123456789))
print("")

roster.addStudent(Bill)
print("Added Bill, prints Bill's record:")
print(roster.viewRecord(123456788))
