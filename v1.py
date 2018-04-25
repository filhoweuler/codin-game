''' Codigo escrito no video #1 da serie '''

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

built = False

# game loop
while True:
    # touched_site: -1 if none
    gold, touched_site = [int(i) for i in input().split()]
    for i in range(num_sites):
        # ignore_1: used in future leagues
        # ignore_2: used in future leagues
        # structure_type: -1 = No structure, 2 = Barracks
        # owner: -1 = No structure, 0 = Friendly, 1 = Enemy
        site_id, ignore_1, ignore_2, structure_type, owner, param_1, param_2 = [int(j) for j in input().split()]
        
        
    num_units = int(input())
    for i in range(num_units):
        # unit_type: -1 = QUEEN, 0 = KNIGHT, 1 = ARCHER
        x, y, owner, unit_type, health = [int(j) for j in input().split()]
        if unit_type == -1 and owner == 0:
            min_distance = 999999
            min_site = 0
            
            for i in range(num_sites):
                distance = euclidean(x,y,sites[i]['x'],sites[i]['y'])
                if distance < min_distance:
                    min_distance = distance
                    min_site = i
                    
    if min_distance > 30 + sites[min_site]['r'] + 10:
        print("MOVE {} {}".format(sites[min_site]['x'], sites[min_site]['y']))
    else:
        if (not built):
            print("BUILD {} BARRACKS-KNIGHT".format(min_site))
            build=True
        else:
            print("WAIT")
            
    print("TRAIN {}".format(min_site))

