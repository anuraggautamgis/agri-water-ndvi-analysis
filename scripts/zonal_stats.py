zonal_stats = ndvi_aoi.reduceRegions(

    collection=srd,

    reducer=ee.Reducer.mean(),

    scale=10
)