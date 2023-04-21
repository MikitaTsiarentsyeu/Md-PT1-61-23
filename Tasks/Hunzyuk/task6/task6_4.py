import time


numbers_list = list(range(100))
numbers_list.sort()

def get_function_parameters(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()

        with open('register.txt', 'w') as file:
            file.write(f"Function running time: {round((end - start), 2)} seconds \n")
            file.write(f"Input list: {args[0]}\n")
            file.write(f"Search value: {args[1]}\n")
            file.write(f"Search boundaries: {kwargs}\n")
            file.write(f"The result of the function: {res}")

        return res
    
    return wrapper


@get_function_parameters
def search(numbers_list, target, low, high):
    try:
        if not isinstance(numbers_list, list):
            raise TypeError("Invalid data type")
        
        if not isinstance(target, int) or not isinstance(low, int) or not isinstance(high, int):
            raise TypeError("Values for the search as well as the boundaries of the search must be numbers")
        
        if high >= low:
            mid = (low + high) // 2
            if numbers_list[mid] == target:
                return mid
            elif numbers_list[mid] > target:
                return search(numbers_list, target, low, mid -1)
            else:
                return search(numbers_list, target, mid + 1, high)
    except Exception as ex:
        return ex
        

print(search(numbers_list, 54, low=0, high=len(numbers_list)-1))