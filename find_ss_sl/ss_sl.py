def extract_numbers(l):
   numbers=set()
   
   for elem in l:
       if isinstance (elem,int):
           numbers.add(elem)
           
       elif isinstance (elem,str) and  elem.isdigit():
           numbers.add(int(elem))
             
             
       elif isinstance (elem,tuple):  
           numbers.update(extract_numbers(elem))
           
           
           
   return numbers 
   
   
def find_ss_sl(l):
    numbers=  extract_numbers(l)
    
    if len(numbers)<2:
        return None,None
        
        
    sorted_numbers= sorted(numbers)
    
    ss  = sorted_numbers[1]
    sl  = sorted_numbers[-2]
    
    return ss,sl
    
test_list = [10, "5", (1, 2, 3), "100", 20, 30, (40, 50, "60"), "7", (8, "9", 4)]
ss,sl= find_ss_sl(test_list)
print(f"ss:{ss}")
print (f"sl:{sl}")
        
       
