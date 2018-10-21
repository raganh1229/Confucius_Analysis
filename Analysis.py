from collections import Counter #Importing to organize various lists used later in the program
from collections import defaultdict

break_cond = 0 #Variable for breaking entrance loop.
word_count = -1 #Variable for storing the total number of characters in the document.
word_1_count = 0 #Counter for the number of occurrences of word 1.
word_2_count = 0 #Counter for the number of occurrences of word 2.
total_dist = 0 #Counter for the total distance between two characters.
dist_count = 0 #Counts the number of distance iterations between two characters
word_list = [] #list created that keeps track of each word.
word_list_char1 = [] #list of words near character 1.
word_list_char2 = [] #list of words near character 2.
word_1_OC = [] #list of occurrences of word 1.
word_2_OC = [] #list of occurrences of word 2.

while break_cond != 1:
    #Prompt for entering the first Chinese character.
    first_char = input('Enter the first character to analyze: ')

    if len(first_char) > 1:
        print("Please enter only one Chinese character")
        continue

    try:
        val = int(first_char)
        print("That is not a valid Chinese character.")
        break_cond = 0
    except:
        break_cond = 1

#Prompt for entering the second Chinese character.
break_cond = 0 #Variable for breaking entrance loop is reset.
while break_cond != 1:
    #Prompt for entering the first Chinese character.
    second_char = input('Enter the second character to analyze: ')

    if len(second_char) > 1:
        print("Please enter only one Chinese character")
        continue

    try:
        val = int(second_char)
        print("That is not a valid Chinese character.")
        break_cond = 0
    except:
        break_cond = 1

#Prompt for entering the name of the file to analyze text from.
file_name = input("Enter the core name of the text you wish to analyze: ")

with open(file_name + '.txt', encoding='utf8') as f:
    for line in f:
        line = line.strip() #removes new lines or spaces at the start/end.    
        for word in line: #Iterates over each line and counts the position of each word.

            word_count += 1
            word_list.append(word)
            
            if word == first_char: #If a user-inputted word is found, it iterates that character's word count by one and appends it's location to the list of it's indices.
                word_1_count += 1
                word_1_OC.append(word_count)


            if word == second_char: #If a user-inputted word is found, it iterates that character's word count by one and appends it's location to the list of it's indices.
                word_2_count += 1
                word_2_OC.append(word_count)

for tmp in word_1_OC: 
    six_count = 6
    six_count2 = 6

    while six_count > 0: #Cycles through the indices of a various word and collects data related to the six characters before and after that specific character.
         word_list_char1.append(word_list[tmp - six_count])
         six_count -= 1

    while six_count2 > 0:
         word_list_char1.append(word_list[tmp + six_count2])
         six_count2 -= 1




for tmp in word_2_OC:
    six_count = 6
    six_count2 = 6

    while six_count > 0: #Cycles through the indices of a various word and collects data related to the six characters before and after that specific character.
         word_list_char2.append(word_list[(tmp - six_count)])
         six_count -= 1

    while six_count2 > 0:
         word_list_char2.append(word_list[(tmp + six_count2)])
         six_count2 -= 1

#i = 1
#while i <= 6:
 #   x = count_list_1.most_common(i)
  #  sum_of_distances = sum(x
   # sum_of_distances_list.append(sum_of_distances)
    #i += 1

count_list_1 = Counter(word_list_char1) #Makes use of the imported library to rank the number of times a various character appears next to the desired character inputted by the user.
count_list_2 = Counter(word_list_char2)

#Printing out various pieces of information about the relevant data.
print("\nThe top six characters found in proximity to", first_char, "are", count_list_1.most_common(6))
print("The top six characters found in proximity to", second_char, "are", count_list_2.most_common(6), "\n")

print("There are", (word_count), "total characters in the document.")
print(first_char, "appears", word_1_count, "times in this document.")
print(second_char, "appears", word_2_count, "times in this document.\n")

print(first_char, "consists of", ((word_1_count/word_count)*100),"% of the total document.")
print(second_char, "consists of", ((word_2_count/word_count)*100),"% of the total document.\n")

