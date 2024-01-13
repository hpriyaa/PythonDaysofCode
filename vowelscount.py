# Program to count number of vowels in string

# Function that returns the count of number of vowels
def vowels_count(string_inp):
    string_inp = string_inp.lower()
    # vowels = 'aeiou'
    count = 0
    for i in string_inp:
        if i in 'aeiou':
            count += 1
    return count


# Function that returns count of each individual vowels
def vowels_individual_count(string_input):
    string_input = string_input.lower()
    vowels = 'aeiou'

    # initializing dictionary with vowels as key and value as 0
    count = {}.fromkeys(vowels, 0)
    for char in string_input:
        if char in count:
            count[char] += 1
    return count


input_string = input('Enter a string : ')

print("No. of vowels : " + str(vowels_count(input_string)))
print(vowels_individual_count(input_string))
