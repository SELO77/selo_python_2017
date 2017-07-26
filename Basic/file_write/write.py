import os
print(__file__)
file_dir = os.path.dirname(__file__)
rel_path = 'json/data.txt'
abs_file_path = os.path.join(file_dir, rel_path)
print("!!")
data = "sample text"
with open(abs_file_path, 'wb+') as f:
    f.write(bytes(data, encoding='utf-8'))