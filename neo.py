import streamlit as st
import requests
import pandas as pd
import plotly.express as px


api= "i7PiR3f4zrDEBs26CQ3TomFyghcWuikqaHLpr7Xf" 
url = "https://api.nasa.gov/neo/rest/v1/feed"

st.title(" Near-Earth Object Tracker")

start_date = st.date_input("Select Start Date")
end_date = st.date_input("Select End Date")

st.write("Please Note- Queries of up to 7 days at a time are only taken (eg- 25/08/19 to 25/08/25).")

if st.button("Get Asteroid Data"):
    params = {
        "start_date": str(start_date),
        "end_date": str(end_date),
        "api_key": api
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        asteroids = []

        for date in data["near_earth_objects"]:
            for asteroid in data["near_earth_objects"][date]:
                asteroids.append({
                    "Name": asteroid["name"],
                    "Diameter (km)": asteroid["estimated_diameter"]["kilometers"]["estimated_diameter_max"],
                    "Velocity (km/s)": asteroid["close_approach_data"][0]["relative_velocity"]["kilometers_per_second"],
                    "Miss Distance (km)": asteroid["close_approach_data"][0]["miss_distance"]["kilometers"],
                    "Hazardous": asteroid["is_potentially_hazardous_asteroid"]
                })

        df = pd.DataFrame(asteroids)
        st.dataframe(df)

        st.write("Please Note- An Aestroid is regarded hazardous only when it satisfies the 2 condition-")
        st.write("1. Its Minimum Orbit Intersection Distance (MOID) with Earth is ≤ 0.05 AU (about 7.5 million km or ~20 times the distance to the Moon).")
        st.write("2. Asteroid larger than ~140 meters in diameter.")


        fig = px.scatter(df, x="Miss Distance (km)", y="Diameter (km)", color="Hazardous",
                         size="Diameter (km)", hover_name="Name", title="Asteroids: Size vs Distance")
        st.plotly_chart(fig)

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("Download Data ", csv, "asteroids.csv", "text/csv")

    else:
        st.error("Failed to fetch data")

    st.write("Made with love by Anshuman Nigam ❤️")


