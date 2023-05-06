new_dict = dict()
with open('1.txt', 'rt') as file_1:
    lenght_1 = len(file_1.readlines())
with open('2.txt', 'rt') as file_2:
    lenght_2 = len(file_2.readlines())
if lenght_1 > lenght_2:
    with open('final.txt', 'wt') as final_file:
        final_file.write('2.txt\n')
        final_file.write(f'{lenght_2}\n')
        for index in range(1,lenght_2+1):
            final_file.write(f'Line {index} of file 2\n')
        final_file.write('1.txt\n')
        final_file.write(f'{lenght_1}\n')
        for index in range(1,lenght_1+1):
            final_file.write(f'Line {index} of file 1\n')
else:
    with open('final.txt', 'wt') as final_file:
        final_file.write('1.txt\n')
        final_file.write(f'{lenght_1}\n')
        for index in range(1,lenght_1+1):
            final_file.write(f'Line {index} of file 1\n')
        final_file.write('2.txt\n')
        final_file.write(f'{lenght_2}\n')
        for index in range(1,lenght_2+1):
            final_file.write(f'Line {index} of file 2\n')