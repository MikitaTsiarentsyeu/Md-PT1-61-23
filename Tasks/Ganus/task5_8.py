def count_symbol(a, symbol, result = []):
    a = a.lower()
   
    if not a:
        return ""
    else:
        
        if a[0] == symbol:
           
            result.append(a[0])
    
           
             
        count_symbol(a[1:], symbol)
  
    return len(result)

a = "Светит солнце, поют птицы"
print(count_symbol(a, symbol = "о"))
