class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for i in self.marks:
            sum += i

        print(f"Hi {self.name} your avg score is = {sum/len(self.marks)}")


s1 = Student("mahesh", [97, 98, 95])
s1.get_avg()

s2 = Student("karan", [84, 75, 99])
# s2.get_avg()

s2.name = "mahesh maurya"
s2.get_avg()
