import arcpy
import os

BASE_DIR = os.path.dirname(os.path.abspath('C:\\Users\\Julian\\Desktop\\lab4_gisprogramming\\lab4data'))

### >>>>>> Add your code here
INPUT_DB_PATH = "C:\\Users\\Julian\\Desktop\\lab4_gisprogramming\\lab4data\\Campus.gdb"
CSV_PATH = "C:\\Users\\Julian\\Desktop\\lab4_gisprogramming\\lab4data\\garages.csv"
OUTPUT_DB_PATH = "C:\\Users\\Julian\\Desktop\\lab4_gisprogramming\\lab4data\\output.gdb"
### <<<<<< End of your code here

arcpy.env.workspace = INPUT_DB_PATH

# Layers need to be kept
layers_to_keep = ["GaragePoints", "LandUse", "Structures", "Trees"]

# list all feature clases
feature_classes = arcpy.ListFeatureClasses()

# delete other classes
for fc in feature_classes:
    if fc not in layers_to_keep:
        arcpy.management.Delete(fc)

# create GDB management
if not os.path.exists(OUTPUT_DB_PATH):
    ### >>>>>> Add your code here
    arcpy.management.CreateFileGDB(os.path.dirname(OUTPUT_DB_PATH), os.path.basename(OUTPUT_DB_PATH))
    ### <<<<<< End of your code here

# Load .csv file to input GDB
### >>>>>> Add your code here
garage_points_output = "C:\\Users\\Julian\Desktop\\lab4_gisprogramming\\lab4data\\garages.csv"
arcpy.management.XYTableToPoint(
    CSV_PATH, 
    garage_points_output, 
    x_field="X", 
    y_field="Y", 
)   
### <<<<<< End of your code here

# Print spatial references before re-projection
print("Before Re-Projection:")
print(f"garages layer spatial reference: {arcpy.Describe(garage_points_output).spatialReference.name}.")
print(f"Structures layer spatial reference: {arcpy.Describe('Structures').spatialReference.name}.")
# Re-project
## >>>>>>>>> change the codes below
target_ref = arcpy.SpatialReference(4326)  
structures_projected = arcpy.management.Project("Structures", 
"in_memory/Structures_Projected",
 target_ref
 )
## <<<<<<<< End of your code here
# print spatial references after re-projection
print("After Re-Projection:")
print(f"garages layer spatial reference: {arcpy.Describe(garage_points_output).spatialReference.name}.")
print(f"re-projected Structures layer spatial reference: {arcpy.Describe(structures_projected).spatialReference.name}.")

### >>>>>> Add your code here
# Buffer analysis
radiumStr = "150 meter"
garages_buffered = arcpy.analysis.Buffer(garage_points_output, "in_memory/garages_buffered", radiumStr)
# Intersect analysis
intersection_result = arcpy.analysis.Intersect([garages_buffered, structures_projected], "in_memory/intersection")

layers_to_copy = {garage_points_output: "garages", "Structures": "Structure", garages_buffered: "garages_buffered", intersection_result: "intersection"}

for source_layer, output_name in layers_to_copy.items():
    output_path = os.path.join(OUTPUT_DB_PATH, output_name)
    
    if arcpy.Exists(output_path):
        arcpy.management.Delete(output_path)
    
    arcpy.management.CopyFeatures(source_layer, output_path)

print("Feature layers have been exported to the output GDB.")
 
### <<<<<< End of your code here
