import random

l = int(input("\n\t\t\tEnter your lower number \n"))

la = int(input("\t\t\tEnter your larger number \n"))

rand = random.randint(l, la)

n = None
count = int(0)
while n!= rand:
   rand = random.randint(l, la)
   count+=1
   n = input("\t\tEnter your number \n\n")
   n = int(n)
   if rand == n:
       print("\t\t\tYou win!!!")
       print(f'\t\t\tYou comple this game in {count} steps...\n\n')
   else:
       print("\tTry next one....")
       print(f'{rand} ')


input('Press ENTER for exit....')
   
