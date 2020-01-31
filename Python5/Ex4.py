class Shape:
    def tinhChuvi(self):
        print("Chu vi")

    def tinhDientich(self):
        print("Dien tich")

class Circle(Shape):

    r = 0
    def typeBankinh(self):
        r = float(input("Nhap ban kinh : "))
        self.r = r

    def tinhChuvi(self):
        print("Chu vi hinh tron: "+ str(2*self.r*3.14))

    def tinhDientich(self):
        print("Dien tich hinh tron: "+str(self.r*self.r*3.14))

# class Triangle(Shape):
#     r = 0
#     def tinhChuvi(self, r):
#         print("Chu vi tam giac: "+ str(2*r*3.14))
#
#     def tinhDientich(self, r):
#         print("Dien tich tam giac: "+str(r*r*3.14))
#
# class Retangle(Shape):
#     r = 0
#     def tinhChuvi(self, r):
#         print("Chu vi chu nhat: "+ str(2*r*3.14))
#
#     def tinhDientich(self, r):
#         print("Dien tich chu nhat: "+str(r*r*3.14))
#
# class Square(Shape):
#     r = 0
#     def tinhChuvi(self, r):
#         print("Chu vi hinh vuong: "+ str(2*r*3.14))
#
#     def tinhDientich(self, r):
#         print("Dien tich hinh vuong: "+str(r*r*3.14))

circle = Circle()
circle.typeBankinh()
circle.tinhChuvi()