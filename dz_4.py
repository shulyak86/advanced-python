def get_denominator(file):
    num = 0
    try:
        with open(file, 'r') as f:
            stroka = f.read()
            if not stroka.isdigit():
                raise Exception('It is not a number in the file. Check it please')
            elif stroka == '0':
                raise Exception('It is a 0 in the file. Need valid number')
            else:
                num = int(stroka)
    except FileNotFoundError:
        print('File not found')
    return num


def get_list_of_numbers(denominator):
    list_all_numbers = [i for i in range(1, 100)]
    new_numbers = []
    for i in list_all_numbers:
        if i % denominator == 0:
            new_numbers.append(i)
    return new_numbers


def get_sum(list_of_numbers):
    sum = 0
    for i in list_of_numbers:
        sum += i
    return sum


def write_result(number_to_write, file_name):
    with open(file_name, 'w') as file:
        file.write(str(number_to_write))


number_to_write = get_sum(get_list_of_numbers(get_denominator('d.txt')))

file_name = 'some_new_file'

write_result(number_to_write, file_name)
