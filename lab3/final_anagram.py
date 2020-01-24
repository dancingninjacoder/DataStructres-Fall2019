#Kimberly Arenas 
#Imports the AVL_Trees and RB_Trees programs to build the binary trees
import AVLTree
import RBTree

#Creates and returns an AVL tree from the imported file.
def AVL(filename):  
    AVL = AVLTree.AVLTree()
    key = 0
    print("Processing AVL Tree...")
    print()
    #"latin-1" maps all possible byte values to the first 256 Unicode code points
    with open(filename, encoding="latin-1") as textFile: 
        for line in textFile:
            string = line.split()
            word = str(string) 
            stringedWord = word[2:len(word) - 2]
            key = make_key(stringedWord) 
            AVL.avlTree_insert(stringedWord, key)
    return AVL

#Creates and returns an Red and Black tree from the imported file.   
def RB(filename): 
    RB = RBTree.RedBlack()
    key = 0 
    print("Processing the Red and Black Tree...")
    print()
    with open(filename, encoding="latin-1") as textFile: 
        for line in textFile:
            string = line.split()
            word = str(string) 
            stringedWord = word[2:len(word) - 2]
            key = make_key(stringedWord)   
            RB.rbInsert(stringedWord, key)
    return RB
#Method that counts the number of anagrams a certain word has.
def count_anagrams(tree): 
    print("Please input a word for counting the number of anagrams:") 
    new_word = input() 
    count = search_anagrams(tree, new_word) 
    print("Total anagrams found were:", count)  

#Finds the necessary anagrams for both the maximum and count methods for the anagrams by using a binary search tree
def search_anagrams(tree, word, prefix=""):
    if len(word) <= 1: 
        str = prefix + word
        # print(str)
        key = make_key(str)  
        # print(key)
        searched_word = BSTsearch(tree, key)
        if (searched_word != None): 
            return 1 
        return 0 
    else:
        count_anagrams = 0 
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i]  
            after = word[i + 1:] 
            if cur not in before:
                count_anagrams += search_anagrams(tree, before + after, prefix + cur)
    return count_anagrams

#BST that will find the anagrams 
def BSTsearch(tree, key): 
    cur = tree.root   
    while cur != None:
        if key == cur.key:
            return cur 
        elif key < cur.key:
            cur = cur.left
        else:
            cur = cur.right
    return None

#Generates keys for each word by stringing together character numbers of each letter of a word.   
def make_key(word):  
    key = "" 
    res = list(word) 
    if (len(res[0]) > 1):   
        str_word = str(res[0]) 
        return make_key(str_word)
    for i in range(len(res)): 
        char = caps(res[i])
        char_num = ord(char) 
        char_str = str(char_num)
        key += char_str 
    key_int = int(key) 
    return key_int 
  
#Method activated by make key that will find the lower case letter by comparing it to its caps counterpart.
def caps(char): 
    capList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'N', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowerList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
    lowerChar = '' 
    for i in range(len(capList)): 
        if (char == capList[i]): 
            lowerChar = lowerList[i] 
            print(lowerChar)
            return lowerChar     
    return char 
  


#Finds the maximum number of anagrams from another text file
def maximum_anagrams(): 
    print("\nWould you like to load another file to find the word that has the most anagrams? Y/N") 
    print("1. Yes")
    print("2. No")
    user_selection = input() 
    count = 0
    if (user_selection == '1'):
        print("\nInput your filename:")
        filename = input() 
        tree = RB(filename) 
        anagrams = "" 
        anagrams_num = 0 
        with open(filename, encoding='windows-1252') as textFile:  
              for line in textFile:
                  string = line.split()
                  word = str(string)
                  word_str = word[2:len(word) - 2]
                  count = search_anagrams(tree, word_str)   
                  if (anagrams_num < count): 
                      anagrams = word_str 
                      anagrams_num = count     
        print("The word with the most anagrams is '", anagrams, "' with the total of", anagrams_num, "anagrams.")
        print("Terminating program...\nGoodbye!")
    elif (user_selection == '2'): 
        print("You have selected to exit the program.")
        print("Goodbye.")
    elif count == 3:
        print("ERROR: Too many incorrect statements...")
        print("Goodbye.")
    else: 
        print("ERROR: Input not valid!") 
        count+=1
        maximum_anagrams() 
#Main method asks for user input. User can choose to create an avl or rb tree.        
def main(): 
	print("Input textfile name: ") 
	filename = input() 
	
	print("") 
	print("Do you want to use an AVL tree or a Black-Red tree? Type '1' for AVL or type '2' for Red-Black.") 
	user_input = input()
	
	if (user_input == '1'):  
		tree = AVL(filename) 
		count_anagrams(tree) 
		
	elif (user_input == '2'): 
		tree = RB(filename)
		count_anagrams(tree) 
		
	else: 
		print("Invalid input, try again. \n") 
		main() 
		
main() 
maximum_anagrams()