import numpy as np
import matplotlib.pyplot as plt
import time
import matplotlib.animation as animation


fig = plt.figure()

xC = 20
yC = 20

game = np.zeros((xC,yC))


game[1,3] = 1
game[2,3] = 1
game[3,3] = 1
game[4,3] = 1
game[1,4] = 1
game[2,5] = 1
game[3,4] = 1
game[4,4] = 1

game[10,10] = 1
game[11,10] = 1
game[12,10] = 1
game[10,11] = 1
game[10,12] = 1

game[15,11] = 1
game[15,12] = 1
game[15,13] = 1
game[15,14] = 1
game[16,14] = 1
game[17,14] = 1
game[18,15] = 1
game[18,16] = 1
game[18,17] = 1
game[18,18] = 1

im = plt.imshow(game, 'gray',animated=True)
ims = []
ims.append([im])
newGame = np.copy(game)
#plt.figure(1)
#plt.imshow(game, 'gray')

epoch = 100
n=0
while n<epoch:
    n=n+1
    print(n)       
    for i in range(xC):
        for j in range(yC):
            n_neigh = game[(j-1) % xC, (i-1) % yC] + \
                      game[(j) % xC, (i-1) % yC] + \
                      game[(j+1) % xC, (i-1) % yC] + \
                      game[(j-1) % xC, (i) % yC] + \
                      game[(j+1) % xC, (i) % yC] + \
                      game[(j-1) % xC, (i+1) % yC] + \
                      game[(j) % xC, (i+1) % yC] + \
                      game[(j+1) % xC, (i+1) % yC]
            # time.sleep(0.01)
            # print(i,j, n_neigh)
            #regla 1
            if game[j, i] == 0 and n_neigh == 3:
                newGame[j,i] = 1
            elif game[j,i] == 1 and (n_neigh < 2 or n_neigh > 3):
                newGame[j,i] = 0
    game = newGame
    im = plt.imshow(game, 'gray',animated=True)
    ims.append([im])
    #time.sleep(5)
    #plt.figure(2)
    #plt.imshow(newGame, 'gray')
ani = animation.ArtistAnimation(fig, ims, interval=500, blit=True,
                                repeat_delay=1000)

plt.show()

###
# epoch = 3
# n = 0
# while n<epoch:
#     n = n + 1
#     print(n)


    
    
    
    
    
    
    
    