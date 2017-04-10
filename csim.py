# Last Edited: Finished the core system including the display arrangement
# Next Plan: - Restrict user input
#            - Infinite time itteration without the needs to re-run the program

#          Sleep well, love your body
#                       -anonymous-

from random import randint
file = open('out.txt','w')
#------------------------------------------------------------------------------

def address(_addSize, _maxFrame, _policy, _inputType):
    len_frame = _maxFrame
    policy = _policy
    
    if(_inputType==1):    
        stack=[]
        stack=randomInput(_addSize)
    elif(_inputType==0):
        stack=userInput(_addSize)

    if(policy==1):
        FIFO(len_frame, stack)
    elif(policy==2):
        LRU(len_frame, stack)    

#------------------------------------------------------------------------------    
    
def randomInput(_addSize):
    min=0
    max=6
    add_size = _addSize
    stack = []
    for i in range(add_size):
        stack.append(randint(min,max))
    return stack
    
#------------------------------------------------------------------------------    

def userInput(_addSize):
    add_size = _addSize
    stack = []
#---- ways, input then enter until reach last file
#    print("Enter numbers in array: ")
#    for i in range(add_size):
#        n = input("num: ")
#        stack.append(int(n))
        
#---- ways, input separate with space
    
    #print("Enter numbers in array: ")
    #n = input("num: ")
    #n = [int(i) for i in n.split()]
    #stack = n    
    print('Please enter', add_size,'number (without space):')
    n = input('enter:')
    while len(n) != add_size or (not n.isdigit()):
        print('Please enter', add_size,'number (without space):')
        n = input('enter:')
    str_n = str(n)
    for i in range(add_size):
        stack.append(int(str_n[i]))
    
    print ('The final number is:', stack)
    
#---- restrict to certain length || NOT SUCCESS
#    import re
#    
#    input_str = input("Enter: ")
#    if not re.match("[0-9]", input_str):
#        print("Error! Only numbers allowed!")
#        userInput(_addSize)
#    elif len(input_str) > add_size:
#        print("Error! Only", add_size, "characters allowed!")
#        userInput(_addSize)
#    stack = input_str
    
    return stack
    
#------------------------------------------------------------------------------    

def FIFO(max_frame, stack):
    s = stack   
    c = max_frame-1
    hit = 0
    total = len(stack)
    frame = []           
    
    print("\n------FIFO Policy-------\n")
    
    print(' add',end='  ')
    for i in range(c+1):
        print("", i, end="  ")
    print('hit')

    file.write("\nadd  ")
    for i in range(max_frame):
        file.write(" %s  "%str(i))
    file.write('hit\n')
    
    #put stack in frame if frame is NOT full
    while(len(frame) < max_frame):
        l = len(frame)
        sisa=max_frame-(len(frame)+2)
        cur_add = s[0]
        if(s[0] == s[0] in frame):      
            l-=1
            print(" ",cur_add,"||", end='')
            for i in range(l,-1,-1):
                print("",frame[i],end=" |")
            print("   |"*(sisa+2),end='')
            print(" * ")
            
            file.write(" %s ||"%cur_add)
            for i in range(l,-1,-1):
                file.write(" %s |"%str(frame[i]))
            file.write("   |"*(sisa+2))
            file.write(" *")
            file.write("\n")
            
            hit+=1
            s.pop(0)
        else:
            frame.append(s.pop(0))
            #print(" "*3*sisa, frame, "  ||", cur_add)
            print(" ",cur_add,"||", end='')
            for i in range(l,-1,-1):
                print("",frame[i],end=" |")
            print("   |"*(sisa+1),end='')
            print('')
            
            file.write(" %s ||"%cur_add)
            for i in range(l,-1,-1):
                file.write(" %s |"%str(frame[i]))
            file.write("   |"*(sisa+1))            
            file.write("\n")
            
    
    #if full, take out frame(0), then append 
    while( (len(frame) == max_frame) and (len(s)!=0) ):
        cur_add = s[0]
        if(s[0] == s[0] in frame):
            #print("",frame, "* ||", cur_add)
            print(" ",cur_add,"||", end='')
            for i in range(c,-1,-1):
                print("",frame[i],end=" |")
            print(" * ")
            
#            file.write("    %s "%' || '.join(str(i) for i in frame))
#            file.write("*")
#            file.write(" || %s"%cur_add)
#            file.write("\n")
            
            file.write(" %s ||"%cur_add)
            for i in range(l,-1,-1):
                file.write(" %s |"%str(frame[i]))
            file.write(" *")
            file.write("\n")
            
            hit+=1
            s.pop(0)
        else:
            frame.pop(0)
            frame.append(s.pop(0))
            
            #print("",frame, "  ||",cur_add)
            print(" ",cur_add,"||", end='')            
            for i in range(c,-1,-1):
                print("",frame[i],end=" |")
            print('')
            
#            file.write("    %s "%' || '.join(str(i) for i in frame))
#            file.write("  || %s"%cur_add)
#            file.write("\n")
            
            file.write(" %s ||"%cur_add)
            for i in range(l,-1,-1):
                file.write(" %s |"%str(frame[i]))
            file.write("\n")
            
    hitPrint(total, hit)

    #WRITE-end
    file.close()
#------------------------------------------------------------------------------        
         
def LRU(max_frame, stack):
    s = stack
    c = max_frame-1
    total = len(stack)
    
    hit = 0
    frame = []    

    print("\n-------LRU Policy-------\n") 
    
    print(' add',end='  ')
    for i in range(c+1):
        print("", i, end="  ")
    print('hit')            
    
    file.write("\nadd  ")
    for i in range(max_frame):
        file.write(" %s  "%str(i))
    file.write('hit\n')
    
    #put stack in frame if frame is NOT full
    while(len(frame) < max_frame):
        l = len(frame)
        cur_add = s[0]
        sisa=max_frame-(len(frame)+1)
        if(s[0] == s[0] in frame):
            l-=1            
            loc = frame.index(s[0]) 
            frame.append(frame.pop(loc)) #pop the hit number, then push to the beginning
            print(" ",cur_add,"||", end='')
            for i in range(l,-1,-1):
                print("",frame[i],end=" |")
            print("   |"*(sisa+1),end='')
            print(" * ")
            
#            file.write(" "*4*(sisa+2))
#            file.write("%s "%' | '.join(str(i) for i in frame))
#            file.write("*\n")
            
            file.write(" %s ||"%cur_add)
            for i in range(l,-1,-1):
                file.write(" %s |"%str(frame[i]))
            file.write("   |"*(sisa+1))
            file.write(" *")
            file.write("\n")
            
            hit+=1
            s.pop(0)
        else:
            frame.append(s.pop(0))
            #print(" "*3*sisa, frame)
            print(" ",cur_add,"||", end='')
            for i in range(l,-1,-1):
                print("",frame[i],end=" |")
            print("   |"*(sisa),end='')
            print('')            
            
#            file.write(" "*4*(sisa+1))
#            file.write("%s \n"%' | '.join(str(i) for i in frame))
            file.write(" %s ||"%cur_add)
            for i in range(l,-1,-1):
                file.write(" %s |"%str(frame[i]))
            file.write("   |"*(sisa))            
            file.write("\n")
            
     #if full, take out frame(0), then append 
    while( (len(frame) == max_frame) and (len(s)!=0) ):
        cur_add = s[0]        
        if(s[0] == s[0] in frame):
            #pop hit, put to the entrance(frame[max_frame])
            loc = frame.index(s[0])
            frame.append(frame.pop(loc))
            #print("",frame, "*")
            print(" ",cur_add,"||", end='')
            for i in range(c,-1,-1):
                print("",frame[i],end=" |")
            print(" * ")
            
#            file.write("    %s "%' | '.join(str(i) for i in frame))
#            file.write("*\n")
            file.write(" %s ||"%cur_add)
            for i in range(l,-1,-1):
                file.write(" %s |"%str(frame[i]))
            file.write(" *")
            file.write("\n")
            
            hit+=1
            s.pop(0)
        else:
            frame.pop(0)
            frame.append(s.pop(0))
            
            #print("",frame)
            print(" ",cur_add,"||", end='')            
            for i in range(c,-1,-1):
                print("",frame[i],end=" |")
            print('')
            
            #file.write("    %s \n"%' | '.join(str(i) for i in frame))
            file.write(" %s ||"%cur_add)
            for i in range(l,-1,-1):
                file.write(" %s |"%str(frame[i]))
            file.write("\n")
            
    hitPrint(total, hit)            

    #WRITE-end
    file.close()
#------------------------------------------------------------------------------
       
def hitPrint(_total,_hit):
    total = _total
    hit = _hit

    hit_ratio=hit/total*100
    hr_round=round(hit_ratio, 2)
    
    print("\nmiss:", total - hit)
    file.write("\nmiss: %s \n"% str(total - hit))
    
    print("hit :", hit)
    file.write("hit : %s \n"% str(hit))
    
    print("hit percentage:","%.2f" % hit_ratio, "%")
    file.write("hit percentage: %s "% str(hr_round))
    file.write("%")
       
#------------------------------------------------------------------------------
def execute(_addSize, _maxFrame, _policy, _inputType):
    add_size = _addSize
    max_frame = _maxFrame
    policy = _policy
    input_type = _inputType
    
    #WRITE-start
#    file = open('out.txt','w')
    
    file.write("address size: %s\n"% add_size)
    file.write("frame size  : %s\n"% max_frame)
    if(policy==1):
        file.write("policy      : FIFO\n")
    elif(policy==2):
        file.write("policy      : LRU\n")

        
    address(add_size, max_frame, policy, input_type)
    
    
#------------------------------------------------------------------------------

def main():
    print("\n-------------------  WELCOME  ----------------------") 
    print("to start please write with the following format:\n")    
    print("   execute(addSize, frameSize, policy, autoGenerate)")
    print("   where,")
    print("   - addSize   : size of address")
    print("   - frameSize : size of frame")
    print("   - policy    : 1 for FIFO, 2 for LRU")
    print("   - autoGenerate: 1 for yes, 0 for no")
    print("\nInput example: execute(10, 3, 1, 1)\n")
    
main()

#------------------------------------------------------------------------------