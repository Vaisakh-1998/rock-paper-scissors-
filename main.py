import random
#rock paper scissor game


def win(u,c):
  #returns the winner
  #win condition r>s, s>p, p>r
  
  if u=='r' and c=='s' or u=="s" and c=="p" or u=="p" and c=="r":
    return u
  return c

def play():
  #user,computer choose from r,p,s
  user = input("\nchoose from r,p,s\nr:rock\np:paper\ns:scissor\nwhats your choice:")
  user = user.lower()
  com = random.choice("rps")
  
  #tie
  if user == com:   
    return (0,user,com)
  #user win
  elif win(user,com) == user:
    return (1,user,com)
  #computer win
  else:
    return (-1,user,com)
    
def win_streak():  
  #returns point of players and total number of play
  
  user_win = 0
  com_win = 0
  total_play = 0
  
  while True:
    #loop till user exit
    
    result,user,com = play()
    total_play += 1  
     #tie     
    if result == 0:
      print(f"\nyou and computer choose {com}, it's a tie")
   #user win
    elif result == 1:
      user_win +=1
      print(f"\nyou choose {user} and computer choose {com}, you win")
   #computer win
    else:
      com_win += 1
      print(f"\nyou choose {user} and computer choose {com}, computer win")
    
    #exit loop if user input 'y'
    exit = input("y to exit play:")
    if exit == "y":
      break
  print("________________")
  print(f"\nyou win:{user_win}\ncomputer win:{com_win}\ntotal play:{total_play}")
  
if __name__ == "__main__":
  win_streak()
