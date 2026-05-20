ndvi = image.normalizedDifference(["B8","B4"]).rename("NDVI")
ndvi_aoi = ndvi.clip(aoi)