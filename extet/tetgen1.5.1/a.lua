-- Lua script.
p=tetview:new()
p:load_mesh("D:/Google Drive/Projects/Tunable Composites [w. SSYS]/extet/examples/voronoi/voronoi.1.ele")
rnd=glvCreate(0, 0, 500, 500, "TetView")
p:plot(rnd)
glvWait()
