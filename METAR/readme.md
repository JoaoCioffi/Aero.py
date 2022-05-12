![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white) ![google_colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)

# Predictive System Using Metar Data (SBJS)

> **Main database:**  https://mesonet.agron.iastate.edu/request/download.phtml?network=BR__ASOS

The IEM maintains an ever growing archive of automated airport weather observations from around the world! These observations are typically called 'ASOS' or sometimes 'AWOS' sensors. A more generic term may be METAR data, which is a term that describes the format the data is transmitted as. This archive simply provides the as-is collection of historical observations, very little quality control is done. More details on this dataset are here: https://mesonet.agron.iastate.edu/info/datasets/metar.html

* **ASOS User's Guide:** https://www.weather.gov/media/asos/aum-toc.pdf

*  **Tools/Libaries:** Here (https://github.com/akrherz/iem/blob/main/scripts/asos/iem_scraper_example.py) is a python script example  that automates the download of data from this interface. A community user has contributed R language  version of the python script. There is also a riem R package  allowing for easy access to this archive.
