import time

chunk = 1

start = time.time()
with open('test.jpg', 'rb') as donor:
    with open('test-copy.jpg', 'wb') as receiver:
        while True:
            file_part = donor.read(chunk)
            if file_part:
                receiver.write(file_part)
            else:
                break
end = time.time()

print(end-start)