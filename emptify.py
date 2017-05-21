import bpy

def main(context):
    obs = list(context.selected_objects)
    scene = bpy.context.scene
    for ob in obs:
        Emptyfy.empty(ob,scene)
        
        
        scene.update()
        
class Emptyfy(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emptyfy"
    bl_label = "Emptify"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}

    def empty(ob,scene):
        #creates new empty and links to original
        empty_ob = bpy.data.objects.new(ob.name+"_empty", None)
        scene.objects.link(empty_ob)
        
        #selecte them both
        bpy.ops.object.select_all(action='DESELECT')
        empty_ob.select = True;
        ob.select = True;
        bpy.context.scene.objects.active = ob;
        
        bpy.ops.object.parent_no_inverse_set()
        bpy.ops.object.select_all(action='DESELECT')
        
        empty_ob.select = True;        
        #bpy.ops.object.select_pattern(pattern=empty_ob.name,extend=False)
        bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
        bpy.ops.object.select_all(action='DESELECT')

        ob.select = True;
        #bpy.ops.object.select_pattern(pattern=ob.name,extend=False)
        bpy.ops.object.delete(use_global=False)


def register():
    bpy.utils.register_class(Emptyfy)


def unregister():
    bpy.utils.unregister_class(Emptyfy)


if __name__ == "__main__":
    register()

    # test call
    #bpy.ops.object.emptyfy()
