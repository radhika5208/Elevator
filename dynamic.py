
while 1:
  choice=map(int,raw_input("Enter your choice:"))

  if(dp<=(max1/2)):
   for item in choice:
       item=int(item)
   choice.sort()
   print choice
   length=len(choice)
   for j in range(0,length):
       dp=choice[j]

  else:
    for item in choice:
        item=int(item)
    choice.sort(reverse=True)
    print choice
    length=len(choice)
    for j in range(0,length):

      if(choice[j]>max):
        print "WRONG INPUT...!"

      elif(choice[j]==dp):
        print "You are at same floor"

      elif(choice[j]>dp):
        tp=choice[j]-dp
        upward(dp,tp)
        dp=choice[j]

      elif (choice[j]<dp | choice[j]<=max):
        tp=dp-choice[j]
        downword(dp,tp)
        dp=choice[j]
g.cleanup()
