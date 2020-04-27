import numpy as np
import matplotlib.pyplot as plt
import time

plt.close()

xC = 5
yC = 5

game = np.zeros((xC,yC))


game[1,3] = 1
game[2,3] = 1
game[3,3] = 1
game[4,3] = 1
game[1,4] = 1
game[2,4] = 1
game[3,4] = 1
game[4,4] = 1


newGame = np.copy(game)
plt.figure(1)
plt.imshow(game, 'gray')        
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
plt.figure(2)
plt.imshow(newGame, 'gray')

###
# epoch = 3
# n = 0
# while n<epoch:
#     n = n + 1
#     print(n)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    