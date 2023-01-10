import bpy
from bpy.types import Panel, Operator

#General Panel Class--------------------------------------

class CustomRenderPanel(bpy.types.Panel):
    
    bl_idname = 'General'
    bl_label = 'General'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Render Panel'
    
    def draw(self, context):
        layout = self.layout

        scene = context.scene

#Labels---------------------------------------------------
        self.layout.label(text='Render Settings')
        col = layout.column(align=True)
        row = col.row(align=True)
        
        row.operator("render.render", text = "Engine Render")
        row.operator("render.opengl", text = "Viewport Render")
        layout.operator("")
        
        
#Camera Controls------------------------------------------        
        
        
        self.layout.label(text='Camera Settings')
        col = layout.column(align=True)
        row = col.row(align=True)
        
        row.operator("view3d.camera_to_view", text = "Camera to View")
        row.operator("view3d.camera_to_view_selected", text = "Camera Fit Selected")
        layout.operator("view3d.view_camera", text = "View Camera")
        layout.operator("view3d.walk", text = "Free Camera")

        row = layout.row()
        row.label(text="Output File Path:")
        row.prop(scene.render, "filepath", text="")
        
#Resolutions-----------------------------------------------

class CustomRenderPanel_Res(bpy.types.Panel):
    
    bl_idname = 'Rendering'
    bl_label = 'Resolution Presets'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Render Panel'
    
    def draw(self, context):
        layout = self.layout

        scene = context.scene
        
        row = layout.row()
        row.label(text="Resolution:")
        row.prop(scene.render, "resolution_x", text="X: ")
        row.prop(scene.render, "resolution_y", text="Y: ")
        
        row = layout.row()
        row.label(text="Resolution Scale:")
        row.prop(scene.render, "resolution_percentage", text="")
        
        self.layout.label(text='Resolution Presets')
        layout.operator("render.res_8k", text="8K (7680x4320)")
        layout.operator("render.res_4k", text="4K (3840x2160)")
        layout.operator("render.res_2k", text="2K (2560x1440)")
        layout.operator("render.res_fhd", text="FHD (1920x1080)")
        layout.operator("render.res_hd", text="HD (1280x720)")
        layout.operator("render.res_sd", text="SD (720x480)")
        
#--8K--
class RenderRes8K(bpy.types.Operator):
    bl_idname = "render.res_8k"
    bl_label = "8K"

    def execute(self, context):
        context.scene.render.resolution_x = 7680
        context.scene.render.resolution_y = 4320
        return {'FINISHED'}


#--4K--
class RenderRes4K(bpy.types.Operator):
    bl_idname = "render.res_4k"
    bl_label = "4K"

    def execute(self, context):
        context.scene.render.resolution_x = 3840 
        context.scene.render.resolution_y = 2160
        return {'FINISHED'}


#--2K--    
class RenderRes2K(bpy.types.Operator):
    bl_idname = "render.res_2k"
    bl_label = "2K"

    def execute(self, context):
        context.scene.render.resolution_x = 2560
        context.scene.render.resolution_y = 1440
        return {'FINISHED'}


#--FHD--    
class RenderResFHD(bpy.types.Operator):
    bl_idname = "render.res_fhd"
    bl_label = "FHD"

    def execute(self, context):
        context.scene.render.resolution_x = 1920
        context.scene.render.resolution_y = 1080
        return {'FINISHED'}


#--HD--    
class RenderResHD(bpy.types.Operator):
    bl_idname = "render.res_hd"
    bl_label = "HD"

    def execute(self, context):
        context.scene.render.resolution_x = 1280
        context.scene.render.resolution_y = 720
        return {'FINISHED'}


#--SD--    
class RenderResSD(bpy.types.Operator):
    bl_idname = "render.res_sd"
    bl_label = "SD"

    def execute(self, context):
        context.scene.render.resolution_x = 720
        context.scene.render.resolution_y = 480
        return {'FINISHED'}
    
#Render Engine---------------------------------------------
class RenderEngine(bpy.types.Panel):
    
    bl_idname = 'RenderEnginePT'
    bl_label = 'Render Engine'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Render Panel'
    
    def draw(self, context):
        layout = self.layout

        scene = context.scene
        
        row = layout.row()
        
        self.layout.label(text='Engines')
        
        layout.operator("render.engine_cycles", text="Optmize Render for CYCLES")
        layout.operator("render.engine_eevee", text="Optmize Render for EEVEE")
#--Cycles--
class RenderEngineCycles(bpy.types.Operator):
    bl_idname = "render.engine_cycles"
    bl_label = "Render Engine Cycles"

    def execute(self, context):
        context.scene.render.engine = 'CYCLES'
        context.scene.cycles.device = 'GPU'
        context.scene.cycles.use_preview_adaptive_sampling = False
        context.scene.cycles.preview_samples = 32
        context.scene.cycles.samples = 512*4
        context.scene.cycles.use_auto_tile = True
        context.scene.cycles.tile_size = 128
        return {'FINISHED'}
    
class RenderEngineEevee(bpy.types.Operator):
    bl_idname = "render.engine_eevee"
    bl_label = "Render Engine Eevee"

    def execute(self, context):
        context.scene.render.engine = 'BLENDER_EEVEE'
        context.scene.cycles.device = 'GPU'
        context.scene.cycles.taa_render_samples = 16
        context.scene.cycles.taa_samples = 128*4
        context.scene.eevee.use_bloom = True
        context.scene.eevee.use_motion_blur = False
        context.scene.eevee.use_gtao = True
        context.scene.eevee.use_ssr = True
        return {'FINISHED'}
        
#Register--------------------------------------------------

classes = [CustomRenderPanel,RenderRes8K,RenderRes4K,RenderRes2K,RenderResFHD,RenderResHD,RenderResSD,CustomRenderPanel_Res,RenderEngine,RenderEngineCycles,RenderEngineEevee]

#Thing that does the process
def register():
    
#class register
    for cls in classes:
        bpy.utils.register_class(cls)
        
 
def unregister():
    
    
#class unregister
    for cls in classes:
        bpy.utils.unregister_class(cls) 
     
     
if __name__  == "__main__":
    register() 
