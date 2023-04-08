
enter = int(input("Введите, пожалуйста, максимальное количество символов в строке(должно быть больше 35)\n"))
with open ("text.txt", "r", encoding = "utf-8") as f:
    lines = f.readlines()
    result = ""
   
    for i in lines:
        result_str = ""
        new_str = ""
        i = str(i)
        count = 0
        len_str = len(i)
        
        for j in i.split():
            j = str(j)
            new_str = new_str + j + " "

            if (len(new_str)-1) == enter:
                result_str = result_str + new_str[:-1] + "\n"
                count += (len(new_str)-1)
                new_str = ""
            
            elif (len(new_str)-1) > enter:
              
                margin_len = ((len(new_str) - 1) - (len(j)+1))
     
                margin = ((enter) - (margin_len))
                count += (len(new_str)-1-len(j))
           
                if new_str[:-1].count(" ") >= margin:
           
                    new_str = new_str.replace(" ", "  ", margin)
                elif new_str[:-1].count(" ") >= (int(margin/2)):
                    new_str = new_str.replace(" ", "   ", int(margin/2))
                elif new_str[:-1].count(" ") >= (int(margin/3)):
                    new_str = new_str.replace(" ", "    ", int((margin/3)))
                elif new_str[:-1].count(" ") >= (int(margin/4)):
                    new_str = new_str.replace(" ", "     ", int((margin/4)))


                result_str = result_str + new_str[:margin_len + margin] + "\n"

                new_str = j + " "
            elif ((len_str - count) < enter) and (len(new_str)< enter):
                result_str = result_str + new_str 
                new_str = ''
                if j == i.split()[-1]:
                    result_str = result_str + "\n"
        result = result + result_str  
new_text = open('new_text.txt', "w", encoding = "utf-8")
new_text.write(result)
print("Файл перезаписан!")
new_text.close()
       
    

              
       
        
     
       


            
                          
            

            
            

           

