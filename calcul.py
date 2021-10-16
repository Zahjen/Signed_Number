base_reg = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

# Get total number of digits, i.e. for 5328 -> 4
def get_length(n: str) -> int :
    return len(n)

# Get the first digit of a number, i.e. for 5328 -> 5
def get_first_digit(n: str) -> str :
    return n[0]

# Base needs to be in decimal, i.e. if we have a number in hexa, we have to write 16, in octal, we should have 8, in binary, we have 2
def get_sign(n: str, base: int) -> bool :
    first_digit = get_first_digit(n = n)
    middle_base = int(base / 2 - 1)
    index_of_first_digit = base_reg.index(first_digit)

    #If the number is non - negative, we're returning True, if it is negative, we're returning False
    if (0 <= index_of_first_digit and index_of_first_digit <= middle_base) :
        return True
    else : 
        return False

# Extend a number to operate addition or subtraction according to its sign
def number_extension(n: str, ext_number: str, length_1: int, length_2: int, base: int) -> str : 
    for i in range(length_1 - length_2) :
        if (get_sign(n = n, base = base) == True) :
            ext_number += str(0)
        else :
            ext_number += base_reg[base - 1]
            
    ext_number += n

    return ext_number

# Determine which number we need to extend
def number_extension_digit(number_1: str, number_2: str, base: int) -> tuple :
    length_nb_1 = get_length(n = number_1)
    length_nb_2 = get_length(n = number_2)
    extended_number = ""

    # We are extending the first number, i.e. number_1
    if (length_nb_1 < length_nb_2) :
        extended_number = number_extension(n = number_1, ext_number = extended_number, length_1 = length_nb_2, length_2 = length_nb_1, base = base)
        return extended_number, number_2
    
    # We are extending the second number, i.e. number_2
    else :
        extended_number = number_extension(n = number_2, ext_number = extended_number, length_1 = length_nb_1, length_2 = length_nb_2, base = base)
        return number_1, extended_number

# Convert number from decimal to a given basis between hexa, octal and binary
def convert_dec_to_other_basis(n: str, base: int) -> str :
    if (base == 2) :
        return bin(n)
    elif (base == 8) :
        return oct(n)
    elif (base == 16) :
        return hex(n)

# Determine the complement of a given number
def complement(n: str, base: int) -> str :
    number_length = get_length(n = n)
    cplt_base = str(10**(number_length))
    cplt_dec = int(cplt_base, base) - int(n, base)
    cplt = convert_dec_to_other_basis(n = cplt_dec, base = base)[2:].upper()

    if (get_sign(n = n, base = base) == False and get_sign(n = cplt, base = base) == False) :
        # We are extending the complement if needed. We place [0] in order to only get the complement element
        return number_extension_digit(number_1 = "0" + cplt, number_2 = n, base = base)[0]
    else :
        return cplt

# Addition
def addition(number_1: str, number_2: str, base: int) -> str :
    # We are extending the two numbers
    ext_nbr = number_extension_digit(number_1 = number_1, number_2 = number_2, base = base)
    # Result is given on decimal basis 
    add = int(ext_nbr[0], base) + int(ext_nbr[1], base)
    # Addition is now giving the correct result in the correct basis
    result = convert_dec_to_other_basis(n = add, base = base)[2:].upper()

    # We are adding two non - negative numbers. Result needs to be non - negative.
    if (get_sign(n = number_1, base = base) == True and get_sign(n = number_2, base = base) == True) :
        if (get_sign(n = result, base = base) == False or base == 2) :
            return "0" + result
        else : 
            return result
    # We are adding two negative numbers. Result needs to be negative
    elif (get_sign(n = number_1, base = base) == False and get_sign(n = number_2, base = base) == False) :
        if (get_sign(n = result[1:] + " = ", base = base) == True or base == 2) :
            print(base_reg[base - 1] + result[1:], end="")
            return "-" + complement(n = base_reg[base - 1] + result[1:], base = base)
        else : 
            print(result[1:] + " = ", end="")
            return "-" + complement(n = result[1:], base = base)
    # We are adding two opposite sign numbers
    else :
        if (get_length(ext_nbr[0]) == get_length(result)) :
            if (get_sign(n = result, base = base) == True) :
                return result
            else : 
                print(result + " = ", end="")
                return "-" + complement(n = result, base = base)
        elif (get_length(ext_nbr[0]) < get_length(result)) :
            return result[1:]
        else :
            return "0" + result[1:]
        
# Subtractiing two numbers. Let's assume the subtraction is as follow : number_1 - number_2
def subtraction(number_1: str, number_2: str, base: int) -> str :
    # We are extending the two numbers
    ext_nbr = number_extension_digit(number_1 = number_1, number_2 = number_2, base = base)
    cplt_second_number = complement(n = ext_nbr[1], base = base)
    sub = addition(number_1 = ext_nbr[0], number_2 = cplt_second_number, base = base)
    
    return sub


#print(subtraction("01","010110", 2))
#print(addition("5FA","210",16))