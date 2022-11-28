# buffer a shm at 1km to create a OneRange map

#import sytem modules
import arcpy
from arcpy import env
from arcpy.sa import *
arcpy.env.overwriteOutput = True

#set workspaces and variables
SHM = r"S:\Projects\SHM_Program\Communications\Data\Models\SYN_OneRangeModels\Cglab_159260_rf_20221007\Cglab_159260_rf_20221007\Cglab_159260_rf_20221007_masked_continuous.tif" #update with SHM raster
binarySHM = r"S:\Projects\SHM_Program\Communications\Data\Intermediate\Cgla.gdb\Cglab_SHMbinary" #update output name and location
polySHM = r"S:\Projects\SHM_Program\Communications\Data\Intermediate\Cgla.gdb\Cglab_SHM" #update output name and location
buff1km = r"S:\Projects\SHM_Program\Communications\Data\Intermediate\Cgla.gdb\Cglab_SHM_buff1km" #udpdate output name and location
print ("variables set")

#make model binary, set the thresholded value to be kept to 1 and everything below it to NODATA
out_raster = arcpy.sa.Reclassify(SHM, "VALUE", "0 0.72999 NODATA;0.73 1 1", "DATA"); out_raster.save(binarySHM)
print ("binary raster created")

#if model is already binary proceed to the next step

#turn binary raster into polygon
arcpy.conversion.RasterToPolygon(binarySHM, polySHM, "SIMPLIFY", "Value", "SINGLE_OUTER_PART", None)
print ("shm raster to poly")

#if model is already a polygon, proceed to the next step and update the polySHM with the location of polygonized SHM

#buffer shm polygon by 1 km to create a One Range map
arcpy.analysis.Buffer(polySHM, buff1km, "1 Kilometers", "FULL", "ROUND", "ALL", None, "PLANAR")
print ("buffer 1 complete")
