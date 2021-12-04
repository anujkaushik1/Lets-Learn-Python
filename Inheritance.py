
class A:

    def feature1(self):
        print("Feature 1 is working");

    def feature2(self):
        print("Feature 2 is working");



class B(A):

    def feature3(self):
        print("Feature 3 is working");

    def feature4(self):
        print("Feature 4 is working");

class C(B):

    def feature5(self):
        print("feature 5");

obj = C();


#Multiple Inheritance ------>



