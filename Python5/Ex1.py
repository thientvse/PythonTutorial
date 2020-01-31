class Person:
    name = ""
    address = ""
    age = 0

    def inputDetails(self):
        a = str(input("Nhap name : "))
        b = str(input("Nhap address : "))
        c = str(input("Nhap age : "))

        self.name = a
        self.address = b
        self.age = c

    def displayDetails(self):
        print("Name : "+str(self.name))
        print("Address : "+str(self.address))
        print("Age : "+str(self.age))

person = Person()
person.inputDetails()
person.displayDetails()



