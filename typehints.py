'''type hints untuk fungsi'''

# bentuk standar fungsi yang udah kita pelajari

'''
 studi kasus
def fungsi(parameter):
    print(parameter)

fungsi(1)
fungsi("ucup")
fungsi(True)
'''

# penggunaan type hints


import string 

def sepuluh_pangkat(argument:int) -> int:
    '''fungsi dengan hints'''
    output = 10**argument
    return output

HASIL = sepuluh_pangkat(4)
print(HASIL)

def display(argument:string):
    '''fungsi dengan string'''
    print(argument)

display("ucup")
