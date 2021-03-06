# Converts Blender coords to Minecraft
import mathutils
import math

# Get the Minecraft transformation of an object relative to (blender coordinates) startCoords
def getTransform(context, object, startCoords):

    # Get relative coords
    coords = object.location-startCoords

    # Account for difference in axes between Minecraft and Blender
    mcCoords = convertLoc(coords)
    location = [mcCoords.x, mcCoords.y, mcCoords.z]
    xrot = math.degrees(object.rotation_euler.z)*-1
    
    # Cameras have to be rotated down 90 degrees
    if object.type=='CAMERA':
        yrot = (math.degrees(object.rotation_euler.x)-90)*-1
    else:
        yrot = math.degrees(object.rotation_euler.x)*-1
    
    rotation = [xrot,yrot]

    return (location, rotation)

def convertLoc(coords):
    return mathutils.Vector((coords.x, coords.z, coords.y*-1))

# returns the rotation in euler, no matter what it was initially in 
def get_rotation(input):
    if input.rotation_mode == 'QUATERNION':
        return input.rotation_quaternion.to_euler()
    else:
        return input.rotation_euler
 
# takes an array attained by armature.pose.bones[bone].rotation_euler and converts it to an array
def rotation_to_array(array, isHead):
    
    if isHead:
        new_array = [array[0]*-1, array[1]*-1, array[2]]
    else:
        new_array = [array[2], array[1], array[0]*-1]  
        
    new_array[0] = round(math.degrees(new_array[0]), 2)
    new_array[1] = round(math.degrees(new_array[1]), 2)
    new_array[2] = round(math.degrees(new_array[2]), 2)
    
    return new_array

