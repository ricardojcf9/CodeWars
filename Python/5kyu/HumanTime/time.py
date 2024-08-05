seconds = 86399

def make_readable(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds = seconds%3600
    min = seconds // 60
    seconds = seconds % 60
    
    return(hour,':',min,':',seconds)
    
make_readable(seconds)