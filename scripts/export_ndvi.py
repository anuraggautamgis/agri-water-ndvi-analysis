raster_task = ee.batch.Export.image.toDrive(

    image=ndvi_aoi,

    description="Sangareddy_Kharif_2021_NDVI",

    folder="GEE_Exports",

    fileNamePrefix="srd_ndvi_kharif_2021",

    region=aoi,

    scale=10,

    maxPixels=1e13
)

raster_task.start()