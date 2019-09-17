import hashlib


def read_txtfile():

    for line in open ('/Users/kimberlyarenas/Desktop/password_file.txt'): #pass through new values created
        col = line.split(',')
        user_Pass = col[1]
        hash_Password = col[2] 
        gen_pass(start, maxlen, user_Pass, hash_Password)

def gen_pass(s,mL,userP,hashP):
    if len(s) == mL: 
        return start #once the length has been reached returns empty string

    for i in range(0,10): #0-9 
        allPass = gen_pass(s + str(i), mL, userP, hashP) #int into string; save all the possible combinations
        concat = userP + allPass #concatenate user password with the hashed password
        hash_Pass = hash_with_sha256(concat) 
        check_pass(hashP, hash_Pass)
        final_verdict = check_pass(hashP, hash_Pass) #stores wether it be true or false 
    print(final_verdict) 
    return gen_pass(s + str(i),maxlen,userP, hashP)
    
def check_pass(hashP, hash_Pass): 
        if hashP != hash_Pass: 
            print('Not found!')
            return True        
        return False  
    sys.exit()
def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig

start = " " #variable s; empty string in order to be able to gen all possible combos 
maxlen = 2 #variable ml 
read_txtfile()
    
    
