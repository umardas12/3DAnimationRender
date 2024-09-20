
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
from copy import copy
from bpy.props import BoolProperty

class OBJECT_OT_elevator(bpy.types.Operator):
    bl_idname = "object.pckt_floor_transform"
    bl_label = "Elevator Objects"
    bl_options = {'REGISTER','UNDO'}
    floor: FloatProperty(name="Floor", default=0)
    constr: BoolProperty(name="Constraints", default=False)
    reuse: BoolProperty(name="Reuse Constraints", default=True)

    @classmethod
    def poll(cls,context):
        return len(bpy.context.selected_objects)>0
    
    def get_constraint(self,ob,constr_type,reuse=True):
        if reuse:
            for constr in ob.constraints:
                if constr.type == constr_type:
                    return constr
                return ob.constraints.new(constr_type)
    def ancestors_count(self,ob):
        ancestors = 0
        while ob.parent:
            ancestors += 1
            ob = ob.parent
        return ancestors
    
    def execute(self,context):
        if self.constr:
            for ob in context.selected_objects:
                #limit = ob.constraints.new('LIMIT_LOCATION')
                limit = self.get_constraint(ob,'LIMIT_LOCATION',self.reuse)
                limit.use_min_z = True
                limit.min_z = self.floor
            return {'FINISHED'}
        selected_objects = copy(context.selected_objects)
        selected_objects.sort(key = self.ancestors_count)
        for ob in context.selected_objects:
            matrix_world = ob.matrix_world
            #if ob.location.z > self.floor:
            if matrix_world[2][3] > self.floor:
                continue
            #ob.location.z =self.floor
            matrix_world[2][3] = self.floor
            context.view_layer.update()
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