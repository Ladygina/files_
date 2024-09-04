filenames = ["1.txt", "2.txt", "3.txt"]
length_list = []
dict_length={}

for i in range( len(filenames) ):
    with open(filenames[i], 'r', encoding='UTF-8') as f:
        lines = len(f.readlines())
        length_list.append(lines)
    dict_length[lines] = filenames[i]

print(dict_length)
length_list.sort()
print(length_list)


with open('result.txt', 'w', encoding='UTF-8') as f:
    for i in range(len(length_list)):
         with open(str(dict_length[length_list[i]]), 'r', encoding='UTF-8') as ref:
            f.write(str(dict_length[length_list[i]])+'\n')
            f.write(str(length_list[i])+'\n')
            for line in ref:
                # write content to second file
                f.write(line)
            f.write("\n")
         ref.close()
f.close()
