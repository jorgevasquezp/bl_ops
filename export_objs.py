import bpy

dest="/Volumes/pegasus/01_PROJECTS/17048_DSROS012_Disney_LionKing_Package/09_Graphics/01_MKN_Graphic_Assets/04_3d/OBJ/mask_pieces/"

def main(context):
    objects = list(context.selected_objects)
    bpy.ops.object.select_all(action='TOGGLE')
    for ob in objects:
        bpy.ops.object.select_pattern(pattern=ob.name)
        bpy.ops.export_scene.obj(filepath=dest+ob.name+".obj",use_selection=True, global_scale=100.0, )
        bpy.ops.object.select_all(action='TOGGLE')


class ExportOBJs(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.export_objs"
    bl_label = "Simple Object Operator"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(ExportOBJs)


def unregister():
    bpy.utils.unregister_class(ExportOBJs)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.object.export_objs()
