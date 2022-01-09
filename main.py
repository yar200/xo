
import turtle
screen=turtle.Screen()
screen.setup(500,500)
screen.title('Tic Tac Toe')
screen.setworldcoordinates(-5,-5,5,5)
screen.tracer(0)
turtle.hideturtle()

def drawBoard():
  turtle.tracer(0)
  turtle.pencolor('red')
  turtle.pensize(10)
  turtle.up()
  turtle.goto(-3,-1)
  turtle.seth(0)
  turtle.down()
  turtle.fd(6)
  turtle.up()
  turtle.goto(-3,1)
  turtle.seth(0)
  turtle.down()
  turtle.fd(6)
  turtle.up()
  turtle.goto(-1,-3)
  turtle.seth(90)
  turtle.down()
  turtle.fd(6)
  turtle.up()
  turtle.goto(1,-3)
  turtle.seth(90)
  turtle.down()
  turtle.fd(6)

def drawcircle(x,y):
  turtle.up()
  turtle.goto(x, y - 0.75)
  turtle.seth(0)
  turtle.color('pink')
  turtle.down()
  turtle.circle(0.75,steps=100)


def drawx(x,y):
  turtle.color('purple')
  turtle.up()
  turtle.goto(x-0.75,y-0.75)
  turtle.down()
  turtle.goto(x+0.75,y+0.75)
  turtle.up()
  turtle.goto(x-0.75,y+0.75)
  turtle.down()
  turtle.goto(x+0.75,y-0.75)

def drawPiece(i,j,p):
  if p==0: return
  x, y=2*(j-1),-2*(i-1)
  if p==1:
    drawx(x,y)

  else:
    drawcircle(x,y)

def draw(b):
  drawBoard()
  for i in range(3):
    for j in range(3):
      drawPiece(i,j,b[i][j])
  screen.update()


def gameOver(b):
  if b[0][0]>0 and b[0][0]==b[0][1] and b[0][1]==b[0][2]: return b[0][0]
  if b[1][0]>0 and b[1][0]==b[1][1] and b[1][1]==b[1][2]:return  b[1][0]
  if b[2][0]>0 and b[2][0]==b[2][1] and b[2][1]==b[2][2]:return  b[2][0]

  if b[0][0]>0 and b[0][0]==b[1][0] and b[1][0]==b[2][0]: return b[0][0]
  if b[0][1]>0 and b[0][1]==b[1][1] and b[1][1]==b[2][1]:return  b[0][1]
  if b[0][2]>0 and b[0][2]==b[1][2] and b[1][2]==b[2][2]:return  b[0][2]

  if b[0][0]>0 and b[0][0]==b[1][1] and b[1][1]==b[2][2]:return  b[0][0]
  if b[2][0]>0 and b[2][0]==b[1][1] and b[1][1]==b[0][2]:return  b[2][0]

  pieces=0

  for i in range(3):
    for j in range(3):
      pieces+=(1 if b[i][j]>0 else 0)
  if pieces==9:
    return 3
  else:
    return 0



def play(x,y):
  global turn
  global b

  i=3-int(y+5)//2
  j=int(x+5)//2 - 1

  if i>2 or j>2 or i<0 or j<0 or b[i][j]!=0:return

  if turn=='x':
    b[i][j], turn=1,'o'
  else:
    b[i][j], turn=2,'x'


  draw(b)

  result=gameOver(b)

  if result==1:
    if screen.textinput('Game overrr','x won! do you want to play one more time?'):
      screen.clear()
      b=[[0,0,0],[0,0,0],[0,0,0]]
      drawBoard()
      start(b)
    else:
      exit()

  elif result==2:
    if screen.textinput('Game overrr','o won! do you want to play one more time?'):
      screen.clear()
      b=[[0,0,0],[0,0,0],[0,0,0]]
      drawBoard()
      start(b)
    else:
      exit()
  elif result==3:
    if screen.textinput('Game overrr','it is tieee! do you want to play one more time?'):
      screen.clear()
      b=[[0,0,0],[0,0,0],[0,0,0]]
      drawBoard()
      start(b)
    else:
      exit()



def start(board):
  draw(board)
  turn='x'
  screen.onclick(play)
  turtle.mainloop()


b=[[0,0,0],[0,0,0],[0,0,0]]
turn='x'
start(b)










