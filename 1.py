nrow = int(input())
ncol= int(input())
maze=[]
maze.append('+' * (ncol + 2))
for k in range(nrow):
    maze.append('+' + input() + '+')
maze.append('+' * (ncol + 2))

def step(x,y,prevx,prevy):
    if prevx + 1 == x:
        prevx += 1
        if maze[y-1][x]=='+':
            y -= 1
        elif maze[y][x+1]=='+':
            x += 1
        elif maze[y+1][x]=='+':
            y += 1
        else:
            x -= 1
    elif prevx - 1 == x:
        prevx -= 1
        if maze[y+1][x]=='+':
            y += 1
        elif maze[y][x-1]=='+':
            x -= 1
        elif maze[y-1][x]=='+':
            y -= 1
        else:
            x += 1
    elif prevy + 1 == y:
        prevy += 1
        if maze[y][x+1]=='+':
            x += 1
        elif maze[y+1][x]=='+':
            y += 1
        elif maze[y][x-1]=='+':
            x -= 1
        else:
            y -= 1
    elif prevy - 1 == y:
        prevy -= 1
        if maze[y][x-1]=='+':
            x -= 1
        elif maze[y-1][x]=='+':
            y -= 1
        elif maze[y][x+1]=='+':
            x += 1
        else:
            y += 1
    return (x, y, prevx, prevy)

x = int(input()) + 1
y = int(input()) + 1

intx=x
inty=y

if x==1:
    prevx = 0 
    prevy = y
if y==1:
    prevx = x
    prevy = 0
if x==ncol:
    prevx = ncol + 1
    prevy = y
if y==nrow:
    prevx = x
    prevy = nrow + 1

count = 0
while x < ncol+1 and x > 0 and y < nrow+1 and y > 0:
    x, y, prevx, prevy = step(x,y,prevx,prevy)
    count += 1

if intx == prevx and inty == prevy:
    print('impossible')
else:
    print(count)
    
