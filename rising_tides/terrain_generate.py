import os
from terrain import Terrain

# List of terrain files to process
terrain_files = [
    "rising_tides/CraterLake.terrain"
]

# Process each terrain file
for terrain_file in terrain_files:
    try:
        # Extract terrain name from path
        terrain_name = os.path.basename(terrain_file).replace(".terrain", "")
        print(f"Processing {terrain_name}...")

        # Initialize the Terrain object and load data
        terrain = Terrain()
        terrain.load_data_from_file(terrain_file)

        # Create directory if it doesn't exist
        os.makedirs("height_map", exist_ok=True)

        # Save height map with proper filename
        save_path = f"height_map/{terrain_name}_height_map.png"
        terrain.gen_frame(save_path=save_path)

        print(f"Generated height map for {terrain_name}")
    except Exception as e:
        print(f"Error processing {terrain_name}: {e}")
        print("Continuing with next terrain file...")