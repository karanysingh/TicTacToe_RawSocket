import socket,time
HOST = '127.0.0.1'
PORT = 9090
class Tictactoe:
  def __init__(self,name,name2):
    self.user1 = name
    self.user2 = name2
    self.alt = True
    self.visited = []
    self.welcome()
    self.server_init()
    self.boardState = [[1,1,1],[1,1,1],[1,1,1]]
    # self.boardState = [["X","X","X"],[1,1,1],[1,1,1]]
    # self.boardState = [["X",1,"X"],[1,1,"X"],[1,1,"X"]]

  def server_init(self):
    self.s = socket.socket()
    self.s.bind((HOST,PORT))
    self.s.listen(5)
    self.c,self.addr = self.s.accept()

  def welcome(self):
    print(self.user1,"X vs O",self.user2)

  def board(self):
    print("Y\X",end=" ")
    for t in range(3):
      print(t,end="   ")
    p=0
    for i in self.boardState:
      print()
      if(p<3):
        print(p,end="  ")
        p=p+1
      for j in i:          
        if j==1:
          print("⬜️",end="  ") 
        elif j=="X":
          print("❎",end="  ")
        elif j=="O":
          print("🅾️",end="  ")
      print()
    
  def modifyState(self,new):
    if(new not in self.visited):
      self.visited.append(new)
      [x,y] = new
      if self.alt==True:
        self.boardState[y][x] = "X"
        self.alt = False
      elif self.alt==False:
        self.boardState[y][x] ="O"
        self.alt = True
      self.board()
      print(self.boardState)

      end = self.checkEnd()
      if(end): return True

    else:
      print("Invalid Move")

  def declareWin(self):
    print("GAME OVER")
    if self.alt==False:
      print("WINNER",self.user1) 
      return
    if self.alt==True:
      print("WINNER",self.user2)
      return

  def declareDraw(self):
      print("GAME OVER")
      print("Match Draw")
      return

  def TwoPlayer(self):
    while True:
      print("Select next move (eg., 2,2) or q to end\n")
      print(self.user1) if self.alt else print(self.user2)
      t = input()
      if(t=='q' or t=='Q'):
        print("User ended the game\n")
        break
      else:
        [a,b] = list(map(int,t.split()))
        end = game.modifyState([a,b])

        if(end): break
   
  def ServerPlay(self):
    while True:
        try:
            user = self.user1 if self.alt else self.user2 
            self.c.send(("Select next move (eg., 2,2) or q to end\n"+user).encode())
            [a,b] = list(map(int,self.c.recv(1024).decode().split()))
            end = game.modifyState([a,b])
            if(end): break 
        except Exception:
            print("error while reading from client",Exception)
            self.c,self.addr = self.s.accept()
  
      
  def checkEnd(self):
    for i in self.boardState:
      if i == ["O","O","O"] or i == ["X","X","X"]:
        self.declareWin()
        return True
        break
    for k in range(3):
      o = 0
      x = 0
      for j in range(3):
        if self.boardState[j][k] == "O":
          o+=1
        if self.boardState[j][k] == "X":
          x+=1
      if(o==3 and x==3):
        self.declareDraw()
        return True

      if(o==3 or x==3):
        print('he')
        self.declareWin()
        return True
        break
    o=0
    x=0
    for j in range(2):
      j+=1
      if self.boardState[j][j] == "O":
        o+=1
      if self.boardState[j][j] == "x":
        x+=1
      if(o==3 and x==3):
        self.declareDraw()
        return True

      if(o==3 or x==3):
        self.declareWin()
        return True
        break
    

         
game = Tictactoe("Player1","Player2")
game.ServerPlay()