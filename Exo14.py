
word = input("Word: ")


word_length = len(word)

total_width = 30
spaces_on_each_side = (total_width - word_length) // 2

top_and_bottom = '*' * total_width
middle_line = '*' + ' ' * spaces_on_each_side + word + ' ' * (total_width - word_length - spaces_on_each_side - 2) + '*'

print(top_and_bottom)
print(middle_line)
print(top_and_bottom)
