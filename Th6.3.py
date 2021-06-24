# Bai tap chuong 6   
class py_solution(object):
 def roman_to_int(self,s):
     rom_val={'I':1, 'V':5, 'X':10,'L':50,'C':100}
     for i in range(len(s)):
         if i>0 and rom_val[s[i]]>rom_val[s[i-1]]:
             int_val+=rom_val[s[i]-2*rom_val[s[i-1]]]
         else:
            int_val+=rom_val[s[i]]
     return int_val

print(py_solution().roman_to_int('MMMCMLXXVI')
#print(py_solution().roma_to_int('MMMM')
#print(py_solution().roma_to_int('C')
         
    
