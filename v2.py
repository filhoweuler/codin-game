import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def euclidean(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)
        
num_sites = int(input())
sites = {}
for i in range(num_sites):
    site_id, x, y, radius = [int(j) for j in input().split()]
    sites[site_id] = {'x': x, 'y': y, 'r': radius}

built = [False, False, False]

building_queue = ["BUILD {} BARRACKS-KNIGHT", "BUILD {} TOWER","BUILD {} TOWER"]

knight = 0

c_id = 0

distances = []

# game loop
while True:
    owner_sites = []
    # touched_site: -1 if none
    gold, touched_site = [int(i) for i in input().split()]
    for i in range(num_sites):
        # ignore_1: used in future leagues
        # ignore_2: used in future leagues
        # structure_type: -1 = No structure, 2 = Barracks
        # owner: -1 = No structure, 0 = Friendly, 1 = Enemy
        site_id, ignore_1, ignore_2, structure_type, owner, param_1, param_2 = [int(j) for j in input().split()]
        owner_sites.append(owner)
        
        
    num_units = int(input())
    for i in range(num_units):
        # unit_type: -1 = QUEEN, 0 = KNIGHT, 1 = ARCHER
        x, y, owner, unit_type, health = [int(j) for j in input().split()]
        
        if unit_type == -1 and owner == 0 and len(distances) == 0:
            min_distance = 999999
            min_site = 0
            
            for i in range(num_sites):
                distance = (euclidean(x,y,sites[i]['x'],sites[i]['y']),i)
                distances.append(distance)
    
    distances.sort()
    site_atual = distances[c_id][1]
    
    #if distances[c_id][0] > 30 + sites[site_atual]['r'] + 10:
    #    print("MOVE {} {}".format(sites[site_atual]['x'], sites[site_atual]['y']))
    #else:
    if (c_id < 3 and not built[c_id]):
        print(building_queue[c_id].format(site_atual))
        
        if "KNIGHT" in building_queue[c_id]:
            knight = site_atual
       
        if owner_sites[site_atual] == 0: 
            built[c_id] = True
            c_id += 1
    else:
        print("WAIT")
            
    print("TRAIN {}".format(knight))

