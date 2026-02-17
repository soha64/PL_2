#17/02/2026

class vehicle:
    def move(self):
        print("vehicle  is moving")

class car(vehicle):
    def move(self):
        print("driving")

class bicycle(vehicle):
    def move(self):
        print("cycling")



vehicle = [car(), bicycle()]
for v in vehicle:
    v.move()





import shape_practicle_05

print("choose a shape to calc the area")
print("1.Circle")
print("2.Rectangle")
print("3.Triangle")

option = int(input("pick anyone from 1-3: "))

if option == 1:
    r= float(input("radius:  "))
    area= shape_practicle_05.area_circle(r)
    print("area:", area)

elif option == 2:
    l = float(input("lenght: "))
    w=float(input("width: "))
    area= shape_practicle_05.area_rectangle(l,w)
    print("arera:", area)

elif option == 3:
     l = float(input("lenght: "))
     w = float(input("width: 4"))
     area= shape_practicle_05.area_triangle(l,w)
     print("area:" ,area)
else :
    print("invalid")
