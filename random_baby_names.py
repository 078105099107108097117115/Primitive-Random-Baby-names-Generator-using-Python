import string, random

def generator():
    
    #Lets ask user for some input

    num_of_letters_in_name = input('Enter the number of letters to be in a random name: ')
    
    A_list_of_letter = []

    i = 0
    len_of_list = int(num_of_letters_in_name)-1

    while i <= len_of_list: 
        if i == 0:
            A_list_of_letter.append(random.choice(string.ascii_uppercase))
        else:
            A_list_of_letter.append(random.choice(string.ascii_lowercase))

        i+=1
    name = "".join(A_list_of_letter)
    return(name)

print(generator())

vowels = 'aeiou'
upper_vowels = vowels.upper()

consonants = 'bcdfghjklmnpqrstvwxyz'
upper_consonants = consonants.upper()

letter = string.ascii_lowercase
upper_letter = string.ascii_uppercase

def new_generator():
    num_of_letter_in_new_name = input('Enter num of letters in name: ')
    num = int(num_of_letter_in_new_name)

    new_List = []
    name_List = []

    n = 0
    while n <= (num-1):
        new_List.append(input('Enter letter "v" for vowel, letter "c" for consonant or letter "l" for any arbitrary letter, or specify the letter itself: '))

        if new_List[n] == "v":
            if n == 0:
                name_List.append(random.choice(upper_vowels))
            else:
                name_List.append(random.choice(vowels))
                
        elif new_List[n] == "c":
            if n == 0:
                name_List.append(random.choice(upper_consonants))
            else:
                name_List.append(random.choice(consonants))
           
        elif new_List[n] == "l":
            if n == 0:
                name_List.append(random.choice(upper_letter))
            else:
                name_List.append(random.choice(letter))
        else:
            if n == 0:
                name_List.append(new_List[n].upper())
            else:
                name_List.append(new_List[n])
        n+=1
    
    finalName = "".join(name_List)
    return finalName

print(new_generator())




























