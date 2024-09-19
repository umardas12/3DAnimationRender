import bpy

previous = bpy.data.objects[0]
for ob in bpy.data.objects[1:]:
    ob.parent = previous
    previous = ob
    
for ob in bpy.data.objects:
    print(f'Parent name {ob.name}')
    children_names = (c.name for c in ob.children)
    print("Child Names:",",".join(children_names))
    children_names = (c.name for c in ob.children_recursive)
    print("Child Names Recursive:",",".join(children_names))