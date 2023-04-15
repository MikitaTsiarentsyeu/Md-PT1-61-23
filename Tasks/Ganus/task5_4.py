lower_case = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
upper_case = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]
def count_lower_upper(a: str) ->int:
    count_lower = 0
    count_upper = 0
    for i in a:
        if i in lower_case:
            count_lower += 1
        if i in upper_case:
            count_upper += 1
    return f"Количество символов нижнего регистра - {count_lower}, количество символов верхнего регистра - {count_upper}"
print(count_lower_upper("Hello, Mary. This day is sunny. UPSS"))