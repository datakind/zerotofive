import pandas as pd
import folium
from folium.plugins import HeatMap

# Read the CSV file with childcare program data
data = pd.read_csv('geocodeddata.csv')

# Filter and select the relevant columns
filtered_data = data[['Latitude', 'Longitude']]

# Create a map centered around Orange County, Florida
m = folium.Map(location=[28.5383, -81.3787], zoom_start=12)

# Create a HeatMap layer with program locations
heat_data = filtered_data.values.tolist()

HeatMap(heat_data).add_to(m)

# Save the map to an HTML file
m.save('childcare_heatmap.html')
