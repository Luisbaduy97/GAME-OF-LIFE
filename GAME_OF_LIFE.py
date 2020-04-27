import numpy as np
import matplotlib.pyplot as plt
import time
import matplotlib.animation as animation

plt.close()
fig = plt.figure()

xC = 50
yC = 50

game = np.zeros((xC,yC))


game[25,20] = 1
game[26,20] = 1
game[27,20] = 1
game[27,21] = 1
game[27,22] = 1
game[28,22] = 1
game[28,22] = 1
game[29,22] = 1
game[29,23] = 1
# game[25,29] = 1







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
            n_neigh = game[(j-1)%xC, (i-1)%yC] + \
                      game[(j)%xC, (i-1)%yC] + \
                      game[(j+1)%xC, (i-1)%yC] + \
                      game[(j-1)%xC, (i)%yC] + \
                      game[(j+1)%xC, (i)%yC] + \
                      game[(j-1)%xC, (i+1)%yC] + \
                      game[(j)%xC, (i+1)%yC] + \
                      game[(j+1)%xC, (i+1)%yC]
            # time.sleep(0.01)
            # print(i,j, n_neigh)
            #regla 1
            if game[j,i] == 1 and n_neigh < 2:
                newGame[j,i] = 0
            elif game[j,i] == 1 and (n_neigh == 2 or n_neigh == 3):
                newGame[j,i] = 1
            elif game[j, i] == 1 and n_neigh > 3: #Dead cell with exactly three live neighbours becamos a live cell
                newGame[j,i] = 0
            elif game[j,i] == 0 and n_neigh == 3:
                newGame[j,i] = 1

    game = np.copy(newGame)
    im = plt.imshow(newGame, 'gray',animated=True)
    ims.append([im])
    #time.sleep(5)
    #plt.figure(2)
    #plt.imshow(newGame, 'gray')
ani = animation.ArtistAnimation(fig, ims, interval=200, blit=True,
                                repeat_delay=500)

plt.show()
    
    
    
    
    
    
    
    