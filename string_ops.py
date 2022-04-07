def is_palindrome(x):
    try:
        x=x.lower()
        txt=x
        txts=txt[::-1]
        if txt == txts:
            return  True
        else:
            return  False
    except:
        print("try again")
is_palindrome("asasa")


def find_nth(string, word, n):
    try:
        start = string.find(word)
        while start >= 0 and n > 1:
            start = string.find(word, start+len(word))
            n -= 1
            
        return start
    except:
            print("your word not exist")
           
find_nth("This is an example. Return the nth occurrence of example in this example string.", "example",1 )



def solve(a,b):
    import re
    try:
            return bool (re.fullmatch(a.replace("*",".*"),b))
    except:
        print('trY again(:')
solve("QWQ*WE","QWQWE")