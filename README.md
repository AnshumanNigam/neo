# Near-Earth Object (NEO) Tracker

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A **Streamlit web app** that tracks near-Earth asteroids using NASA's [NeoWs API](https://api.nasa.gov/).  
It lets you select a date range (up to 7 days) and fetch details such as asteroid size, velocity, miss distance, and whether it’s potentially hazardous.  
The app also provides an interactive Plotly scatter plot and allows exporting results to CSV.

---

## Features

- Select **start and end dates** for asteroid tracking  
- Query **NASA NEO API** (up to 7 days at once)  
- View asteroid details in a **Streamlit DataFrame**  
- Plot **Miss Distance vs Diameter** with Plotly  
- **Download asteroid data** as CSV  
- **potentially hazardous asteroids** based on NASA’s criteria  

---

## Tech Stack

- [Python](https://www.python.org/)  
- [Streamlit](https://streamlit.io/)  
- [Pandas](https://pandas.pydata.org/)  
- [Plotly Express](https://plotly.com/python/plotly-express/)  
- [NASA NeoWs API](https://api.nasa.gov/)  

---

## Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/<your-username>/neo-tracker.git
cd neo-tracker
pip install -r requirements.txt
