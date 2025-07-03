import copy

# Danh sách gốc
classroom = [["Alice", "Bob"], ["Charlie", "David"]]

# Tạo bản sao nông
shallow_copy = classroom.copy()
deep_copy = copy.deepcopy(classroom)
# Thay đổi học sinh đầu tiên của lớp đầu tiên

shallow_copy[0][1] = "Tabber"

print("Original:", classroom)
print("Shallow Copy:", shallow_copy)
print("Deep Copy: ", deep_copy)
