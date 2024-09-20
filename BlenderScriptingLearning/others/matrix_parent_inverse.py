import bpy

previous = bpy.data.objects[0]

for ob in bpy.data.objects[1:]:
    ob.parent=previous
    offset_matrix = previous.matrix_world.inverted()
    ob.matrix_parent_inverse = offset_matrix
    previous = ob
    