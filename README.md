# Windy Post request and JSON File

<img src="https://www.gannett-cdn.com/presto/2020/11/19/PTCN/7d946ccb-7a6e-4456-9a56-416076fc7311-EnIZWibVkAAdWqP.jpg" width="400"  align="middle" >

## Windy Sentinel Maps

```bash
API_ENDPOINT = "https://api.windy.com/api/point-forecast/v2"

Key = 'Your API KEY'
```

## Usage

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
## Sentinel-1, Sentinel-2, Sentinel-3


### Sentinel-1

The Sentinel-1 mission comprises a constellation of two polar-orbiting satellites, operating day and night performing C-band synthetic aperture radar imaging, enabling them to acquire imagery regardless of the weather.

Sentinel-1 will work in a pre-programmed operation mode to avoid conflicts and to produce a consistent long-term data archive built for applications based on long time series.

Sentinel-1 is the first of the five missions that ESA is developing for the Copernicus initiative.[1]

### Sentinel-2

<img src=image/doge.jpg width="400" align="middle" >

#### Bands

<img src=media/Sentinel-2-band-characteristics.png width="400"  align="middle" >


The Copernicus Sentinel-2 mission comprises a constellation of two polar-orbiting satellites placed in the same sun-synchronous orbit, phased at 180° to each other. It aims at monitoring variability in land surface conditions, and its wide swath width (290 km) and high revisit time (10 days at the equator with one satellite, and 5 days with 2 satellites under cloud-free conditions which results in 2-3 days at mid-latitudes) will support monitoring of Earth's surface changes.

### Sentinel-3

The main objective of the Sentinel-3 mission is to measure sea surface topography, sea and land surface temperature, and ocean and land surface colour with high accuracy and reliability to support ocean forecasting systems, environmental monitoring and climate monitoring.

The Sentinel-3 Mission Guide provides a high-level description of the mission objectives, satellite description and ground segment. It also covers an introduction to heritage missions, thematic areas and services, orbit characteristics and coverage, instrument payloads and data products

### NDVI

<img src=media/ndvi.bmp width="400"  align="middle" >

#### Formula

<img src="https://render.githubusercontent.com/render/math?math=(B8-B4)/(B8+B4)" align="middle">

### NDWI

#### Formula 
<img src="https://render.githubusercontent.com/render/math?math=(B3-B8)/(B3+B8)" align="middle">

## References
|   |  Name | Link  |
|---|---|---|
|[1]| Sentinel-1  |https://sentinel.esa.int/web/sentinel/missions/sentinel-1   
|[2]| Sentinel-2  |https://sentinel.esa.int/web/sentinel/missions/sentinel-2
|[3]| Sentinel-3  |https://sentinel.esa.int/web/sentinel/missions/sentinel-3  
