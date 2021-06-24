# Bai tap chuong 5
import numpy as np
data_type = [('name','S15'),('class',int),('heiht',float)]
students_details =[('james', 5,48.5),('nail', 6, 52.5),('paul',5,42.10)]
student =np.array(student_details,dtype=data_type)
print("Original array:")
print(student)
print("Sort by height")
print(np.sort(students,other='height')
