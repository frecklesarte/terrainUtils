import pyright

import bpy
import bmesh



TerrainMesh = bpy.data.meshes.new("PyTerrainErode")
TerrainOb = bpy.data.objects.new("TerrainPlane", TerrainMesh)
bpy.context.scene.collection.objects.link(TerrainOb)

bm = bmesh.new()
bmesh.ops.create_grid(bm, x_segments=2, y_segments=2, size=2)
bm.to_mesh(TerrainMesh)

mod = ob.modifiers


class TerrainNodes():



    def createMesh(self):

    def validateCreatedMesh(self):


