players = [2,4,6,3,76,45,234]
print(players[2])
print(players[-1])
print(players[2:])
print(players[:3])
players[:2] = [0]
print(players)
players[4:5] = [0]
print(players)
players[4:6] = [0]
print(players)
players.append([1,2])
print(players)
players += [3,4]
print(players)
players.append(123,4)
print(players)
players = []
print(players) 
