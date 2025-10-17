import bpy
import random
import math

class box:
    def __init__(self):
        self.r = 0

    def create(self,x,y,z,sx,sy,sz):
        bpy.ops.mesh.primitive_cube_add(
          size=1, 
          enter_editmode=False, 
          align='WORLD', 
          location=(x, y, z),
          scale=(sx, sy, sz) )


        return bpy.context.active_object 

    def makehole(self, Outer, Inner):
        bool_mod = Outer.modifiers.new(name="Hole", type='BOOLEAN')
        bool_mod.operation = 'DIFFERENCE'
        bool_mod.use_self = False
        bool_mod.solver = 'FAST'
        bool_mod.object = Inner

        # Apply the modifier
        bpy.context.view_layer.objects.active = Outer
        bpy.ops.object.modifier_apply(modifier=bool_mod.name)

        # Delete the cutter (optional)
        bpy.data.objects.remove(Inner, do_unlink=True)

        return Outer
