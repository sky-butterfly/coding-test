def solution(my_string, letter):
    
    while(letter in my_string):
        my_string = my_string.replace(letter, '')
    
    return my_string