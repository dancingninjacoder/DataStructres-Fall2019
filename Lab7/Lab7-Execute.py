#Imports the edit_distance program needed to implement the graphs
import EditDistance as ed

def main():
    print("Hello this is the Edit Distance Program that performs the distance of words in three different tests cases.\nTest 1 performs it on two distinct ones that so happen to be my favorite phrase together.\nTest 2 performs it on the same word.\nTest 3 performs it on one word and an empty string.") 
    print("")
    print("Then allow you to compare your own words.\nLet's initiate: ") 
    print("")
    print("Test 1: ")
    #Test case 1
    word_1 = "fire"
    word_2 = "dynasty"
    print("Words being compared are '",word_1,"' and '",word_2,"'.")
    print("\t\t...calculating their distance...\n" )
    print ("Distance between them: ", end = '')
    print(ed.EditDistance(word_1, word_2, len(word_1), len(word_2)))
    print("")
    print("Test 2: ")
    #Test case 2
    word_1 = "elvis"
    word_2 = "elvis"
    print("Words being compared are '",word_1,"' and '",word_2,"'.")
    print("\t\t...calculating their distance...\n" )
    print ("Distance between them: ", end = '')
    print(ed.EditDistance(word_1, word_2, len(word_1), len(word_2)))
    print("")
    print("Test 3: ")
    #Test case 3
    word_1 = "styles"
    word_2 = ""
    print("The two words being compared are '",word_1,"' and '",word_2,"'.")
    print("\t\t...calculating their distance...\n" )
    print ("Distance between them: ", end = '')
    print(ed.EditDistance(word_1, word_2, len(word_1), len(word_2)))
    print("")
    print("Now that the test are completed...")
    print("Would you like to try two words for yourself? Yes or No")
    user_sel = input()
    if(user_sel == 'yes' or user_sel == 'Yes' or user_sel == 'YES'):
        print("Excellent! Now, which two words would you like to try?")
        print("Word 1: ")
        word_1 = input()
        print("Word 2: ")
        word_2 = input()
        print("The two words being compared are '",word_1,"' and '",word_2,"'.")
        print("\t\t...calculating their distance...\n" )
        print ("Distance between them: ", end = '')
        print(ed.EditDistance(word_1, word_2, len(word_1), len(word_2)))
        print("")
        print("Program complete!\nThank you for participating")
    elif(user_sel == 'no' or user_sel == 'No' or user_sel == 'NO'):
        print("Okay.")
        print("See you again soon!")
    else:
        print("ERROR!\nInput invalid!")
        print("Terminating...\nGoodbye!")
    
main()