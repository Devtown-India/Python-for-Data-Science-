f = open('data/my_file.txt', 'r')
file_data = f.read()
f.close()

# with open('my_path/my_file.txt', 'r') as f:
#     file_data = f.read()

print(file_data)
