def parser():
    with open("inputday8.txt","r") as f:
        # set up 2D grid
        #grid = [line.split(",") for line in f.readlines()]
        # gives string list
        #grid = [list( map(int,i) ) for i in grid] 
        #grid = list(map(grid,f.readlines()))
        grid = list(map(lambda n: [int(x) for x in list(n.strip())], f.readlines()))
    return grid


def parta():
    grid = parser()
    # visible on edge
    visible = 0
    visible += len(grid)*2
    visible += len(grid[0])*2 -4
    print(visible)
    # row
    for i in range(1, len(grid)):

        # 2, 5, 5, 3, 4, 5
        #sorted(grid)
        #column

        for j in range(1, len(grid[i])):
            #print(grid[i][j])
            pass
    DIR = [(-1,0), (0,1), (1,0), (0,-1)]
    R = len(grid)
    C = len(grid[0])
    #print(R,C)
    ans = 0
    for r in range(R):
        for c in range(C):
            vis = False
            for (dr, dc) in DIR:
                rr = r
                cc = c
                ok = True
                while True:
                    rr += dr
                    cc += dc
                    if not (0<=rr<R and 0<=cc<C):
                        break
                    if grid[rr][cc] >= grid[r][c]:
                        ok = False
                if ok:
                    vis = True
            if vis:
                ans += 1
    print(ans)
    grid = parser()
    best = 0
    DIR = [(-1,0), (0,1), (1,0), (0,-1)]
    R = len(grid)
    C = len(grid[0])    
    for r in range(R):
        for c in range(C):
            score = 1 
            for (dr, dc) in DIR:
                dist = 1
                rr = r+dr
                cc = c+dc
                while True:
                    if not (0<=rr<R and 0<=cc<C):
                        dist -= 1
                        break
                    if grid[rr][cc] >=grid[r][c]:
                        break
                    dist +=1
                    rr += dr
                    cc += dc
                score *= dist
            print(r,c, dist, score)
            best = max(best,score)               
    print(best)        

parta()