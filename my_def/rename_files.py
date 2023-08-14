import os


def rename_file(final_name, number_of_digits, source_extension, resulting_extension, begin_range, end_range):
    count = 0
    for file in os.listdir():
        extention = file.split('.')[-1]
        if extention == source_extension:
            extention = resulting_extension
            name = file.split('.')[0]
            my_index =  str(count).rjust(number_of_digits, '0')
            new_name = name[begin_range:end_range+1] + final_name + my_index
            count += 1
            os.rename(file, new_name+'.'+extention)