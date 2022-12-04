# filename = "input/test3.txt"
filename = "input/input3.txt"


def find_power(input):
    temp = input
    count = 0
    while(temp != 1):
        temp = temp >> 1
        count += 1
    return count

# Uppercase numbers 65 - 27 = 38
# Lowercase 97 - 1 = 96

def find_common(list):
    number_list = []
    for l in list:
        number = 0
        for char in l:
            ascii = ord(char)
            if ascii >= 97:
                power_of_two = ascii-96
            else:
                power_of_two = ascii-38
            number = number | 2**power_of_two
        number_list.append(number)
        
    result = number_list[0]
    for i in range(1,len(number_list)):
        result = result & int(number_list[i])
    result = find_power(result)
    return result

total_1 = 0
temp = 0
total_2 = 0
with open(filename) as f:
    liste_2 = []
    for line in f:
        size = len(line)
        half = int(size/2)
        liste = [line[0:half], line[half:size-1]]        
        total_1 += find_common(liste)


        liste_2.append(line[0:len(line)-1])
        if temp != 2:
            temp += 1
        else:
            total_2 += find_common(liste_2)
            temp = 0
            liste_2 = []


    print(total_1)
    print(total_2)

