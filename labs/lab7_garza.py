#Lab 7
import sys
sys.path.append(r"C:\\Users\\Julian\\AppData\\Local\\ESRI\\conda\\envs\\arcgispro-py3-clone")
import arcpy

# get hillshade of the singleband DEM dataset
arcpy.ddd.HillShade(
    in_raster = r'C:\Users\Julian\Desktop\Lab7Data\Data\DEM\n30_w097_1arc_v3.tif',   # replace this with your `DEM` tif file path.
    out_raster = r'C:\\Users\\Julian\\Desktop\\Lab7Data\\hillshade',  # replace this with your output tif file path.
    azimuth = 315,          # `{**}` means this param is optional, the default value of this dataset's azimuth should be 315
    altitude = 45,               # the default value of this dataset's altitude value of this dataset's altitude should be 45
    model_shadows = "NO_SHADOWS",                # we don't need to add shadows to this case, so set "NO_SHADOWS" to this param
    z_factor = 1,               # default value is 1
)
# get slope of the singleband DEM dataset
arcpy.ddd.Slope(
    in_raster = r'C:\Users\Julian\Desktop\Lab7Data\Data\DEM\n30_w097_1arc_v3.tif',   # replace this with your `DEM` tif file path
    out_raster = r'C:\\Users\\Julian\\Desktop\\Lab7Data\\slope',  # replace this with your output tif file path
    output_measurement = "DEGREE",            # `{**}` means this param is optional, the default value of this dataset's measurement should be "DEGREE"
    z_factor = 1,               # `{**}` means this param is optional, the default value of this dataset's z_factor should be 1
)

band_RED = arcpy.sa.Raster("C:\\Users\\Julian\\Desktop\\Lab7Data\\Data\\LandSAT\\LT05_L2SP_026039_20110803_20200820_02_T1_SR_B3.TIF") # replace the <full-path-to-RED-band> to your path to the band represents RED value.
band_GREEN = arcpy.sa.Raster("C:\\Users\\Julian\\Desktop\\Lab7Data\\Data\\LandSAT\\LT05_L2SP_026039_20110803_20200820_02_T1_SR_B2.TIF") # replace the <full-path-to-GREEN-band> to your path to the band represents GREEN value.
band_BLUE = arcpy.sa.Raster("C:\\Users\\Julian\\Desktop\\Lab7Data\\Data\\LandSAT\\LT05_L2SP_026039_20110803_20200820_02_T1_SR_B1.TIF") # replace the <full-path-to-BLUE-band> to your path to the band represents BLUE value.

# ********************
# BE CAREFUL
# The order of the list of the bands' objs should follow the order of R-G-B to get a correct RGB composite raster.
# ********************
arcpy.management.CompositeBands(
    [band_RED, band_GREEN, band_BLUE],
    r"C:\Users\Julian\Desktop\Lab7Data\output_stuff\compbands.tif"
)

BASE_DIR = r"C:\Users\Julian\Desktop\Lab7Data"

band_RED = arcpy.sa.Raster(f"{BASE_DIR}\\Data\\LandSAT\\LT05_L2SP_026039_20110803_20200820_02_T1_SR_B3.TIF")
band_GREEN = arcpy.sa.Raster(f"{BASE_DIR}\\Data\\LandSAT\\LT05_L2SP_026039_20110803_20200820_02_T1_SR_B2.TIF")
band_BLUE = arcpy.sa.Raster(f"{BASE_DIR}\\Data\\LandSAT\\LT05_L2SP_026039_20110803_20200820_02_T1_SR_B1.TIF")
band_NIR = arcpy.sa.Raster(f"{BASE_DIR}\\Data\\LandSAT\\LT05_L2SP_026039_20110803_20200820_02_T1_SR_B4.TIF")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>
# Add your code here
# Compute the NDVI values
# formula: NDVI_ESRI = ((NIR - RED)/(NIR + RED))*100 + 100
band_NDVI = ((band_NIR - band_RED)/(band_NIR + band_RED))*100 + 100
# <<<<<<<<<<<<<<<<<<<<<<<<<<<

band_NDVI.save(f"{BASE_DIR}\\final.TIF")