# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Create LODs",
    "author" : "Padme4000", 
    "description" : "Helps create lods for modding games such as Dragon Age Inquisition and Mass Effect Andromeda where the game requires you to still need the lower lods to import meshes",
    "blender" : (3, 0, 0),
    "version" : (1, 0, 0),
    "location" : "",
    "waring" : "",
    "doc_url": "", 
    "tracker_url": "", 
    "category" : "3D View" 
}


import bpy
import bpy.utils.previews


addon_keymaps = {}
_icons = None
class SNA_OT_Lod_1_8621D(bpy.types.Operator):
    bl_idname = "sna.lod_1_8621d"
    bl_label = "LOD_1"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        import os
        bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":0.163508, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})
        for ob in bpy.context.selected_objects:    
            bpy.context.view_layer.objects.active = ob
            bpy.ops.object.modifier_remove(modifier="Decimate")
            bpy.ops.object.modifier_add(type='DECIMATE')
            bpy.context.object.modifiers["Decimate"].ratio = 0.8
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Lod_2_4B8Bf(bpy.types.Operator):
    bl_idname = "sna.lod_2_4b8bf"
    bl_label = "LOD_2"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        import os
        bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":0.163508, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})
        for ob in bpy.context.selected_objects:    
            bpy.context.view_layer.objects.active = ob
            bpy.ops.object.modifier_remove(modifier="Decimate")
            bpy.ops.object.modifier_add(type='DECIMATE')
            bpy.context.object.modifiers["Decimate"].ratio = 0.7
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Lod_4_C8Bab(bpy.types.Operator):
    bl_idname = "sna.lod_4_c8bab"
    bl_label = "LOD_4"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        import os
        bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":0.163508, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})
        for ob in bpy.context.selected_objects:    
            bpy.context.view_layer.objects.active = ob
            bpy.ops.object.modifier_remove(modifier="Decimate")
            bpy.ops.object.modifier_add(type='DECIMATE')
            bpy.context.object.modifiers["Decimate"].ratio = 0.5
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Lod_3_6A095(bpy.types.Operator):
    bl_idname = "sna.lod_3_6a095"
    bl_label = "LOD_3"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        import os
        bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":0.163508, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})
        for ob in bpy.context.selected_objects:    
            bpy.context.view_layer.objects.active = ob
            bpy.ops.object.modifier_remove(modifier="Decimate")
            bpy.ops.object.modifier_add(type='DECIMATE')
            bpy.context.object.modifiers["Decimate"].ratio = 0.6
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_PT_CREATE_LODS_E9503(bpy.types.Panel):
    bl_label = 'Create LODs'
    bl_idname = 'SNA_PT_CREATE_LODS_E9503'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'Padmes Addons'
    bl_order = 0
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        op = layout.operator('sna.lod_1_8621d', text='Create LOD 1', icon_value=0, emboss=True, depress=False)
        op = layout.operator('sna.lod_2_4b8bf', text='Create LOD 2', icon_value=0, emboss=True, depress=False)
        op = layout.operator('sna.lod_3_6a095', text='Create LOD 3', icon_value=0, emboss=True, depress=False)
        op = layout.operator('sna.lod_4_c8bab', text='Create LOD 4', icon_value=0, emboss=True, depress=False)


class SNA_OT_Change_Lod_2_8367D(bpy.types.Operator):
    bl_idname = "sna.change_lod_2_8367d"
    bl_label = "Change_LOD_2"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        import os
        for ob in bpy.context.selected_objects:    
            bpy.context.view_layer.objects.active = ob
            bpy.ops.object.modifier_remove(modifier="Decimate")
            bpy.ops.object.modifier_add(type='DECIMATE')
            bpy.context.object.modifiers["Decimate"].ratio = 0.7
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_PT_CHANGE_LODS_B56FF(bpy.types.Panel):
    bl_label = 'Change LODs'
    bl_idname = 'SNA_PT_CHANGE_LODS_B56FF'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'Padmes Addons'
    bl_order = 0
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        op = layout.operator('sna.change_lod_1_1a091', text='Change to LOD 1', icon_value=0, emboss=True, depress=False)
        op = layout.operator('sna.change_lod_2_8367d', text='Change to LOD 2', icon_value=0, emboss=True, depress=False)
        op = layout.operator('sna.change_lod_3_5f074', text='Change to LOD 3', icon_value=0, emboss=True, depress=False)
        op = layout.operator('sna.change_lod_4_1811a', text='Change to LOD 4', icon_value=0, emboss=True, depress=False)


class SNA_OT_Change_Lod_4_1811A(bpy.types.Operator):
    bl_idname = "sna.change_lod_4_1811a"
    bl_label = "Change_LOD_4"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        import os
        for ob in bpy.context.selected_objects:    
            bpy.context.view_layer.objects.active = ob
            bpy.ops.object.modifier_remove(modifier="Decimate")
            bpy.ops.object.modifier_add(type='DECIMATE')
            bpy.context.object.modifiers["Decimate"].ratio = 0.5
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Change_Lod_3_5F074(bpy.types.Operator):
    bl_idname = "sna.change_lod_3_5f074"
    bl_label = "Change_LOD_3"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        import os
        for ob in bpy.context.selected_objects:    
            bpy.context.view_layer.objects.active = ob
            bpy.ops.object.modifier_remove(modifier="Decimate")
            bpy.ops.object.modifier_add(type='DECIMATE')
            bpy.context.object.modifiers["Decimate"].ratio = 0.6    
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Change_Lod_1_1A091(bpy.types.Operator):
    bl_idname = "sna.change_lod_1_1a091"
    bl_label = "Change_LOD_1"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        import os
        for ob in bpy.context.selected_objects:    
            bpy.context.view_layer.objects.active = ob
            bpy.ops.object.modifier_remove(modifier="Decimate")
            bpy.ops.object.modifier_add(type='DECIMATE')
            bpy.context.object.modifiers["Decimate"].ratio = 0.8
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def register():
    global _icons
    _icons = bpy.utils.previews.new()
    bpy.utils.register_class(SNA_OT_Lod_1_8621D)
    bpy.utils.register_class(SNA_OT_Lod_2_4B8Bf)
    bpy.utils.register_class(SNA_OT_Lod_4_C8Bab)
    bpy.utils.register_class(SNA_OT_Lod_3_6A095)
    bpy.utils.register_class(SNA_PT_CREATE_LODS_E9503)
    bpy.utils.register_class(SNA_OT_Change_Lod_2_8367D)
    bpy.utils.register_class(SNA_PT_CHANGE_LODS_B56FF)
    bpy.utils.register_class(SNA_OT_Change_Lod_4_1811A)
    bpy.utils.register_class(SNA_OT_Change_Lod_3_5F074)
    bpy.utils.register_class(SNA_OT_Change_Lod_1_1A091)


def unregister():
    global _icons
    bpy.utils.previews.remove(_icons)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    for km, kmi in addon_keymaps.values():
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    bpy.utils.unregister_class(SNA_OT_Lod_1_8621D)
    bpy.utils.unregister_class(SNA_OT_Lod_2_4B8Bf)
    bpy.utils.unregister_class(SNA_OT_Lod_4_C8Bab)
    bpy.utils.unregister_class(SNA_OT_Lod_3_6A095)
    bpy.utils.unregister_class(SNA_PT_CREATE_LODS_E9503)
    bpy.utils.unregister_class(SNA_OT_Change_Lod_2_8367D)
    bpy.utils.unregister_class(SNA_PT_CHANGE_LODS_B56FF)
    bpy.utils.unregister_class(SNA_OT_Change_Lod_4_1811A)
    bpy.utils.unregister_class(SNA_OT_Change_Lod_3_5F074)
    bpy.utils.unregister_class(SNA_OT_Change_Lod_1_1A091)
