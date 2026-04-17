# from .legacy


class ToolsLibrary:
    
    class Legacy:
        from .legacy.dem_functions import addMetadata as addMetadata
        from .legacy.dem_functions import channelized_areas as channelized_areas
        from .legacy.dem_functions import getHucSelection as getHucSelection
        from .legacy.dem_functions import MakeCatchList as MakeCatchList
        from .legacy.dem_functions import defineLocalProc as defineLocalProc
        from .legacy.dem_functions import updateResolution as updateResolution
        from .legacy.dem_functions import try_to_delete as try_to_delete
        from .legacy.dem_functions import createBasicDirectories as createBasicDirectories
        from .legacy.dem_functions import loadInterpDict as loadInterpDict
        from .legacy.dem_functions import loadBasicVariablesDict as loadBasicVariablesDict
        from .legacy.dem_functions import loadVariablesDict as loadVariablesDict
        from .legacy.dem_functions import loadFieldNames as loadFieldNames
        from .legacy.dem_functions import nukedir as nukedir
        from .legacy.dem_functions import loadHucs as loadHucs
        from .legacy.dem_functions import setupLoggingNoCh as setupLoggingNoCh
        from .legacy.dem_functions import setupLoggingSimple as setupLoggingSimple
        from .legacy.dem_functions import setupLoggingNew as setupLoggingNew
        from .legacy.dem_functions import setupLogging as setupLogging
        from .legacy.dem_functions import MakeHUClist as MakeHUClist
        from .legacy.dem_functions import tryAddField as tryAddField
        from .legacy.dem_functions import figureItOut as figureItOut
        from .legacy.dem_functions import splitall as splitall
        from .legacy.dem_functions import condenseStats as condenseStats
        from .legacy.dem_functions import testForZero as testForZero
        from .legacy.dem_functions import ZonalStatistics as ZonalStatistics
        from .legacy.dem_functions import ZeroFeaturesError as ZeroFeaturesError
        from .legacy.dem_functions import tno as tno
        from .legacy.dem_functions import calcTop1Distinct as calcTop1Distinct
        from .legacy.dem_functions import intersectingFeaturesUniqueIteration4 as intersectingFeaturesUniqueIteration4
        from .legacy.dem_functions import addCalcJoin as addCalcJoin
        from .legacy.dem_functions import getfields as getfields
        from .legacy.dem_functions import buildSelection as buildSelection
        from .legacy.dem_functions import buildAndSelection as buildAndSelection
        from .legacy.dem_functions import buildStringSelection as buildStringSelection
        from .legacy.dem_functions import buildAntiSelection as buildAntiSelection
        from .legacy.dem_functions import selectByList as selectByList
        from .legacy.dem_functions import antiSelectByList as antiSelectByList
        from .legacy.dem_functions import conByList as conByList
        from .legacy.dem_functions import copyfc as copyfc
        from .legacy.dem_functions import copyfc2 as copyfc2
        from .legacy.dem_functions import copytbl as copytbl
        from .legacy.dem_functions import copytbl2 as copytbl2
        from .legacy.dem_functions import condDelete as condDelete
        from .legacy.dem_functions import getFrsAsList as getFrsAsList
        from .legacy.dem_functions import create_needed_dirs_and_gdbs as create_needed_dirs_and_gdbs
        from .legacy.dem_functions import CreateInitialWs as CreateInitialWs
        from .legacy.dem_functions import findMaxDepth as findMaxDepth
        from .legacy.dem_functions import punchHolesByDepth4 as punchHolesByDepth4
        from .legacy.dem_functions import condenseDataLvls as condenseDataLvls
        from .legacy.dem_functions import condenseTableLvls as condenseTableLvls
        from .legacy.dem_functions import angleDif as angleDif
        from .legacy.dem_functions import curvatureBasedStreams as curvatureBasedStreams
        from .legacy.dem_functions import pruneStreamByLength as pruneStreamByLength
        from .legacy.dem_functions import overflowFRs as overflowFRs
        from .legacy.dem_functions import stationLines10 as stationLines10
        from .legacy.dem_functions import makeTPI as makeTPI
        from .legacy.dem_functions import expandByFst as expandByFst
        from .legacy.dem_functions import createInvertDEM as createInvertDEM
        from .legacy.dem_functions import getFenceEl as getFenceEl
        from .legacy.dem_functions import setupInversionZones as setupInversionZones
        from .legacy.dem_functions import fixByInversion as fixByInversion
        from .legacy.dem_functions import fixByInversionByPath as fixByInversionByPath
        from .legacy.dem_functions import createInvertAndExpand as createInvertAndExpand
        from .legacy.dem_functions import calcDsFd as calcDsFd
        from .legacy.dem_functions import fullZoneByZs as fullZoneByZs
        from .legacy.dem_functions import rescaleExtent as rescaleExtent
        from .legacy.dem_functions import wait_for_timeout as wait_for_timeout
        from .legacy.dem_functions import printParameters as printParameters
        from .legacy.dem_functions import joinDict as joinDict
        from .legacy.dem_functions import visualizeExtent as visualizeExtent
        from .legacy.dem_functions import cleanupOther as cleanupOther
        from .legacy.dem_functions import getMetadata as getMetadata
        from .legacy.dem_functions import copy_text_line_by_line as copy_text_line_by_line
        from .legacy.dem_functions import test_parameters as test_parameters
        from .legacy.dem_functions import prep_arguments_text as prep_arguments_text


# class Basics:
#             _results=dict()
#             def __init__(self,ACPFyear, node=DEP.Computers.Remote.Cylo.Main, uversion = None):
#                 if uversion is not None:
#                     pass
#                 else:
#                     pass
#             def create_directory_paths(self,ACPFyear, node=DEP.Computers.Local.name, uversion = None):
#                 '''Creates the most basic DEP directories, ACPF directory and DEP base directory as strings'''
#                 # depBase - location of most DEP inputs and outputs
#                 # acpfBase - location of DEP/ACPF management data geodatabases
#                 # replace 10.27.15.155 with dep2.ae.iastate.edu, 2.5 GB connection instead of 1 GB
#                 # acpfStart = '\\\\dep2.ae.iastate.edu\\D$\\DEP'#\\Man_Data_ACPF\\dep_ACPF' + ACPFyear
#                 # depBase = '\\\\dep2.ae.iastate.edu\\M$\\DEP'
#                 acpfStart = 'M:\\DEP'# D drive points to '\\\\dep2.ae.iastate.edu\\D$\\DEP' (faster, smaller storage)
#                 depBase = acpfStart#'M:\\DEP'# M drive points to '\\\\dep2.ae.iastate.edu\\M$\\DEP' (bigger, slower storage)
#                 # if 'EL3354-02' in node.upper():# or 'DA214B-11' in node.upper():
#                 #     acpfStart = 'D:\\DEP'
#                 #     depBase = 'M:\\DEP'
#                 # elif 'EL3321-M10' in node.upper():
#                 #     # run everything local on laptop
#                 #     acpfStart = 'C:\\DEP'
#                 #     depBase = 'C:\\DEP'
#                 # else:
#                 #     acpfStart = '\\\\EL3354-02\\D$\\DEP'#\\Man_Data_ACPF\\dep_ACPF' + ACPFyear
#                 #     depBase = '\\\\EL3354-02\\M$\\DEP'

#                 # basedata never changes with version
#                 basedataDir = opj(acpfStart, 'Basedata_Summaries')

#                 # see above
#                 acpfBase = opj(acpfStart + uversion, 'Man_Data_ACPF\\dep_ACPF'+ ACPFyear)
#                 # otherBase is raster residue cover maps
#                 otherBase = opj(depBase, 'Man_Data_Other')
#                 depBase += uversion

#                 return acpfBase, depBase, basedataDir, otherBase, acpfStart

# class Datasets:
    
#     class PathDicts:
        
#%%

# """information needed for DEP paths to know what to do:
# computer you're working with
# user that's doing it
# what drive the data is on
# dataset that you're working with
# what type of information the dataset is 
# what year the dataset is from
# what resolution the dataset is in

# """


# class Tools:
#     class Raster(arcpy.Raster):
#         def AddMetadata(self,outDEM, paraDict, template_file_path, log: logging.Logger|None=None):
#             # Set the standard-format metadata XML file's path
#             # need to load metadata editor via 'import arcpy.metadata as md'
#             # outDEM = raster to receive updated metadata
#             # paraDict = dictionary of key/value pairs to be stored in metadata
#             #   values stored include things like analyst, lidar acquisition date, etc.
#             # template_file_path = a template to load a basic summary from
#             # log = otional logging of error messages to a log file
#             # scriptPath = sys.path[0]
#             try:
#                 src_file_path = template_file_path

#                 # Get the target item's Metadata object
#                 tgt_item_md = arcpy.metadata.Metadata(outDEM)    

#                 # Import the ACPF metadata content to the target item
#                 if not tgt_item_md.isReadOnly:
#                     tgt_item_md.importMetadata(src_file_path)
#                     tgt_item_md.title = os.path.split(outDEM)[1]
#                     tgt_item_md.credits = 'Analyst: %s' % os.getlogin()#getpass.getuser()

#                     src_desc = tgt_item_md.summary
#                     if src_desc == None:
#                         src_desc = ''
#                     for key, value in paraDict.items():  
#                         src_desc = src_desc + ('%s %s' % (key, value))
#                     tgt_item_md.summary = src_desc
                    
#                     tgt_item_md.save()

#             except TypeError as e:
#                 print('handling as exception')
#         ##        log.debug(e.message)
#                 tb_str=''.join(traceback.format_exception(None, e, e.__traceback__))
#                 # if sys.version_info.major == 2:
#                 #     arcpy.AddError(e.message)
#                 #     print(e.message)
#                 #     log.warning(e.message)
#                 # elif sys.version_info.major == 3:
                
#                 arcpy.AddError(tb_str)
#                 print(tb_str)
#                 if log is not None:
#                     log.warning(tb_str)

#                 # tb = sys.exc_info()[2]
#                 # tbinfo = traceback.format_tb(tb)[0]

#                 # Concatenate information together concerning the error into a message string
#                 # pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
#                 # # Return python error messages for use in script tool or Python Window
#                 # arcpy.AddError(pymsg)
#                 # # Print Python error messages for use in Python / Python Window
#                 # print(pymsg + "\n")
#                 # if log is not None:
#                 #     log.warning(pymsg)

#                 if arcpy.GetMessages(2) not in tb_str:
#                     msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
#                     arcpy.AddError(msgs)
#                     print(msgs)
#                     if log is not None:
#                         log.warning(msgs)

#             except:
#                 print('handling as except')
#                 # Get the traceback object
#                 tb = sys.exc_info()[2]
#                 tbinfo = traceback.format_tb(tb)[0]

#                 # Concatenate information together concerning the error into a message string
#                 pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
#                 # Return python error messages for use in script tool or Python Window
#                 arcpy.AddError(pymsg)
#                 # Print Python error messages for use in Python / Python Window
#                 print(pymsg + "\n")
#                 if log is not None:
#                     log.warning(pymsg)

#                 if arcpy.GetMessages(2) not in pymsg:
#                     msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
#                     arcpy.AddError(msgs)
#                     print(msgs)
#                     if log is not None:
#                         log.warning(msgs)

#     class Feature:
        
#         def HucSelectionString(self,pdcAcres, pdcSlope, thresh):

#             selStr = pdcAcres + ' >= 15 AND ' + pdcSlope + ' > 0 AND (( AGarea.VALUE_1 * 0.000247) / ' + pdcAcres + ' > %s)' %(thresh)

#             return selStr
#         def MakeCatchList(self,inCATCHFCls, isAG, pdChnl, pdCatch, nAG, inHUC,  log:logging.Logger):
#             '''Makes a list of catchments for DEP random sampling. Sorts results by
#             percent agriculture and threshold adjusts to minimize number of watersheds
#             processed.
#             This was copied from cmd_gen1Flowpath_v6.py on 2020-02-20 to minimize code copies'''
#             try:
#                 log.info("Select Catchments...")
#                 # Create column names
#                 pdcAcres = os.path.basename(pdCatch) + ".Acres"#"pdCatch" + huc12 + "_" + interpType + ".Acres"
#                 pdcSlope = os.path.basename(pdChnl) + ".Slope"#"pdChnl" + huc12 + "_" + interpType + ".Slope"
#                 pdcWSNO = os.path.basename(pdCatch) + ".WSNO"#"pdCatch" + huc12 + "_" + interpType + ".WSNO"


#                 # Tabulate Ag in each catchment (WSNO)
#                 taIsAg = arcpy.sa.TabulateArea(inCATCHFCls, "WSNO", isAG, "VALUE", "AGarea.dbf")
                        
#                 # catchLayer = arcpy.MakeFeatureLayer_management(inCATCHFCls, "CTCH.lyr")
#                 # channelLayer = arcpy.MakeFeatureLayer_management(pdChnl, "CHNL.lyr")
#                 # arcpy.AddJoin_management(catchLayer, "WSNO", taIsAg, "WSNO")
#                 # arcpy.AddJoin_management(catchLayer, "WSNO", channelLayer, "WSNO") 
                        
#                 catchLayer = arcpy.management.MakeFeatureLayer(inCATCHFCls, "CTCH.lyr")
#                 channelLayer = arcpy.management.MakeFeatureLayer(pdChnl, "CHNL.lyr")
#                 arcpy.management.AddJoin(catchLayer, "WSNO", taIsAg, "WSNO")
#                 arcpy.management.AddJoin(catchLayer, "WSNO", channelLayer, "WSNO") 

#                 # Select Catchments GT 25% Ag and 15 Acres
#                 thresh = .25#75
#                 maxCatch = 150
#                 minCatch = 100
#         ####        selStr = '"%s.Acres" >= 15 AND "%s.Slope" > 0 AND (( AGarea.VALUE_1 * 0.000247) / "%s.Acres" > %s)' %(os.path.basename(pdCatch), os.path.basename(pdChnl), os.path.basename(pdCatch), thresh)
#                 selStr = self.HucSelectionString(pdcAcres, pdcSlope, thresh)

#             ## switched to list comprehension to handle errors when no catchments returned (del row would fail)
#             ## bkgelder - 2019/03/20
#             ## revised again to use with statement (for handling 0 returns)
#             ## bkgelder - 2019/09/06
#         ##        CatchList = [str(int(row[0])) for row in arcpy.da.SearchCursor(catchLayer, ["pdCatch%s.WSNO" %(inHUC)], selStr)]
#                 CatchList = []
#                 with arcpy.da.SearchCursor(catchLayer, [pdcWSNO], selStr) as scur:
#         ####        with arcpy.da.SearchCursor(catchLayer, ["%s.WSNO" %(os.path.basename(pdCatch))], selStr) as scur:
#                     for srow in scur:
#                         CatchList.append(srow[0])
                                                        
                
#                 catchCount = len(CatchList)
#                 log.info("ag sub-catchment count: " + str(catchCount) + " at " + str(thresh))

#                 if catchCount > 0:
#                     # Set higher or lower Catchments % Ag criteria to focus on subcatchments (in high ag), area GT 15 Acres
#                     if (catchCount < minCatch) or (catchCount > maxCatch):
#                         if catchCount > maxCatch:
#                             while catchCount > maxCatch and thresh < 0.975:
#                                 thresh += 0.025
#                                 selStr = self.HucSelectionString(pdcAcres, pdcSlope, thresh)
#         ####                        selStr = '"%s.Acres" >= 15 AND "%s.Slope" > 0 AND (( AGarea.VALUE_1 * 0.000247) / "%s.Acres" > %s)' %(os.path.basename(pdCatch), os.path.basename(pdChnl), os.path.basename(pdCatch), thresh)
                        
#                                 CatchList = [str(int(row[0])) for row in arcpy.da.SearchCursor(catchLayer, [pdcWSNO], selStr)]
#         ####                        CatchList = [str(int(row[0])) for row in arcpy.da.SearchCursor(catchLayer, ["%s.WSNO" %(os.path.basename(pdCatch))], selStr)]
#                                 catchCount = len(CatchList)
#                                 log.info("   loop sub-catchment count: " + str(catchCount) + " at " + str(thresh))

#                         elif catchCount < minCatch:
#                             while catchCount < minCatch and thresh > 0.25:
#                                 thresh -= 0.025
#                                 selStr = self.HucSelectionString(pdcAcres, pdcSlope, thresh)
#         ####                        selStr = '"%s.Acres" >= 15 AND "%s.Slope" > 0 AND (( AGarea.VALUE_1 * 0.000247) / "%s.Acres" > %s)' %(os.path.basename(pdCatch), os.path.basename(pdChnl), os.path.basename(pdCatch), thresh)

#                                 CatchList = [str(int(row[0])) for row in arcpy.da.SearchCursor(catchLayer, [pdcWSNO], selStr)]
#         ####                        CatchList = [str(int(row[0])) for row in arcpy.da.SearchCursor(catchLayer, ["%s.WSNO" %(os.path.basename(pdCatch))], selStr)]
#                                 catchCount = len(CatchList)
#                                 log.info("   loop sub-catchment count: " + str(catchCount) + " at " + str(thresh))
#                 else:
#                     log.warning("agricultural sub-catchment count is 0, quitting")
                
#                 arcpy.management.Delete(catchLayer)
#                 arcpy.management.Delete(channelLayer)
                
#                 return(CatchList)
#             except:
                
#                 # Get the traceback object
#                 #
#                 tb = sys.exc_info()[2]
#                 tbinfo = traceback.format_tb(tb)[0]

#                 # Concatenate information together concerning the error into a message string
#                 #
#                 pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
#                 msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"

#                 # Return python error messages for use in script tool or Python Window
#                 #
#                 ##            arcpy.AddError(pymsg)
#                 ##            arcpy.AddError(msgs)

#                 # Print Python error messages for use in Python / Python Window
#                 #
#                 log.warning(pymsg)
#                 log.warning(msgs)

#                 log.warning('failure on: ' + inHUC)