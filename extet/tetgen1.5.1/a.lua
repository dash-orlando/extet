-- Lua script.
p=tetview:new()
p:load_mesh("D:/Google Drive/Tools/HoudiniX.X/otls/extet/output/temp_out.1.ele")
rnd=glvCreate(0, 0, 500, 500, "TetView")
p:plot(rnd)
glvWait()
