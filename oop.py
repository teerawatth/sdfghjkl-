class Student:
    count = 0
    mean = []
    def __init__(self, number, name,mid,final,assign) -> None:
        self.number = number
        self.name = name
        self.mid = mid
        self.final = final
        self.assign = assign
        Student.count += 1
        Student.mean = []

    def sumScore(self):
        totalscore = self.mid + self.final + self.assign
        return totalscore

    def listStudent(self):
        print(f'{self.number}  {self.name}  {Student.sumScore(self)}')

# std1 = Student('001','John',15,35,20)
# std1.listStudent()
# std2 = Student('002','Jne',54,17,20)
# std2.listStudent()
# print(f'Number of student {Student.count}')

    