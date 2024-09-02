def slice(obj, slicing_param):
        output = [] if isinstance(obj, list) else ""
        step = 1
        if not obj:
                return obj
        elif len(slicing_param) > 3 or not isinstance(slicing_param,list):
                return "Slicing param must be [start, end, step]"
        elif len(slicing_param) == 1:
                return obj[slicing_param[0]]
        elif len(slicing_param) == 2:
                start, end = slicing_param[0], slicing_param[1]

        elif len(slicing_param) == 3:
                if slicing_param[2] > 0:
                        start = slicing_param[0] if slicing_param[0] != '-' else 0
                        end = slicing_param[1] if slicing_param[1] != '-' else len(obj)
                        step = slicing_param[2]
                elif slicing_param[2] < 0:
                        start = slicing_param[1] if slicing_param[0] != '-' else len(obj)-1
                        end = slicing_param[0] if slicing_param[1] != '-' else -1
                        step = slicing_param[2]
                else:
                        return "Step cannot be zero!!"


        for i in range(start, end, step):
                if type(output) == list:
                        output.append(obj[i])
                else:
                        output += obj[i]
        return output


print(slice([1, 2, 3, 4, 5], ['-', '-', -1])) 
print(slice("abcdef", [1, 2, 1]))            
print(slice("abcdef", [1, 5, 2]))                      
