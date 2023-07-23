
import numpy as np

# Unit spacing for each row in x direction. Physical position, not electrical
# grid position
spacing_x = [[0, 1, 1.25, 1, 1, 1], 
             [0, 1, 1.25, 1, 1, 1],
             [0, 1, 1.25, 1, 1],
             [5.25],
             [0, 1, 1.25, 1, 1],
             [0, 1, 1.25, 1, 1],
             [5.25],
             [0, 1, 1.75, 1.5]]

# Unit spacing for each row in y direction
spacing_y = [0, 1.5, 1, 0.5, 0.5, 1, 0.5, 0.5]

xy = []
base_spacing_mm = 19

# Calculate position in mm
ysum = 0
xsum = 0
for i, y in enumerate(spacing_y):
    ysum += y*base_spacing_mm
    for x in spacing_x[i]:
        xsum += x*base_spacing_mm
        xy.append([xsum, ysum])
    xsum = 0

print(xy)

# Scale to 0->224 for x and 0->64 for y
xy = np.array(xy)
max_x = np.max(xy[:, 0])
max_y = np.max(xy[:, 1])

xy[:, 0] = np.round(xy[:, 0]*224/max_x)
xy[:, 1] = np.round(xy[:, 1]*64/max_y)

#  Format for C
for i, point in enumerate(xy.astype(int)):
    if i%6 == 0 and i != 0:
        print('')
    print(f"{{{point[0]:3d}, {point[1]:3d}}}, ", end='')