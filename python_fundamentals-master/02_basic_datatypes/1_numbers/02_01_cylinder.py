'''
Write the necessary code to calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''
import math

radius = 3.14
height = 5

volume_cylinder = (math.pi * radius**2 * height)
surface_area_cylinder = 2 * math.pi * radius * (height+radius)


print(("Cylinder volume = " + str(round(volume_cylinder, 4))))
print(("Cylinder surface area = " + str(round(surface_area_cylinder, 4))))





