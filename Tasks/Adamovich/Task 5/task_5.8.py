#8. Write a recursive function to count the number of occurrences of a given character in a string.


def count_of_occurences(string, chr):
      if not string:
        return 0
      elif string[0] == chr:
            return 1 + count_of_occurences(string[1:], chr)
      else:
            return count_of_occurences(string[1:],chr)
      

print(count_of_occurences("mama", "m"))