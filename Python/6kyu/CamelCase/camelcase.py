text = "the_Stealth_Warrior"


def to_camel_case(text):
    arr = []
    str = ''
    if len(text) > 0:
        arr.append(text[0])
        x = 1
        cl = 0
        while x < len(text):
            y = text[x]
            if ((y >= "a" and y <= "z") or (y >= "A" and y <= "Z")):
                y = ord(y) - cl
                y = chr(y)
                arr.append(y)
                cl = 0
            else:
                if((text[x+1] >= "a" and text[x+1] <= "z")):
                    cl = 32
                else:
                    cl = 0
            x = x + 1
        
    for x in arr:
        str += x
    print(str)

to_camel_case(text)