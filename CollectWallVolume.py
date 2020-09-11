from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory
wall_collector=FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType()

total_volume=0.0
for wall in wall_collector:
    vol_param=wall.LookupParameter("Volume")
    if vol_param:
        total_volume+=vol_param.AsDouble()

print ("Total Volume: {}".format(total_volume))