![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white) ![google_colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)

# Predictive System Using Metar Data (SBJS)

> **Main database:**  https://mesonet.agron.iastate.edu/request/download.phtml?network=BR__ASOS

![image](https://user-images.githubusercontent.com/60454486/167980061-04c1055b-6c96-42ba-8f43-40e6da65a562.png)


The IEM maintains an ever growing archive of automated airport weather observations from around the world! These observations are typically called 'ASOS' or sometimes 'AWOS' sensors. A more generic term may be METAR data, which is a term that describes the format the data is transmitted as. This archive simply provides the as-is collection of historical observations, very little quality control is done. More details on this dataset are here: https://mesonet.agron.iastate.edu/info/datasets/metar.html

* **ASOS User's Guide:** https://www.weather.gov/media/asos/aum-toc.pdf

*  **Tools/Libaries:** Here (https://github.com/akrherz/iem/blob/main/scripts/asos/iem_scraper_example.py) is a python script example  that automates the download of data from this interface. A community user has contributed R language  version of the python script. There is also a riem R package  allowing for easy access to this archive.

---
> **Decoder:** 

```
Source: <https://onedrive.live.com/?cid=3FCCB15EB1D3C6E0&mid=DB6B1FEDF4FAA3AA%2114487&mcid=DB6B1FEDF4FAA3AA&sd=1&id=3FCCB15EB1D3C6E0%2121492&parId=3FCCB15EB1D3C6E0%2121459&o=OneUp>

Q     - Pressão barométrica - 0
----------------------------------------
FEW   - Poucas - 100
SCT   - Esparsa - 101
BKN   - Nublado - 110
OVC   - Encoberto - 111
----------------------------------------
CB    - Cumulunimbus - 99
TCU   - Towering cumulus - 999
NSC   - No significative clouds - 912
CAVO (CAVOK) - Clouds and visibility OK - 9123
----------------------------------------------
V     - 1
RE    - Recente - 11
VC    - Vizinhança - 12
TS    - Trovoada - 38
RETS  - Recente trovoada - 1138
BR    - Névoa úmida - 70 
DZ    - Chuvisco - 71
RA    - Chuva - 77
SH    - Chuva - 77
VCSH  - Vicinity Showers - 1277
HZ    - Névoa seca - 78
FG    - Nevoeiro - 79
RERA  - Recente chuva - 1177
TSRA  - Trovoada com chuva - 3877
----------------------------------------------
WS    - Windshear - 69
GXX   - Rajada velocidade XX - 6XX
NIL   - No item listed - 000
```

---
> **Metadata:**
---
* **station:**
three or four character site identifier
* **valid:**
timestamp of the observation
* **tmpf:**
Air Temperature in Fahrenheit, typically @ 2 meters
* **dwpf:**
Dew Point Temperature in Fahrenheit, typically @ 2 meters
* **relh:**
Relative Humidity in %
* **drct:**
Wind Direction in degrees from *true* north
* **sknt:**
Wind Speed in knots
* **p01i:**
One hour precipitation for the period from the observation time to the time of the previous hourly precipitation reset. This varies slightly by site. Values are in inches. This value may or may not contain frozen precipitation melted by some device on the sensor or estimated by some other means. Unfortunately, we do not know of an authoritative database denoting which station has which sensor.
* **alti:**
Pressure altimeter in inches
* **mslp:**
Sea Level Pressure in millibar
* **vsby:**
Visibility in miles
* **gust:**
Wind Gust in knots
* **skyc1:**
Sky Level 1 Coverage
* **skyc2:**
Sky Level 2 Coverage
* **skyc3:**
Sky Level 3 Coverage
* **skyc4:**
Sky Level 4 Coverage
* **skyl1:**
Sky Level 1 Altitude in feet
* **skyl2:**
Sky Level 2 Altitude in feet
* **skyl3:**
Sky Level 3 Altitude in feet
* **skyl4:**
Sky Level 4 Altitude in feet
* **wxcodes:**
Present Weather Codes (space seperated)
* **feel:**
Apparent Temperature (Wind Chill or Heat Index) in Fahrenheit
* **ice_accretion_1hr:**
Ice Accretion over 1 Hour (inches)
* **ice_accretion_3hr:**
Ice Accretion over 3 Hours (inches)
* **ice_accretion_6hr:**
Ice Accretion over 6 Hours (inches)
* **peak_wind_gust:**
Peak Wind Gust (from PK WND METAR remark) (knots)
* **peak_wind_drct:**
Peak Wind Gust Direction (from PK WND METAR remark) (deg)
* **peak_wind_time:**
Peak Wind Gust Time (from PK WND METAR remark)
* **metar:**
unprocessed reported observation in METAR format

---
> **Obs:** for *Sky Coverage* values:
- **FEW**   -  few clouds
- **SCT**   - sparse
- **BKN**   - cloudy
- **OVC**   - overcast
---
