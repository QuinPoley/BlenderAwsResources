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
from bpy.types import Operator, Menu
from bpy.props import FloatVectorProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector
#from . import ec2_maker
#from . import lambda_maker
#from . import dynamo_maker
#from . import apigateway_maker
#from . import waf_maker

class DRAWAWSRESOURCE_MT_ComputeAdd(Menu):
    bl_idname = "VIEW3D_MT_mesh_compute_add"
    bl_label = "Compute"

    def draw(self, context):
        self.layout.operator("mesh.ecmaker", text="Amazon Elastic Compute Cloud (EC2)")
        self.layout.operator("mesh.ecmaker", text="Amazon EC2 Spot")
        self.layout.operator("mesh.ecmaker", text="Amazon EC2 Autoscaling")
        self.layout.operator("mesh.ecmaker", text="Amazon Lightsail")
        self.layout.operator("mesh.ecmaker", text="AWS Batch")
        self.layout.operator("mesh.ecmaker", text="Amazon Elastic Container Service (ECS)")
        self.layout.operator("mesh.ecmaker", text="Amazon ECS Anywhere")
        self.layout.operator("mesh.ecmaker", text="Amazon Elastic Container Registry (ECR)")
        self.layout.operator("mesh.ecmaker", text="Amazon Elastic Kubernetes Service (EKS)")
        self.layout.operator("mesh.ecmaker", text="Anazon EKS Anywhere")
        self.layout.operator("mesh.ecmaker", text="AWS Fargate")
        self.layout.operator("mesh.ecmaker", text="AWS App Runner")
        self.layout.operator("mesh.lambda", text="AWS Lambda")
        self.layout.operator("mesh.lambda", text="AWS Outposts")
        self.layout.operator("mesh.lambda", text="AWS Snow Family")
        self.layout.operator("mesh.lambda", text="AWS Wavelength")
        self.layout.operator("mesh.lambda", text="VMware Cloud on AWS")
        self.layout.operator("mesh.lambda", text="AWS Local Zones")
        self.layout.operator("mesh.lambda", text="AWS Savings Plan")
        self.layout.operator("mesh.lambda", text="AWS Compute Optimizer")
        self.layout.operator("mesh.lambda", text="AWS Elastic Beanstalk")
        self.layout.operator("mesh.lambda", text="EC2 Image Builder")
        self.layout.operator("mesh.lambda", text="Elastic Load Balancing (ELB)")

class DRAWAWSRESOURCE_MT_StorageAdd(Menu):
    bl_idname = "VIEW3D_MT_mesh_storage_add"
    bl_label = "Storage"

    def draw(self, context):
        self.layout.operator("mesh.simplestorageservice", text="Amazon Simple Storage Service (S3)")
        self.layout.operator("mesh.efs", text="Amazon Elastic File System")
        self.layout.operator("mesh.simplestorageservice", text="Amazon FSx for Windows File Server")
        self.layout.operator("mesh.simplestorageservice", text="Amazon FSx for Lustre")
        self.layout.operator("mesh.simplestorageservice", text="Amazon Elastic Block Store")
        self.layout.operator("mesh.simplestorageservice", text="AWS Backup")
        self.layout.operator("mesh.simplestorageservice", text="AWS Storage Gateway")
        self.layout.operator("mesh.simplestorageservice", text="AWS Datasync")
        self.layout.operator("mesh.simplestorageservice", text="AWS Transfer Family")
        self.layout.operator("mesh.simplestorageservice", text="AWS Snow Family")

class DRAWAWSRESOURCE_MT_DatabaseAdd(Menu):
    bl_idname = "VIEW3D_MT_mesh_database_add"
    bl_label = "Database"

    def draw(self, context):
        self.layout.operator("mesh.aurora", text="Amazon Aurora")
        self.layout.operator("mesh.aurora", text="Amazon RDS")
        self.layout.operator("mesh.redshift", text="Amazon Redshift")
        self.layout.operator("mesh.dynamo", text="Amazon DynamoDB")
        self.layout.operator("mesh.elasticache", text="Amazon ElastiCache for Memcached")
        self.layout.operator("mesh.elasticache", text="Amazon ElastiCache for Redis")
        self.layout.operator("mesh.dynamo", text="Amazon DocumentDB") # ??????
        self.layout.operator("mesh.dynamo", text="Amazon Keyspaces") # ??????
        self.layout.operator("mesh.dynamo", text="Amazon Neptune")  # ?????
        self.layout.operator("mesh.dynamo", text="Amazon Timestream")  # ??????
        self.layout.operator("mesh.dynamo", text="Amazon QLDB")  # ???????

class DRAWAWSRESOURCE_MT_SecurityAdd(Menu):
    bl_idname = "VIEW3D_MT_mesh_security_add"
    bl_label = "Security"

    def draw(self, context):
        self.layout.operator("mesh.apigateway", text="AWS Identity & Access Management (IAM)")
        self.layout.operator("mesh.apigateway", text="AWS Single Sign-On")
        self.layout.operator("mesh.apigateway", text="Amazon Cognito")
        self.layout.operator("mesh.apigateway", text="AWS Directory Service")
        self.layout.operator("mesh.apigateway", text="AWS Resource Access Manager")
        self.layout.operator("mesh.apigateway", text="AWS Organizations")
        self.layout.operator("mesh.apigateway", text="AWS Security Hub")
        self.layout.operator("mesh.apigateway", text="Amazon GuardDuty")
        self.layout.operator("mesh.apigateway", text="Amazon Inspector")
        self.layout.operator("mesh.apigateway", text="AWS Config")
        self.layout.operator("mesh.apigateway", text="AWS CloudTrail")

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

class DRAWAWSRESOURCE_OT_S3MAKER(Operator):
    bl_idname = "mesh.simplestorageservice"
    bl_label = "S3"
    bl_description = "Draw S3"

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

class DRAWAWSRESOURCE_OT_AURORA(Operator):
    bl_idname = "mesh.aurora"
    bl_label = "Aurora"
    bl_description = "Draw Aurora"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Use Properties panel (N) to define parms", icon='INFO')

    # -----------------------------------------------------
    # Execute
    # -----------------------------------------------------
    def execute(self, context):
        if bpy.context.mode == "OBJECT":
            create_Aurora(self, context)
            return {'FINISHED'}
        else:
            self.report({'WARNING'}, "Archimesh: Option only valid in Object mode")
            return {'CANCELLED'}

class DRAWAWSRESOURCE_OT_REDSHIFT(Operator):
    bl_idname = "mesh.redshift"
    bl_label = "Redshift"
    bl_description = "Draw Redshift"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Use Properties panel (N) to define parms", icon='INFO')

    # -----------------------------------------------------
    # Execute
    # -----------------------------------------------------
    def execute(self, context):
        if bpy.context.mode == "OBJECT":
            create_redshift(self, context)
            return {'FINISHED'}
        else:
            self.report({'WARNING'}, "Archimesh: Option only valid in Object mode")
            return {'CANCELLED'}
        
class DRAWAWSRESOURCE_OT_ELASTICACHE(Operator):
    bl_idname = "mesh.elasticache"
    bl_label = "ElastiCache"
    bl_description = "Draw ElastiCache"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Use Properties panel (N) to define parms", icon='INFO')

    # -----------------------------------------------------
    # Execute
    # -----------------------------------------------------
    def execute(self, context):
        if bpy.context.mode == "OBJECT":
            create_elasticache(self, context)
            return {'FINISHED'}
        else:
            self.report({'WARNING'}, "Archimesh: Option only valid in Object mode")
            return {'CANCELLED'}
        
class DRAWAWSRESOURCE_OT_ELASTICFILESYSTEM(Operator):
    bl_idname = "mesh.efs"
    bl_label = "Elastic File System"
    bl_description = "Draw EFS"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Use Properties panel (N) to define parms", icon='INFO')

    # -----------------------------------------------------
    # Execute
    # -----------------------------------------------------
    def execute(self, context):
        if bpy.context.mode == "OBJECT":
            create_efs(self, context)
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

def create_Aurora(self, context):
    for o in bpy.data.objects:
        o.select_set(False)
    verts = []
    edges = []
    faces = []
    
    
    verts.append(Vector((0, 1, 1)))
    verts.append(Vector((0.6, 0.8, 1)))
    verts.append(Vector((0.9, 0.3, 1)))
    verts.append(Vector((0.9, -0.3, 1)))
    verts.append(Vector((0.6, -0.8, 1)))
    verts.append(Vector((0, -1, 1)))
    verts.append(Vector((-0.6, -0.8, 1)))
    verts.append(Vector((-0.9, -0.3, 1)))
    verts.append(Vector((-0.9, 0.3, 1)))
    verts.append(Vector((-0.6, 0.8, 1)))
    # Bottom half
    verts.append(Vector((0, 1, -1)))
    verts.append(Vector((0.6, 0.8, -1)))
    verts.append(Vector((0.9, 0.3, -1)))
    verts.append(Vector((0.9, -0.3, -1)))
    verts.append(Vector((0.6, -0.8, -1)))
    verts.append(Vector((0, -1, -1)))
    verts.append(Vector((-0.6, -0.8, -1)))
    verts.append(Vector((-0.9, -0.3, -1)))
    verts.append(Vector((-0.9, 0.3, -1)))
    verts.append(Vector((-0.6, 0.8, -1)))
    

        
    faces.append([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    faces.append([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
    faces.append([0, 10, 11, 1])
    faces.append([1, 11, 12, 2])
    faces.append([2, 12, 13, 3])
    faces.append([3, 13, 14, 4])
    faces.append([4, 14, 15, 5])
    faces.append([5, 15, 16, 6])
    faces.append([6, 16, 17, 7])
    faces.append([7, 17, 18, 8])
    faces.append([8, 18, 19, 9])
    faces.append([9, 19, 10, 0])

    mesh = bpy.data.meshes.new(name="Aurora Mesh")
    mesh.from_pydata(verts, edges, faces)
    # useful for development when the mesh may be invalid.
    # mesh.validate(verbose=True)
    object_data_add(context, mesh, operator=self)
    
def create_redshift(self, context):
    for o in bpy.data.objects:
        o.select_set(False)
    verts = []
    edges = []
    faces = []
    
    # Cylinder
    verts.append(Vector((0.4, 0, -1.25)))
    verts.append(Vector((1, 0, -1.25)))
    verts.append(Vector((1, 1, -1.25)))
    verts.append(Vector((0, 1, -1.25)))
    verts.append(Vector((0, 0.4, -1.25)))
    
    verts.append(Vector((0.4, 0, 2.25)))
    verts.append(Vector((1, 0, 2.25)))
    verts.append(Vector((1, 1, 2.25)))
    verts.append(Vector((0, 1, 2.25)))
    verts.append(Vector((0, 0.4, 2.25)))
    
    verts.append(Vector((0, 2, 2.25)))  # 10
    verts.append(Vector((0, 2.5, 2.25))) #11
    verts.append(Vector((2, 2, 2.25)))   #12
    verts.append(Vector((2.5, 2.5, 2.25)))  #27   13
    verts.append(Vector((2, 0, 2.25)))     #28  14
    verts.append(Vector((2.5, 0, 2.25))) # 29   15
    verts.append(Vector((0, 2, -1.25)))   #30   16
    verts.append(Vector((0, 2.5, -1.25)))  #31   17 
    verts.append(Vector((2, 2, -1.25)))    #32    18 
    verts.append(Vector((2.5, 2.5, -1.25))) #33   19 
    verts.append(Vector((2, 0, -1.25)))     #34   20 
    verts.append(Vector((2.5, 0, -1.25)))   #35   21
    
    
    faces.append([0, 1, 6, 5])
    faces.append([4, 0, 5, 9])
    faces.append([1, 2, 7, 6])
    faces.append([2, 3, 8, 7])
    faces.append([3, 4, 9, 8])
    faces.append([0, 1, 2, 3, 4])
    faces.append([5, 6, 7, 8, 9])
    
    
    faces.append([10, 12, 13, 11])
    faces.append([10, 12, 18, 16])
    faces.append([11, 17, 19, 13])
    faces.append([10, 11, 17, 16])
    faces.append([16, 17, 19, 18])
    
    faces.append([20, 21, 19, 18]) # bot
    faces.append([20, 14, 12, 18]) # front
    faces.append([21, 15, 13, 19]) # bac
    faces.append([20, 21, 15, 14]) #side
    faces.append([14, 15, 13, 12]) #top

    mesh = bpy.data.meshes.new(name="Redshift Mesh")
    mesh.from_pydata(verts, edges, faces)
    # useful for development when the mesh may be invalid.
    # mesh.validate(verbose=True)
    object_data_add(context, mesh, operator=self)
    
def create_elasticache(self, context):
    for o in bpy.data.objects:
        o.select_set(False)
    verts = []
    edges = []
    faces = []
    
    offset = 8
    scalar = [3, 1, 3]
    zVals = [-0.25, 1, 2]
    zVals2 = [-1, 0, 1.25]
    for i in range(3): # Make the squares
        verts.append(Vector((0, 1*scalar[i], zVals[i])))
        verts.append(Vector((1*scalar[i], 1*scalar[i], zVals[i])))
        verts.append(Vector((1*scalar[i], 0, zVals[i])))
        verts.append(Vector((0, 0, zVals[i])))
        verts.append(Vector((0, 1*scalar[i], zVals2[i])))
        verts.append(Vector((1*scalar[i], 1*scalar[i], zVals2[i])))
        verts.append(Vector((1*scalar[i], 0, zVals2[i])))
        verts.append(Vector((0, 0, zVals2[i])))
        
        faces.append([0+(i*offset), 1+(i*offset), 2+(i*offset), 3+(i*offset)])
        faces.append([4+(i*offset), 5+(i*offset), 6+(i*offset), 7+(i*offset)])
        faces.append([0+(i*offset), 4+(i*offset), 5+(i*offset), 1+(i*offset)])
        faces.append([1+(i*offset), 5+(i*offset), 6+(i*offset), 2+(i*offset)])
        faces.append([2+(i*offset), 6+(i*offset), 7+(i*offset), 3+(i*offset)])
        faces.append([3+(i*offset), 7+(i*offset), 4+(i*offset), 0+(i*offset)])
    
    
    
    mesh = bpy.data.meshes.new(name="ElastiCache Mesh")
    mesh.from_pydata(verts, edges, faces)
    # useful for development when the mesh may be invalid.
    # mesh.validate(verbose=True)
    object_data_add(context, mesh, operator=self)
    
def create_efs(self, context):
    for o in bpy.data.objects:
        o.select_set(False)
    verts = []
    edges = []
    faces = []
    
    offset = 8
    xvalue = [-1, -1, 0.25, 0, 1.25, 0, 1]
    xvalue2 = [0, 0, 1.25, 1, 2.25, 1, 2]
    yvalue = [-1, 0.25, -1, 0, 0, 1.25, 1]
    yvalue2 = [0, 1.25, 0, 1, 1, 2.25, 2]
    zvalue = [-0.25, -0.25, -0.25, 1, 1, 1, 2.25]
    zvalue2 = [-1.25, -1.25, -1.25, 0, 0, 0, 1.25]
    for i in range(7): # Make the squares
        verts.append(Vector((xvalue[i], yvalue[i], zvalue[i])))
        verts.append(Vector((xvalue2[i], yvalue[i], zvalue[i])))
        verts.append(Vector((xvalue2[i], yvalue2[i], zvalue[i])))
        verts.append(Vector((xvalue[i], yvalue2[i], zvalue[i])))
        verts.append(Vector((xvalue[i], yvalue[i], zvalue2[i])))
        verts.append(Vector((xvalue2[i], yvalue[i], zvalue2[i])))
        verts.append(Vector((xvalue2[i], yvalue2[i], zvalue2[i])))
        verts.append(Vector((xvalue[i], yvalue2[i], zvalue2[i])))
        
        faces.append([0+(i*offset), 1+(i*offset), 2+(i*offset), 3+(i*offset)])
        faces.append([4+(i*offset), 5+(i*offset), 6+(i*offset), 7+(i*offset)])
        faces.append([0+(i*offset), 4+(i*offset), 5+(i*offset), 1+(i*offset)])
        faces.append([1+(i*offset), 5+(i*offset), 6+(i*offset), 2+(i*offset)])
        faces.append([2+(i*offset), 6+(i*offset), 7+(i*offset), 3+(i*offset)])
        faces.append([3+(i*offset), 7+(i*offset), 4+(i*offset), 0+(i*offset)])
    mesh = bpy.data.meshes.new(name="Elastic File System Mesh")
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
        self.layout.menu("VIEW3D_MT_mesh_compute_add", text="Compute", icon="GROUP")
        self.layout.menu("VIEW3D_MT_mesh_storage_add", text="Storage", icon="GROUP")
        self.layout.menu("VIEW3D_MT_mesh_database_add", text="Database", icon="GROUP")
        self.layout.menu("VIEW3D_MT_mesh_security_add", text="Security", icon="GROUP")

def AWSResources(self, context):
    layout = self.layout
    layout.separator()
    self.layout.menu("VIEW3D_MT_mesh_custom_menu_add_aws", icon="GROUP")

classes = (
    DRAWAWSRESOURCE_ADDMENU,
    DRAWAWSRESOURCE_MT_ComputeAdd,
    DRAWAWSRESOURCE_MT_StorageAdd,
    DRAWAWSRESOURCE_MT_DatabaseAdd,
    DRAWAWSRESOURCE_MT_SecurityAdd,
    DRAWAWSRESOURCE_OT_ecmaker,
    DRAWAWSRESOURCE_OT_LAMBDAMAKER,
    DRAWAWSRESOURCE_OT_DynamoMAKER,
    DRAWAWSRESOURCE_OT_APIGATEWAYMAKER,
    DRAWAWSRESOURCE_OT_S3MAKER,
    DRAWAWSRESOURCE_OT_AURORA,
    DRAWAWSRESOURCE_OT_REDSHIFT,
    DRAWAWSRESOURCE_OT_ELASTICACHE,
    DRAWAWSRESOURCE_OT_ELASTICFILESYSTEM
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