class Person:
  def __init__ (self, std1, std2, std3, pre, mid, fin):
    self.__std1 = std1
    self.__std2 = std2
    self.__std3 = std3
    self.__pre = pre
    self.__mid = mid
    self.__fin = fin

  def grade(self):
    return (self.__pre + self.__mid + self.__fin) / 3

  def display1(self):
    print(self.__std1, self.grade())

  def display2(self):
    print(self.__std2, self.grade())

  def display3(self):
    print(self.__std3, self.grade())

class Student1(Person):
  std1 = Person("Student 1 Average: ", 0, 0, float(input("Prelim Grade: ")), float(input("Midterm Grade: ")), float(input("Final Grade: ")))
  std1.display1()

class Student2(Person):
  std2 = Person(0, "Student 2 Average: ", 0, float(input("Prelim Grade: ")), float(input("Midterm Grade: ")), float(input("Final Grade: ")))
  std2.display2()

class Student3(Person):
  std3 = Person(0, 0, "Student 3 Average: ", float(input("Prelim Grade: ")), float(input("Midterm Grade: ")), float(input("Final Grade: ")))
  std3.display3()
