import bpy

previous = bpy.data.objects[0]

for ob in bpy.data.objects[1:]:
    w_mat = ob.matrix_world.copy()
    ob.parent = previous
    ob.matrix_world = w_mat
    previous = ob