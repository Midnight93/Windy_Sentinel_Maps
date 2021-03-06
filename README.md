# Windy Sentinel Maps

<img src=media/good_boy.jpg width="400" align="middle" >

## Windy POST Request

```bash
API_ENDPOINT = "https://api.windy.com/api/point-forecast/v2"

Key = 'Your API KEY'
```

## Documentation

Requests are sent to the following endpoint: POST https://api.windy.com/api/point-forecast/v2 with the following body:

```json
{
    "lat": 49.809,
    "lon": 16.787,
    "model": "desired_model",
    "parameters": ["desired_parameter_1", "desired_parameter_2", ...],
    "levels": ["optionally_desired_gh_level_1", ...],
    "key": "your_API_key"
}
```
For example:

```json
{
    "lat": 49.809,
    "lon": 16.787,
    "model": "gfs",
    "parameters": ["wind", "dewpoint", "rh", "pressure"],
    "levels": ["surface", "800h", "300h"],
    "key": "abcd123"
}
```


## Tree Project

```bash
├── LICENSE
├── media
│   ├── dem.jpg
│   ├── doge.jpg
│   ├── good_boy.jpg
│   ├── ndvi_formula.gif
│   ├── ndvi.png
│   ├── ndwi_formula.gif
│   ├── ndwi.png
│   ├── Sentinel-2-band-characteristics.png
│   └── sentinel_co.png
├── opencv
│   ├── Dem_Analysis_OpenCV.ipynb
│   └── slicer_for_dataset_preparation.py
├── README.md
├── sentinel
│   ├── dem
│   │   └── eo_browser
│   │       └── dem.js
│   ├── ndvi
│   │   ├── eo_browser
│   │   │   └── ndvi.js
│   │   └── python
│   │       └── NDVI.ipynb
│   └── ndwi
│       └── ndwi.js
├── sentinelsat
│   ├── AUTHORS.rst
│   ├── CHANGELOG.rst
│   ├── CONTRIBUTE.rst
│   ├── docs
│   │   ├── api_overview.rst
│   │   ├── api_reference.rst
│   │   ├── changelog.rst
│   │   ├── cli.rst
│   │   ├── common_issues.rst
│   │   ├── conf.py
│   │   ├── index.rst
│   │   ├── install.rst
│   │   ├── make.bat
│   │   ├── Makefile
│   │   └── readthedocs-requirements.txt
│   ├── LICENSE
│   ├── MANIFEST.in
│   ├── README.rst
│   ├── requirements.txt
│   ├── sentinelsat
│   │   ├── exceptions.py
│   │   ├── __init__.py
│   │   ├── __main__.py
│   │   ├── products.py
│   │   ├── scripts
│   │   │   ├── cli.py
│   │   │   └── __init__.py
│   │   └── sentinel.py
│   ├── setup.cfg
│   ├── setup.py
│   └── tests
│       ├── conftest.py
│       ├── custom_serializer.py
│       ├── fixtures
│       │   ├── clean_cassettes.sh
│       │   ├── expected_search_footprints_s1.geojson
│       │   ├── expected_search_footprints_s2.geojson
│       │   ├── map_boundaries_lat.geojson
│       │   ├── map_boundaries_lon.geojson
│       │   ├── map_download.geojson
│       │   ├── map.geojson
│       │   ├── map_nested.geojson
│       │   ├── map_z.geojson
│       │   ├── odata_response_full.yml
│       │   ├── odata_response_short.yml
│       │   ├── server_maintenance.html
│       │   └── vcr_cassettes
│       │       ├── data
│       │       │   ├── manifest.safe
│       │       │   ├── map-overlay.kml
│       │       │   ├── S1A_WV_OCN__2SSH_20150603T092625_20150603T093332_006207_008194_521E.zip
│       │       │   ├── S1A_WV_OCN__2SSV_20150526T081641_20150526T082418_006090_007E3E_104C.zip
│       │       │   ├── S1A_WV_OCN__2SSV_20150526T211029_20150526T211737_006097_007E78_134A.zip
│       │       │   ├── S2A_MSIL2A_20201007T022601_N0214_R046_T49MFN_20201007T064142-ql.jpg
│       │       │   ├── S2B_MSIL2A_20201007T121649_N0214_R123_T23FQB_20201007T160401-ql.jpg
│       │       │   └── S2B_MSIL2A_20201007T131939_N0214_R124_T28XEK_20201007T160755-ql.jpg
│       │       ├── products_fixture.yaml
│       │       ├── quicklook_products.yaml
│       │       ├── smallest_archived_products.yaml
│       │       ├── smallest_online_products.yaml
│       │       ├── test_api_query_format_escape_spaces.yaml
│       │       ├── test_area_relation.yaml
│       │       ├── test_check_existing.yaml
│       │       ├── test_cli_geometry_alternatives.yaml
│       │       ├── test_cli_gnss.yaml
│       │       ├── test_cloud_flag_url.yaml
│       │       ├── test_count.yaml
│       │       ├── test_date_arithmetic.yaml
│       │       ├── test_download_all_lta.yaml
│       │       ├── test_download_all_one_fail.yaml
│       │       ├── test_download_all_quicklooks_one_fail.yaml
│       │       ├── test_download_all_quicklooks.yaml
│       │       ├── test_download_all.yaml
│       │       ├── test_download_invalid_id.yaml
│       │       ├── test_download_many.yaml
│       │       ├── test_download_product_nodes.yaml
│       │       ├── test_download_quicklook_invalid_id.yaml
│       │       ├── test_download_quicklook.yaml
│       │       ├── test_download_single_quicklook.yaml
│       │       ├── test_download_single.yaml
│       │       ├── test_download.yaml
│       │       ├── test_footprints_cli.yaml
│       │       ├── test_footprints_s1.yaml
│       │       ├── test_format_date.yaml
│       │       ├── test_get_product_info_bad_key.yaml
│       │       ├── test_get_product_odata_full.yaml
│       │       ├── test_get_product_odata_short_with_missing_online_key.yaml
│       │       ├── test_get_product_odata_short.yaml
│       │       ├── test_get_products_size.yaml
│       │       ├── test_get_stream.yaml
│       │       ├── test_info_cli.yaml
│       │       ├── test_instrument_flag.yaml
│       │       ├── test_invalid_query.yaml
│       │       ├── test_is_online.yaml
│       │       ├── test_large_query.yaml
│       │       ├── test_limit_flag.yaml
│       │       ├── test_location_cli.yaml
│       │       ├── test_name_search_multiple.yaml
│       │       ├── test_name_search.yaml
│       │       ├── test_no_auth_netrc.yaml
│       │       ├── test_order_by_flag.yaml
│       │       ├── test_order_by.yaml
│       │       ├── test_placename_to_wkt_invalid.yaml
│       │       ├── test_placename_to_wkt_valid.yaml
│       │       ├── test_product_flag.yaml
│       │       ├── test_product_node_download_single_with_filter.yaml
│       │       ├── test_product_node_download_single.yaml
│       │       ├── test_query_by_names.yaml
│       │       ├── test_quote_symbol_bug.yaml
│       │       ├── test_repeated_keywords.yaml
│       │       ├── test_returned_filesize.yaml
│       │       ├── test_s2_cloudcover.yaml
│       │       ├── test_sentinel1_flag.yaml
│       │       ├── test_sentinel2_flag.yaml
│       │       ├── test_sentinel3_flag.yaml
│       │       ├── test_SentinelAPI_connection.yaml
│       │       ├── test_SentinelAPI_wrong_credentials.yaml
│       │       ├── test_small_query.yaml
│       │       ├── test_too_long_query.yaml
│       │       ├── test_unicode_support.yaml
│       │       └── test_uuid_search.yaml
│       ├── __init__.py
│       ├── pytest.ini
│       ├── test_cli.py
│       ├── test_docs.py
│       ├── test_download.py
│       ├── test_geographic.py
│       ├── test_misc.py
│       ├── test_odata.py
│       ├── test_opensearch.py
│       └── test_pandas.py
└── windy
    ├── Maps_html
    │   ├── index.html
    │   └── script.js
    └── Web Service
        ├── post_request.py
        └── text.json

```

## Usage

### POST Request Windy Point Forecast API

```bash
python3 post_request.py
```

```bash
Usage: post_request.py [-h] --api_key API_KEY --lat LAT --lon LON --model MODEL [--output OUTPUT]

optional arguments:
  -h, --help         show this help message and exit
  --api_key API_KEY  Your API Keys
  --lat LAT          Latitude
  --lon LON          Longitude
  --model MODEL      Reference model
  --output OUTPUT    Define your output file name ex. output.json
```
### Large Image - Dataset Preparation for Annotations (Object Detection)
```bash
python3 slicer_for_dataset_preparation.py
```

```bash
Usage: slicer_for_dataset_preparation.py [-h] --image IMAGE --slicer SLICER

optional arguments:
  -h, --help       show this help message and exit
  --image IMAGE    Your Image path
  --slicer SLICER  Your slicer value (es. 8x8 = value --> 64)
```
#### Example
```bash
python3 slicer_for_dataset_preparation.py --image ./image.png --slicer 64
```
## Sentinel-1, Sentinel-2, Sentinel-3

<img src=media/doge.jpg width="400" align="middle" >

### Sentinel-1

The Sentinel-1 mission comprises a constellation of two polar-orbiting satellites, operating day and night performing C-band synthetic aperture radar imaging, enabling them to acquire imagery regardless of the weather.

Sentinel-1 will work in a pre-programmed operation mode to avoid conflicts and to produce a consistent long-term data archive built for applications based on long time series.

Sentinel-1 is the first of the five missions that ESA is developing for the Copernicus initiative.[1]

### Sentinel-2

#### Bands

<img src=media/Sentinel-2-band-characteristics.png width="400"  align="middle" >


The Copernicus Sentinel-2 mission comprises a constellation of two polar-orbiting satellites placed in the same sun-synchronous orbit, phased at 180° to each other. It aims at monitoring variability in land surface conditions, and its wide swath width (290 km) and high revisit time (10 days at the equator with one satellite, and 5 days with 2 satellites under cloud-free conditions which results in 2-3 days at mid-latitudes) will support monitoring of Earth's surface changes.

### Sentinel-3

The main objective of the Sentinel-3 mission is to measure sea surface topography, sea and land surface temperature, and ocean and land surface colour with high accuracy and reliability to support ocean forecasting systems, environmental monitoring and climate monitoring.

The Sentinel-3 Mission Guide provides a high-level description of the mission objectives, satellite description and ground segment. It also covers an introduction to heritage missions, thematic areas and services, orbit characteristics and coverage, instrument payloads and data products

### NDVI

The well known and widely used NDVI is a simple, but effective index for quantifying green vegetation. It normalizes green leaf scattering in Near Infra-red wavelengths with chlorophyll absorption in red wavelengths.

The value range of the NDVI is -1 to 1. Negative values of NDVI (values approaching -1) correspond to water. Values close to zero (-0.1 to 0.1) generally correspond to barren areas of rock, sand, or snow. Low, positive values represent shrub and grassland (approximately 0.2 to 0.4), while high values indicate temperate and tropical rainforests (values approaching 1). It is a good proxy for live green vegetation; see [4] for details.

<img src=media/ndvi.png width="400"  align="middle" >

|        Region:       | Sicily |
|:--------------------:|------------------------------------------------------------------|
|       Latitude:      | 37° 30' 0.0000'' N                                               |  
|      Longitude:      | 15° 5' 25.0008'' E                                               |  
|    Lat/Long (dec):   | 37.5, 15.090278                                                  |  
| Software used_:      | SNAP                                                             |  


#### Formula

![](media/ndvi_formula.gif)

### NDWI

<img src=media/ndwi.png align="middle">

|        Region:       | Adabozato, Isalo, Miandrivazo District, Menabe Region, Madagascar |
|:--------------------:|-------------------------------------------------------------------|
|       Latitude:      | 19° 43' 0" S                                                      |  
|      Longitude:      | 45° 22' 0" E                                                      |  
|    Lat/Long (dec):   | -19.71667,45.36667                                                |  
| Köppen climate type: | Aw : Tropical savanna, wet                                        |  
| Software used_:      | SNAP                                                             |  

The NDWI is used to monitor changes related to water content in water bodies. As water bodies strongly absorb light in visible to infrared electromagnetic spectrum, NDWI uses green and near infrared bands to highlight water bodies. It is sensitive to built-up land and can result in over-estimation of water bodies. The index was proposed by McFeeters, 1996.[5]

#### Formula
![](media/ndwi_formula.gif)

### DEM

A digital elevation model (DEM) is a 3D computer graphics representation of elevation data to represent terrain, commonly of a planet (e.g. Earth), moon, or asteroid. A "global DEM" refers to a discrete global grid. DEMs are used often in geographic information systems, and are the most common basis for digitally produced relief maps.[6]

![](media/dem.jpg)

|        Region:       |Rome, Italy |
|:--------------------:|-------------------------------------------------------------------|
|       Latitude:      | 41°54'39"24 N                                                     |  
|      Longitude:      | 12°28'54"48 E                                                 |  
|    Lat/Long (dec):   | 41,9109; 12,4818                                              |  
| Software used_:      | SentinelHub                                                       |  

Authors of the scripts for Sentinel Hub

* Peter Gabrovšek
* Marko Repše
* Monja Šebela

### Measuring Air Pollution From Space (CO - Carbon monoxide)


Gaseous Air Pollutants of Primary Concern
Air pollution is a release of various gases into the atmosphere, such as solids and dispersed liquid aerosols which cannot be absorbed in the environment. There are six common air pollutants also known as criteria air pollutants defined by the U.S. Environmental Protection Agency (EPA) which can harm our health and the environment:

* Sulfur dioxide (SO₂)
* Nitrogen dioxide (NO₂)
* Carbon monoxide (CO)
* Ozone (O₃)
* Particulate matter (PM)
* Lead

#### Info Data

![](media/sentinel_co.png)

* Mission: Sentinel
* Orbit number (start): 18530
* Processing level: L2
* Processing mode: Near real time
* Processing mode abbreviation: NRTI
* Processor version: 010400
* Product type: L2__CO____
* Product type description: Carbon Monoxide
* Revision number: 01
* Sensing start: 2021-05-11T12:07:57.000Z
* Sensing stop: 2021-05-11T12:13:10.000Z


## References
|   |  Name | Link  |
|---|---|---|
|[1]| Sentinel-1  |https://sentinel.esa.int/web/sentinel/missions/sentinel-1   
|[2]| Sentinel-2  |https://sentinel.esa.int/web/sentinel/missions/sentinel-2
|[3]| Sentinel-3  |https://sentinel.esa.int/web/sentinel/missions/sentinel-3  
|[4]| NDVI  |Wikipedia, Normalized Difference Vegetation Index
|[5]| NDWI  |Wikipedia, Normalized Difference Water Index
|[6]| DEM   |Wikipedia, Digital elevation model
