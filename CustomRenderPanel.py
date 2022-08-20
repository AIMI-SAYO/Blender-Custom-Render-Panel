import bpy
from bpy.types import Panel

class CustomRenderPanel(bpy.types.Panel):
    
    bl_idname = 'CustomRenderPanel'
    bl_label = 'Label Here'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Render Panel'
    
    def draw(self, context):
        layout = self.layout
        
        
######################################################################################        
        
        
        self.layout.label(text='Render Settings')
        col = layout.column(align=True)
        row = col.row(align=True)
        
        row.operator("render.render", text = "Engine Render")
        row.operator("render.opengl", text = "Viewport Render")
        layout.operator("")
        
        
######################################################################################        
        
        
        self.layout.label(text='Camera Settings')
        col = layout.column(align=True)
        row = col.row(align=True)
        
        row.operator("view3d.camera_to_view", text = "Camera to View")
        row.operator("view3d.camera_to_view_selected", text = "Camera Fit Selected")
        layout.operator("view3d.view_camera", text = "View Camera")
        layout.operator("view3d.walk", text = "Free Camera")
        
        
######################################################################################        
        
        
        self.layout.label(text='TEST')
        
        layout.operator("")
     
        
######################################################################################        


bpy.utils.register_class(CustomRenderPanel)
