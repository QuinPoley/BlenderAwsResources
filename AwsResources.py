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
            create_lambda(self, context)
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
            create_dynamo(self, context)
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
            create_S3(self, context)
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
    
def create_lambda(self, context):
    for o in bpy.data.objects:
        o.select_set(False)
    verts = []
    edges = []
    faces = []

    # TOP FACE
    verts.append(Vector((-1, 1, 0.5)))
    verts.append(Vector((-0.4, 1, 0.5)))
    verts.append(Vector((0.7, -0.7, 0.5)))
    verts.append(Vector((1, -0.7, 0.5)))
    verts.append(Vector((1, -1, 0.5)))
    verts.append(Vector((0.6, -1, 0.5)))
    verts.append(Vector((-0.5, 0.7, 0.5)))
    verts.append(Vector((-1, 0.7, 0.5)))
    
    # BOTTOM FACE
    verts.append(Vector((-1, 1, 0)))
    verts.append(Vector((-0.4, 1, 0)))
    verts.append(Vector((0.7, -0.7, 0)))
    verts.append(Vector((1, -0.7, 0)))
    verts.append(Vector((1, -1, 0)))
    verts.append(Vector((0.6, -1, 0)))
    verts.append(Vector((-0.5, 0.7, 0)))
    verts.append(Vector((-1, 0.7, 0)))
    
    # OTHER THING
    verts.append(Vector((-0.3, 0.2, 0.5)))
    verts.append(Vector((-0.1, -0.1, 0.5)))
    verts.append(Vector((-0.7, -1, 0.5)))
    verts.append(Vector((-1, -1, 0.5)))
    verts.append(Vector((-0.3, 0.2, 0)))
    verts.append(Vector((-0.1, -0.1, 0)))
    verts.append(Vector((-0.7, -1, 0)))
    verts.append(Vector((-1, -1, 0)))

        
    faces.append([0, 1, 2, 3, 4, 5, 6, 7])# Top
    faces.append([8, 9, 10, 11, 12, 13, 14, 15]) # Bottom 
    faces.append([0, 8, 15, 7])
    faces.append([0, 8, 9, 1])
    faces.append([1, 9, 10, 2])
    faces.append([2, 10, 11, 3])
    faces.append([3, 11, 12, 4])
    faces.append([4, 12, 13, 5])
    faces.append([5, 13, 14, 6])
    faces.append([6, 14, 15, 7])
    
    # OtherThing
    faces.append([16, 17, 18, 19])
    faces.append([20, 21, 22, 23])
    faces.append([16, 20, 21, 17])
    faces.append([17, 21, 22, 18])
    faces.append([18, 22, 23, 19])
    faces.append([19, 23, 20, 16])
 

    mesh = bpy.data.meshes.new(name="Lambda Mesh")
    mesh.from_pydata(verts, edges, faces)
    # useful for development when the mesh may be invalid.
    # mesh.validate(verbose=True)
    object_data_add(context, mesh, operator=self)
    
    
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


    mesh = bpy.data.meshes.new(name="Ec2 Mesh")
    mesh.from_pydata(verts, edges, faces)
    # useful for development when the mesh may be invalid.
    # mesh.validate(verbose=True)
    object_data_add(context, mesh, operator=self)
    
def create_dynamo(self, context):
    for o in bpy.data.objects:
        o.select_set(False)
    verts = []
    edges = []
    faces = []
    
    offset = 20
    z_offset = [0.35, 0.85, 1.35, 1.85]
    zs_offset = [0, 0.45, 0.95, 1.45]
    for i in range(4): # Number blocks that jut out
        verts.append(Vector((0, 1, z_offset[i])))
        verts.append(Vector((0.6, 0.8, z_offset[i])))
        verts.append(Vector((0.9, 0.3, z_offset[i])))
        verts.append(Vector((0.9, -0.3, z_offset[i])))
        verts.append(Vector((0.6, -0.8, z_offset[i])))
        verts.append(Vector((0, -1, z_offset[i])))
        verts.append(Vector((-0.6, -0.8, z_offset[i])))
        verts.append(Vector((-0.9, -0.3, z_offset[i])))
        verts.append(Vector((-0.9, 0.3, z_offset[i])))
        verts.append(Vector((-0.6, 0.8, z_offset[i])))
        # Bottom half
        verts.append(Vector((0, 1, zs_offset[i])))
        verts.append(Vector((0.6, 0.8, zs_offset[i])))
        verts.append(Vector((0.9, 0.3, zs_offset[i])))
        verts.append(Vector((0.9, -0.3, zs_offset[i])))
        verts.append(Vector((0.6, -0.8, zs_offset[i])))
        verts.append(Vector((0, -1, zs_offset[i])))
        verts.append(Vector((-0.6, -0.8, zs_offset[i])))
        verts.append(Vector((-0.9, -0.3, zs_offset[i])))
        verts.append(Vector((-0.9, 0.3, zs_offset[i])))
        verts.append(Vector((-0.6, 0.8, zs_offset[i])))
    

        
        faces.append([0+(i*offset), 1+(i*offset), 2+(i*offset), 3+(i*offset), 4+(i*offset), 5+(i*offset), 6+(i*offset), 7+(i*offset), 8+(i*offset), 9+(i*offset)])
        faces.append([10+(i*offset), 11+(i*offset), 12+(i*offset), 13+(i*offset), 14+(i*offset), 15+(i*offset), 16+(i*offset), 17+(i*offset), 18+(i*offset), 19+(i*offset)])
        faces.append([0+(i*offset), 10+(i*offset), 11+(i*offset), 1+(i*offset)])
        faces.append([1+(i*offset), 11+(i*offset), 12+(i*offset), 2+(i*offset)])
        faces.append([2+(i*offset), 12+(i*offset), 13+(i*offset), 3+(i*offset)])
        faces.append([3+(i*offset), 13+(i*offset), 14+(i*offset), 4+(i*offset)])
        faces.append([4+(i*offset), 14+(i*offset), 15+(i*offset), 5+(i*offset)])
        faces.append([5+(i*offset), 15+(i*offset), 16+(i*offset), 6+(i*offset)])
        faces.append([6+(i*offset), 16+(i*offset), 17+(i*offset), 7+(i*offset)])
        faces.append([7+(i*offset), 17+(i*offset), 18+(i*offset), 8+(i*offset)])
        faces.append([8+(i*offset), 18+(i*offset), 19+(i*offset), 9+(i*offset)])
        faces.append([9+(i*offset), 19+(i*offset), 10+(i*offset), 0+(i*offset)])

    mesh = bpy.data.meshes.new(name="Dynamo Mesh")
    mesh.from_pydata(verts, edges, faces)
    # useful for development when the mesh may be invalid.
    # mesh.validate(verbose=True)
    object_data_add(context, mesh, operator=self)
    
def create_S3(self, context):
    for o in bpy.data.objects:
        o.select_set(False)
    verts = []
    edges = []
    faces = []
    
    offset = 8
    squares1 = [-0.25, 1, 2.25]
    squares2 = [-1.25, 0, 1.25]
    for i in range(3): # Make the squares
        verts.append(Vector((0, 1, squares1[i])))
        verts.append(Vector((1, 1, squares1[i])))
        verts.append(Vector((1, 0, squares1[i])))
        verts.append(Vector((0, 0, squares1[i])))
        verts.append(Vector((0, 1, squares2[i])))
        verts.append(Vector((1, 1, squares2[i])))
        verts.append(Vector((1, 0, squares2[i])))
        verts.append(Vector((0, 0, squares2[i])))
        
        faces.append([0+(i*offset), 1+(i*offset), 2+(i*offset), 3+(i*offset)])
        faces.append([4+(i*offset), 5+(i*offset), 6+(i*offset), 7+(i*offset)])
        faces.append([0+(i*offset), 4+(i*offset), 5+(i*offset), 1+(i*offset)])
        faces.append([1+(i*offset), 5+(i*offset), 6+(i*offset), 2+(i*offset)])
        faces.append([2+(i*offset), 6+(i*offset), 7+(i*offset), 3+(i*offset)])
        faces.append([3+(i*offset), 7+(i*offset), 4+(i*offset), 0+(i*offset)])
    
    # Background
    verts.append(Vector((0, 2, squares1[2])))  # 24
    verts.append(Vector((0, 2.5, squares1[2]))) #25
    verts.append(Vector((2, 2, squares1[2])))   #26
    verts.append(Vector((2.5, 2.5, squares1[2])))  #27
    verts.append(Vector((2, 0, squares1[2])))     #28
    verts.append(Vector((2.5, 0, squares1[2]))) # 29
    verts.append(Vector((0, 2, squares2[0])))   #30
    verts.append(Vector((0, 2.5, squares2[0])))  #31
    verts.append(Vector((2, 2, squares2[0])))    #32
    verts.append(Vector((2.5, 2.5, squares2[0]))) #33
    verts.append(Vector((2, 0, squares2[0])))     #34
    verts.append(Vector((2.5, 0, squares2[0])))   #35
    
    # 25 
    faces.append([24, 26, 27, 25])
    faces.append([24, 26, 32, 30])
    faces.append([25, 31, 33, 27])
    faces.append([24, 25, 31, 30])
    faces.append([30, 31, 33, 32])
    
    faces.append([34, 35, 33, 32]) # bot
    faces.append([34, 28, 26, 32]) # front
    faces.append([35, 29, 27, 33]) # bac
    faces.append([34, 35, 29, 28]) #side
    faces.append([28, 29, 27, 26]) #top
    
    mesh = bpy.data.meshes.new(name="S3 Mesh")
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