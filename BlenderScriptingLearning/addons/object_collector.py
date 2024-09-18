
bl_info = {
    "name": "Collector",
    "author": "John Doe",
    "version": (1, 0),
    "blender": (3, 00, 0),
    "description": "Create collections for object types",
    "category": "Object",
}

import bpy

class OBJECT_OT_collector_types(bpy.types.Operator):
    """Create Collection Based on Objects Types."""
    bl_idname = "object.pckt_type_collector"
    bl_label = "Create Type Collections"
    @classmethod
    def poll(cls,context):
        return len(context.scene.objects)>0
    
    def execute(self,context):
        mesh_cl = bpy.data.collections.new("MESH")
        light_cl = bpy.data.collections.new("LIGHT")
        camera_cl = bpy.data.collections.new("CAMERA")
        context.scene.collection.children.link(mesh_cl)
        context.scene.collection.children.link(light_cl)
        context.scene.collection.children.link(camera_cl)
        for ob in context.scene.objects:
            if ob.type == 'MESH':
                mesh_cl.objects.link(ob)
            elif ob.type == 'LIGHT':
                light_cl.objects.link(ob)
            elif ob.type == 'CAMERA':
                camera_cl.objects.link(ob)
        return {'FINISHED'}



def register():
    bpy.utils.register_class(OBJECT_OT_collector_types)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_collector_types)
