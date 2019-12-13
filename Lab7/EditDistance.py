#Method that alters two given strings based on the rules of edit distance
def EditDistance(word_1, word_2, len_1 , len_2): 
    #If the length of the first string is none, it will return the length of the second string 
    if len_1 == 0: 
         return len_2
    #If the length of the second string is none, it will return the length of the first string
    if len_2 == 0: 
        return len_1
    #If the last characters of both strings are the same, it will return the count of the remaining characters and will ignore the duplicated ones
    if word_1[len_1-1] == word_2[len_2-1]: 
        return EditDistance(word_1,word_2,len_1-1,len_2-1) 
    #Returns one for the counter indicating that the last elements of the string are not the same. The program will then proceed to perform the three operations, insert, remove, and replace to find the best solution
    return 1 + min(EditDistance(word_1, word_2, len_1, len_2-1),    # Insert 
                   EditDistance(word_1, word_2, len_1-1, len_2),    # Remove 
                   EditDistance(word_1, word_2, len_1-1, len_2-1))   # Replace 