# loop = int(input())
#
# for i in range(loop):
#   num = int(input())
#   sum = 0
#   while num > 0:
#     d = num % 10;
#     num = num//10;
#     sum= sum+d
#
#   print(sum)
# from Tools.scripts.treesync import raw_input

# loop = int(input())
#
# remainder = []
#
# for i in range(loop):
#   itemToAdd = int(input())
#   a, b = itemToAdd.split()
#   remainder = a%b;
#   remainder.append(remainder)
#
# for result in remainder:
#   print(result)

# print(100 % 200)

# remainder  = []
# itemToAdd = int(input())
# a, b = itemToAdd.split( )
# remainder = a%b;
# remainder.append(remainder)

# t=int(input())
# while t > 0:
#     m=int(input())
#     res=0
#     while m > 0:
#         l=input() #take input as string
#         l,d=l.split() #split input
#         l=int(l)
#         d=int(d)
#         print(l)
#         print(d)



# for x in range(len(b)):
#
#   b[x]=int(b[x])

#print(b)

# loop = int(input())
# remainder =[]
# for i in range(loop):
#   a = input()
#   b, c = a.split()
#   #print(b, c)
#   remainderA = int(b) % int(c);
#   remainder.append(remainderA)
#
# for i in remainder:
#   print(i)

# number = int(input())
# print(number)

loop = int(input())
win = 1; #player 1 wins
player1score = []
player2score = []
diffOf2players =[]

for i in range(loop):
  a = input()
  b,c = a.split()
  b=int(b)
  c=int(c)
  if(b>c):
    out= b-c;
    player1score.append(b)
    diffOf2players.append(out)
    win =1
  else:
    out=c-b;
    player2score.append(c)
    diffOf2players.append(out)
    win=2;
# if(max(player1score)>max(player2score)):
#   print("1"+ " "+str(max(player1score)))
#
# else:
#   print("2"+ " "+ str(max(player2score)))

for i in range(len(diffOf2players)-1):
  #print(diffOf2players(i))
  index = diffOf2players.index(max(diffOf2players))
  print(index)
  print(player1score[index])

