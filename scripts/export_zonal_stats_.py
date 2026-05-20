csv_task = ee.batch.Export.table.toDrive(

    collection=zonal_stats,

    description="Sangareddy_Kharif_2021_NDVI_Zonal_Stats",

    folder="GEE_Exports",

    fileNamePrefix="srd_ndvi_zonal_stats_2021",

    fileFormat="CSV"
)

csv_task.start()