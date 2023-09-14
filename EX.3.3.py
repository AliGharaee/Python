score = input('Enter Score:')
sr = float(score)
if sr>1.0 or sr<0.0 :
    print ("Error: Please Enter Correct Score")
elif sr>=0.9 :
      print ('A')
elif sr>=0.8 :
    print ('B')
elif sr>=0.7 :
    print ('C')
elif sr>=0.6 :
    print ('D')
else :
    print ('F') 
