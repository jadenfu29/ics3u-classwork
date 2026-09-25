heightinches= float(input("Height in inches: "))
heightfeet = float(input("Height in feet: "))
heightinches+=heightfeet*12
height = heightinches/39.37
weight = float(input("Weight in pounds: "))
weight/=2.205
height **=2
weight/=height
print(weight)

