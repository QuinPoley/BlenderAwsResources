bl_info = {
    "name": "DrawAwsResources",
    "author": "Quin Poley",
    "location": "View3D > Add Mesh / Sidebar > Create Tab",
    "version": (1, 0, 0),
    "blender": (2, 93, 0),
    "description": "Draw AWS Resources",
    "category": "Add Mesh"
    }

import bpy
from bpy.types import Operator
from bpy.props import FloatVectorProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector
#from . import ec2_maker
#from . import lambda_maker
#from . import dynamo_maker
#from . import apigateway_maker
#from . import waf_maker

class DRAWAWSRESOURCE_OT_ecmaker(Operator):
    bl_idname = "mesh.ecmaker"
    bl_label = "Ec2 Instance"
    bl_description = "Draw Ec2 Instance"
    bl_category = 'View'
    bl_options = {'REGISTER', 'UNDO'}

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Use Properties panel (N) to define parms", icon='INFO')

    # -----------------------------------------------------
    # Execute
    # -----------------------------------------------------
    def execute(self, context):
        if bpy.context.mode == "OBJECT":
            create_ec2(self, context)
            return {'FINISHED'}
        else:
            self.report({'WARNING'}, "Archimesh: Option only valid in Object mode")
            return {'CANCELLED'}

class DRAWAWSRESOURCE_OT_LAMBDAMAKER(Operator):
    bl_idname = "mesh.lambda"
    bl_label = "Lambda"
    bl_description = "Draw Lambda Func"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Use Properties panel (N) to define parms", icon='INFO')

    # -----------------------------------------------------
    # Execute
    # -----------------------------------------------------
    def execute(self, context):
        if bpy.context.mode == "OBJECT":
            create_object(self, context)
            return {'FINISHED'}
        else:
            self.report({'WARNING'}, "Archimesh: Option only valid in Object mode")
            return {'CANCELLED'}

class DRAWAWSRESOURCE_OT_DynamoMAKER(Operator):
    bl_idname = "mesh.dynamo"
    bl_label = "DynamoDB"
    bl_description = "Draw DynamoDB"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Use Properties panel (N) to define parms", icon='INFO')

    # -----------------------------------------------------
    # Execute
    # -----------------------------------------------------
    def execute(self, context):
        if bpy.context.mode == "OBJECT":
            create_object(self, context)
            return {'FINISHED'}
        else:
            self.report({'WARNING'}, "Archimesh: Option only valid in Object mode")
            return {'CANCELLED'}

class DRAWAWSRESOURCE_OT_APIGATEWAYMAKER(Operator):
    bl_idname = "mesh.apigateway"
    bl_label = "API_Gateway"
    bl_description = "Draw API Gateway"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Use Properties panel (N) to define parms", icon='INFO')

    # -----------------------------------------------------
    # Execute
    # -----------------------------------------------------
    def execute(self, context):
        if bpy.context.mode == "OBJECT":
            create_object(self, context)
            return {'FINISHED'}
        else:
            self.report({'WARNING'}, "Archimesh: Option only valid in Object mode")
            return {'CANCELLED'}

class DRAWAWSRESOURCE_OT_WAFMAKER(Operator):
    bl_idname = "mesh.webappfirewall"
    bl_label = "WAF"
    bl_description = "Draw WAF"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Use Properties panel (N) to define parms", icon='INFO')

    # -----------------------------------------------------
    # Execute
    # -----------------------------------------------------
    def execute(self, context):
        if bpy.context.mode == "OBJECT":
            create_object(self, context)
            return {'FINISHED'}
        else:
            self.report({'WARNING'}, "Archimesh: Option only valid in Object mode")
            return {'CANCELLED'}

def create_object(self, context):
    scene = context.scene
    cursor = scene.cursor.location
    active = context.active_object
    
    copy = active.copy()
    scene.collection.objects.link(copy)
    copy.location = cursor

def create_ec2(self, context):
    for o in bpy.data.objects:
        o.select_set(False)

    verts = []
    edges = []
    faces = []
    offset = 8 
    for i in range(4):
        scale_x = 0.15
        x_buffer = 0.5
        scale_y = 1
        scale_z = 1 - (i/20)
        scale_z_second = scale_z - 0.1
            
        #scale_x-
        verts.append(Vector((-scale_x-(i*x_buffer), 1 * scale_y, -1 * scale_z_second)))
        verts.append(Vector((scale_x-(i*x_buffer), 1 * scale_y, -1 * scale_z)))
        verts.append(Vector((scale_x-(i*x_buffer), -1 * scale_y, -1 * scale_z)))
        verts.append(Vector((-scale_x-(i*x_buffer), -1 * scale_y, -1 * scale_z_second)))
        verts.append(Vector((-scale_x-(i*x_buffer), 1 * scale_y, 1 * scale_z_second)))
        verts.append(Vector((scale_x-(i*x_buffer), 1 * scale_y, 1 * scale_z)))
        verts.append(Vector((scale_x-(i*x_buffer), -1 * scale_y, 1 * scale_z)))
        verts.append(Vector((-scale_x-(i*x_buffer), -1 * scale_y, 1 * scale_z_second)))


        
        faces.append([0+(offset*i), 1+(offset*i), 2+(offset*i), 3+(offset*i)])
        faces.append([0+(offset*i), 1+(offset*i), 5+(offset*i), 4+(offset*i)])
        faces.append([1+(offset*i), 2+(offset*i), 6+(offset*i), 5+(offset*i)])
        faces.append([2+(offset*i), 3+(offset*i), 7+(offset*i), 6+(offset*i)])
        faces.append([3+(offset*i), 0+(offset*i), 4+(offset*i), 7+(offset*i)])
        faces.append([4+(offset*i), 5+(offset*i), 6+(offset*i), 7+(offset*i)])


    mesh = bpy.data.meshes.new(name="New Object Mesh")
    mesh.from_pydata(verts, edges, faces)
    # useful for development when the mesh may be invalid.
    # mesh.validate(verbose=True)
    object_data_add(context, mesh, operator=self)
# ----------------------------------------------------------
# Registration
# ----------------------------------------------------------

class DRAWAWSRESOURCE_ADDMENU(bpy.types.Menu):
    bl_idname = "VIEW3D_MT_mesh_custom_menu_add_aws"
    bl_label = "AwsResources"

    # noinspection PyUnusedLocal
    def draw(self, context):
        self.layout.operator_context = 'INVOKE_REGION_WIN'
        self.layout.operator("mesh.ecmaker", text="Ec2")
        self.layout.operator("mesh.lambda", text="Lambda")
        self.layout.operator("mesh.dynamo", text="Dynamo")
        self.layout.operator("mesh.apigateway", text="API Gateway")
        self.layout.operator("mesh.webappfirewall", text="WAF")

def AWSResources(self, context):
    layout = self.layout
    layout.separator()
    self.layout.menu("VIEW3D_MT_mesh_custom_menu_add_aws", icon="GROUP")

classes = (
    DRAWAWSRESOURCE_ADDMENU,
    DRAWAWSRESOURCE_OT_ecmaker,
    DRAWAWSRESOURCE_OT_LAMBDAMAKER,
    DRAWAWSRESOURCE_OT_DynamoMAKER,
    DRAWAWSRESOURCE_OT_APIGATEWAYMAKER,
    DRAWAWSRESOURCE_OT_WAFMAKER
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.VIEW3D_MT_mesh_add.append(AWSResources)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    bpy.types.VIEW3D_MT_mesh_add.remove(AWSResources)

if __name__ == "__main__":
    register()