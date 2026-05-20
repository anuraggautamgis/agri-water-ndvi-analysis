# Agricultural Water Demand & NDVI Analysis

## Overview
This project explores the spatial relationship between agricultural water demand and vegetation health across Sangareddy district using Sentinel-2 NDVI and irrigation demand estimates.

## Objectives
- Derive NDVI for Kharif 2021 using Sentinel-2 imagery
- Compare vegetation health with mandal-level irrigation demand
- Identify zones exhibiting potential vegetation-water stress

## Workflow
1. Sentinel-2 preprocessing using Google Earth Engine Python API
2. QA60 cloud masking
3. NDVI computation using Sentinel-2 Band 8 (NIR) and Band 4 (Red)
4. Zonal statistics using mandal boundaries
5. Correlation analysis
6. Visualization in QGIS

## Tools & Technologies
- Google Earth Engine Python API
- Python
- QGIS
- Google Sheets
- Sentinel-2 Surface Reflectance

## Water Demand Estimation Method

- Mandal-level agricultural water demand was estimated using proportional crop-area allocation.

- The total district irrigation demand for Sangareddy (1830.3 MCM for 2021) was spatially distributed across
mandals using 2021 crop-area statistics.

- For administrative units lacking direct historical irrigation estimates in the 2018 District Irrigation Plan (DIP), proportional redistribution was performed using updated crop-area shares from the latest available agricultural records.

- This approach provides an approximate spatial representation of irrigation demand suitable for exploratory regional analysis.

## Key Findings
- Western mandals exhibited relatively higher irrigation demand
- Mogudampally showed comparatively strong vegetation condition with moderate demand
- Raikode exhibited comparatively lower NDVI alongside elevated estimated irrigation demand, indicating potential vegetation-water stress conditions

## Limitations
- NDVI was derived specifically for the Kharif 2021 season.
- Agricultural water demand estimates included mixed crop cycles, including long-duration crops such as sugarcane.
- Temporal mismatch between seasonal NDVI and annual/mixed crop demand may influence correlation strength.
- Results should be interpreted as exploratory spatial indicators rather than crop-specific irrigation forecasts.

## Data Sources

- Sentinel-2 Surface Reflectance imagery accessed through Google Earth Engine
- Sangareddy District Irrigation Plan (DIP) 2018
- 2021 mandal-level crop area statistics
- OpenStreetMap administrative boundaries (processed in QGIS)

## Future Improvements
- Crop-wise seasonal filtering
- Multi-temporal NDVI analysis
- Integration of rainfall and groundwater datasets
- Time-series vegetation monitoring

## Repository Structure

```text
data/           # Input boundaries and exported datasets
notebooks/      # Exploratory analysis and visualization
outputs/        # Final maps, charts, workflow graphics, report
scripts/     # GEE Python API scripts
```