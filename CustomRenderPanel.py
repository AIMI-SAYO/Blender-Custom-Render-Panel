import bpy

class CustomRenderPanel(bpy.types.Panel):
    
    bl_idname = 'CustomRenderPanel'
    bl_label = 'Label Here'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Render Panel'
    
    def draw(self, context):
        layout = self.layout
        
        layout.operator("object.delete")
        layout.operator("mesh.primitive_cube_add")

bpy.utils.register_class(CustomRenderPanel)
