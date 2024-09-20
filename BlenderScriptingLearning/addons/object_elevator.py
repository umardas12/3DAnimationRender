
bl_info = {
    "name": "Elevator",
    "author": "John Doe",
    "version": (1,0),
    "blender": (4,1,1),
    "description": "Move Objects up to a minimum height",
    "category": "Object"
}

import bpy
from bpy.props import FloatProperty

class OBJECT_OT_elevator(bpy.types.Operator):
    bl_idname = "object.pckt_floor_transform"
    bl_label = "Elevator Objects"
    bl_options = {'REGISTER','UNDO'}
    floor: FloatProperty(name="Floor", default=0)

    @classmethod
    def poll(cls,context):
        return len(bpy.context.selected_objects)>0
    
    def execute(self,context):
        for ob in context.selected_objects:
            if ob.location.z > self.floor:
                continue
            ob.location.z =self.floor
        return {'FINISHED'}
    
def draw_elevator_item(self,context):
    row = self.layout.row()
    row.operator(OBJECT_OT_elevator.bl_idname)

def register():
    bpy.utils.register_class(OBJECT_OT_elevator)
    object_menu = bpy.types.VIEW3D_MT_object_context_menu
    object_menu.append(draw_elevator_item)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_elevator)
    object_menu = bpy.types.VIEW3D_MT_object_context_menu
    object_menu.remove(draw_elevator_item)