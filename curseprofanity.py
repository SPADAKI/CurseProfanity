import urllib
def profanity():
    text=open("/Users/user/Documents/PY/movie_quotes.txt")  
    content = text.read()
    print(content)
    text.close()
    profanity_check(content)

def profanity_check(content_to_send):
    examine = urllib.urlopen("http://www.wdylike.appspot.com/?q="+ content_to_send)
    output = examine.read();
    if "false" in output:
        print("profanity not found!!!")
    else:
        print("Profanity found!!!")

    
    examine.close()
    
profanity()
