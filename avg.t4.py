n=int(input('enter the number of student:'))


sum=0

score =[]
for i in range(n):
  score.append(float(input('enter number programming:')))
  score.sort()
  min=score[0]
  max=score[i]  
  sum=sum+score[i]  
  avg=sum/n
  

print('min=',min,'max=',max,'avg=',avg) 




