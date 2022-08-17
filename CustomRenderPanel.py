import bpy

class CustomRenderPanel(bpy.types.Panel):
    
    bl_idname = 'CustomRenderPanel'
    bl_label = 'Label Here'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Render Panel'
    
    def draw(self, context):
        self.layout.label(text='Context Here')

if __name__ == '__main__':
    bpy.utils.register_class(CustomRenderPanel)
