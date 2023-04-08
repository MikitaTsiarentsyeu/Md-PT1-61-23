# 3. Write a program that takes a string as input and returns a dictionary with the count of each word in the string.
str = "the dog dog the calm before the storm";
count = dict();
words = str.split();

for word in words:
    if word in count:
        count[word] += 1;
    else:
        count[word] = 1;

print(count);

