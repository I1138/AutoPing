import subprocess # subproccess is used to make command line calls


#get ip range
adress = str(input("enter ip adress range: "))
#parse input, and assign variables.
adress = str.split(adress,sep=".")
#print(adress)
scan = adress.pop()
scan = str.split(scan, sep="-")
#print(scan)
first = scan.pop(0)
#print(first)
first = int(first)
last = scan.pop()
#print(last)
last = int(last)
current = first
top = adress.pop(0)
#print(top)
middle = adress.pop(0)
#print(middle)
bottom = adress.pop(0)
#print(bottom)

#main loop
for i in range(last-first+1):
        received = "false"
        #cmd-line call
        cmd = "ping /n 1 " + top + "." + middle + "." + bottom + "." + str(current) + " | findstr Reply"
        text = subprocess.run(cmd,stderr=subprocess.STDOUT,shell=True,stdout=subprocess.PIPE)
        #parse command output
        text = str(text)
        #print(text)
        textString = str.split(text,sep=":")
        textString = textString.pop(0)
        #print(textString)
        textString = str.split(textString, sep=".")
        textString = textString.pop()
        #print(textString)
        #print output to console.
        if textString== str(current):
                received = "true"
        print(top+"."+middle+"."+bottom+"." + str(current) + ": " + received)
        current += 1
