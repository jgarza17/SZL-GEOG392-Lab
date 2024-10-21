import os
import geopandas as gpd

# Load the GeoJson file into a GeoDataFrame
gdf = gpd.read_file(r'C:\Users\julia\OneDrive\Desktop\gis_programming_folder\data.geojson')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

class CensusTract:
    def __init__(self, geoid, population, geometry):
        self.geoid = geoid
        self.population = population
        self.geometry = geometry
    
    def calculate_population_density(self):
        # calculate the population density based on geometry
        area = self.geometry.area 
        if area > 0:
            population_density = self.population / area
        else:
            population_density = 0 
        
        return population_density

if __name__ == "__main__":
    # read data
    file_path = os.path.join(DATA_DIR, 'data.geojson')
    # load data into GeoDataFrame
    gdf = gpd.read_file(r'C:\Users\julia\OneDrive\Desktop\gis_programming_folder\data.geojson')
    # preview data
    print(gdf.head())
    print(gdf.columns)
    print(gdf.shape)
    print(gdf.dtypes)

    # calculate the Population Density based on geometry
gdf['Pop_Den_new'] = gdf.apply(
    lambda row: CensusTract(row['GeoId'], row['Pop'], row['geometry']).calculate_population_density(),
    axis=1
)
# Check the result
print(gdf[['GeoId', 'Pop', 'Pop_Den_new']].head())


    