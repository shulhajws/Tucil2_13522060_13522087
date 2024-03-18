'''
    * Summary of File: 
    * 
    *   Program to display the Bezier Curve of any degree
    *   Using De Castlejau's algorithm to display the curve
    * Compilation Command : python bezier.pyw
'''

#!/usr/bin/python

import tkinter as tk

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800

# Initializing X coordinate, Y coordinate, and storing indices of control point arrays
Px = []
Py = []
cpoints = []

# Initializing array to delete path when canvas gets updated
del_arr = []

# Initialize Control Polygon Array
c_polygon = []

# Initializing variables to store X and Y coordinates for the centre of a control point
global x, y

# Function that defines De Castlejau's algorithm
def de_castlejau(P, u):
    Temp = P[:]
    n = len(Temp)

    for k in range(1, n):
        for i in range(0, n - 1 - k + 1):
            Temp[i] = (1 - u)*Temp[i] + u*Temp[i + 1]
    return Temp[0]

# Function that draws and stores a control point and deletes a control point if clicked
def drawOval(event):
      x = event.x
      y = event.y

      if cpoints:
            global i
            for i in range(len(Px)):
                  # Checks if the point clicked is inside the control point/square
                  is_event_inside_x_coords = event.x > (Px[i] - 10) and event.x < (Px[i] + 10)
                  is_event_inside_y_coords = event.y > (Py[i] - 10) and event.y < (Py[i] + 10)
                  if ( is_event_inside_x_coords and is_event_inside_y_coords):
                        C.delete(cpoints[i])
                        del cpoints[i]
                        del Px[i]
                        del Py[i]
                        return          
      
      # Draws a circle inside a square of side length 20 with centre (x, y)
      cp = (C.create_oval(x - 10, y - 10, x + 10, y + 10))
      cpoints.append(cp)        
      Px.append(x)
      Py.append(y)

# Function that inserts new control point when right mouse button is released
def moveOval(event):
      x = event.x
      y = event.y
      cp = (C.create_oval(x - 10, y - 10, x + 10, y + 10))      
      cpoints.insert(i, cp)          
      Px.insert(i, x)
      Py.insert(i, y)

      C.delete(c_polygon[i-1], c_polygon[i])
      del c_polygon[i-1], c_polygon[i]

# Function that draws the curve when updated
def drawCurve(event):
    k = 0
    if del_arr:
      for i in range(len(del_arr)):
            C.delete(del_arr[i])
    if c_polygon:
      for i in range(len(c_polygon)):
            C.delete(c_polygon[i])

    while k < 1:
        k += 0.001
        x = de_castlejau(Px, k)
        y = de_castlejau(Py, k)
        point = C.create_oval(x - 1, y - 1, x + 1, y + 1)
        del_arr.append(point)

    #c_polygon = []
    for x in range(len(cpoints) - 1):
          cpol = C.create_line(Px[x], Py[x], Px[x + 1], Py[x + 1], fill = "light gray")  
          c_polygon.append(cpol)  

    
# Main function   
if __name__ == '__main__':
    top = tk.Tk()
    C = tk.Canvas(top, bg="white", height=CANVAS_HEIGHT, width=CANVAS_WIDTH)
    C.pack()
    # Button 1 - Left mouse button, Button 2 - Right mouse button
    top.bind("<Button 1>", drawOval)
    top.bind("<Button 1>", drawCurve, add="+")
    top.bind("<Button 2>", drawOval)
    top.bind("<ButtonRelease-2>", moveOval)
    top.bind("<ButtonRelease-2>", drawCurve, add="+")
    message = tk.Label(top, text = "Bezier Curve Drawer")
    message.pack(side = tk.BOTTOM)
    top.mainloop()