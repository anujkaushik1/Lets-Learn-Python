
class Student:

    def setName(self,n):   # self is the object
        self.__name = n;

    def getName(self):
        return self.__name;

    def setMarks(self,m):
        self.__marks = m;

    def getMarks(self):
        return self.__marks;

    def display(self):
        print("Name = ",self.__name );
        print("Marks = ",self.__marks);

obj = Student();
obj.setName("Anuj Kaushik");
obj.setMarks("100");
obj.display();