def convhex(x):
    y = ""
    if x <= 0:
        y = "00"
    elif x > 0 and x < 16:
        y = "0" + hex(x).lstrip("0x")
    elif x >= 255:
        y = "FF"
    else:
        y = hex(x).lstrip("0x")
    
    return y

def rgb(r, g, b):

    y = (convhex(r) + convhex(g) + convhex(b))
    return y.upper()