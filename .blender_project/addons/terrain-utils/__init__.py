'''
Start of Block

__init__ file that starts and handlers the registers, the addons and startup settings for the pipeline template.

# licensed by the SPDX GPL 3.0 -- Free software at no warranty
# Authors: David Valencia(FrecklesArte)
# Maintainers: David Valencia(FrecklesArte) of Artist First Productions

End of Block
'''


import bpy
from bpy.app.handlers import persistent

def load_user_preferences():
    print("Allow user preferences!")

def load_startup_settings():
    print("Load the startup settings!")

def register():
    bpy.data.handlers.post.append("load_user_preferences")
    bpy.data.handlers.post.append("load_startup_settings")

def unregister():
    bpy.data.handlers.post.remove("load_user_preferences")
    bpy.data.handlers.post.remove("load_startup_settings")
