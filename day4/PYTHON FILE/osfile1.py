# os module with file


try:
    # If the file does not exist,
    # then it would throw an IOError
    filename = 'demo.txt'
    f = open(filename, 'r')
    text = f.read()
    print("File Contents : ", text)
    f.close()
 
# Control jumps directly to here if 
#any of the above lines throws IOError.    
except IOError:
     print('Problem reading: ' + filename)
     
# In any case, the code then continues with 
# the line after the try/except
