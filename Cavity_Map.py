import sys
maps=[] #2D Array of the input
answers=[] # used later to store valid cavities found
n=int(input())
for line in range(n): #read in input
    ondeck=[]
    x=str(input())
    for item in x:
        ondeck.append(int(item))
    maps.append(ondeck)

#time to find cavities
moves=[(-1,0),(0,1),(1,0),(0,-1)] #this is a bank of valid moves can me modifief to allow diagnol
counter=1
for i in range(n):
    for j in range(n): #iterates over all "nodes" in the 2D Array representing named maps
        score=0
        current=maps[i][j] #current represents the current node you are own
        for move in moves: # attempts all moves in the moves bank
                    a,b=move
        
                    try:
                        neighbor=maps[i+a][j+b] #by adding all moves in the move bank you create all possible neighbores
                        
                        if current>neighbor:
                            score+=1
                            
                    except: #in the event you go out of bounds with an index error, which you will it is safe to assume that current node is greater than nothing
                        score+=1
       

        counter+=1
        if score==4: #the definition of a cavity is when a value is greater than all the values above,below,to the left, and to the right of it
            answers.append((i,j))
        
for answer in answers: #have to find if an answer is a edge
    a,b=answer
    if (a==0 or b==0 or a==n-1 or b==n-1): #I realized around here I could have saved some work by nothing bothering to calculate if a vertex was a cavity since if any of its coordinates occur on the edges, it is automatically disqualified 
        pass
    else:
        maps[a][b]="X"
for line in maps: #iterate over maps and join them together for a nice clean picture
    line=map(str,line)
    print("".join(line))
    
    #overall not very efficient but gets the job done
