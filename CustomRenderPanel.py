import bpy

class CustomRenderPanel(bpy.types.Panel):
    
    bl_idname = 'CustomRenderPanel'
    bl_label = 'Label Here'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Render Panel'
    
    def draw(self, context):
        layout = self.layout
        ##########################################
        self.layout.label(text='Render Settings')
        
        layout.operator("render.render")
        
        ##########################################
        self.layout.label(text='Camera Settings')
        layout.operator("view3d.camera_to_view")
        layout.operator("view3d.camera_to_view_selected")

bpy.utils.register_class(CustomRenderPanel)
