'''
There is three text file t1,t2 and t3 in this programming, I am reading from from all three file merging it into a output file using three three thread.
'''
import threading 
data1=data2=data3=""
def readFile1(): 
    """ 
    function to read from t1.txt file 
    """
    global data1
    file1 = open("t1.txt","r")
    data1=file1.read()
def readFile2(): 
    """ 
    function to read from t2.txt file 
    """
    global data2
    file1 = open('t2.txt', 'r')
    data2=file1.read() 

def readFile3(): 
    """ 
    function to read from t3.txt file 
    """
    global data3
    file1 = open('t3.txt', 'r')
    data3=file1.read()

    
t1 = threading.Thread(target=readFile1)
t1.start() 

t2 = threading.Thread(target=readFile2)
t2.start()

t3 = threading.Thread(target=readFile3)
t3.start()
#     t4 = threading.Thread(target=mergeFile)

t1.join() 
t2.join() 
t3.join()

def mergeFile():
    """
    function to merge all three file text in a single file
    """
    with open("output.txt",'w') as o:
        o.write(data1)
        o.write(data2)
        o.write(data3)

mergeFile()
