import numpy as np
from PIL import Image, ImageDraw
import os

class Terrain:
    def __init__(self):
        self.size = None
        self.grid = None
        self.water_sources = None
        self.water_map = None
        self.water_level = None
        self.max_elevation = None
        self.min_elevation = None

    def load_data_from_file(self, filename):
        with open(filename, 'r') as file:
            if file.readline().strip() != "terrain":
                raise ValueError("Invalid terrain file format")

            size = list(map(int, file.readline().strip().split()))
            num_water_sources = int(file.readline().strip())
            water_sources = [tuple(map(int, file.readline().strip().split())) for _ in range(num_water_sources)]
            grid = [list(map(float, file.readline().strip().split())) for _ in range(size[1])]

        self.size = tuple(size)
        self.grid = np.array(grid)
        self.water_sources = water_sources
        self.water_map = np.zeros_like(self.grid, dtype=bool)
        for source in water_sources:
            self.water_map[source] = True

        self.water_level = self.grid[water_sources[0]] if water_sources else self.grid[0, 0]
        self.max_elevation = np.max(self.grid)
        self.min_elevation = np.min(self.grid)

    def flood_terrain(self, water_level):
        flooded = self.water_map.copy()
        for source in self.water_sources:
            self._flood_recursive(source, water_level, flooded)
        return flooded

    def _flood_recursive(self, position, water_level, flooded):
        x, y = position
        if not (0 <= x < self.size[0] and 0 <= y < self.size[1]) or flooded[x, y] or self.grid[x, y] > water_level:
            return
        flooded[x, y] = True
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            self._flood_recursive((x + dx, y + dy), water_level, flooded)

    def generate_gif(self, output_path, max_water_level):
        images = []
        for water_level in range(max_water_level + 1):
            flooded = self.flood_terrain(water_level)
            image = self._create_image(flooded, water_level)
            images.append(image)
        images[0].save(output_path, save_all=True, append_images=images[1:], duration=500, loop=0)

    def _create_image(self, flooded, water_level):
        colormap = self._generate_colormap()
        image = Image.new('RGB', (self.size[1], self.size[0]))
        draw = ImageDraw.Draw(image)
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                color = (0, 0, 255) if flooded[i, j] else self._get_color_from_colormap(colormap, self.grid[i, j])
                draw.point((j, i), fill=color)
        draw.text((10, 10), f'Water Level: {water_level}', fill=(255, 255, 255))
        return image

    def _generate_colormap(self):
        colormap = [(int(2*i), 255, 0) if i < 128 else (255, 255 - int(2*(i-128)), 0) for i in range(256)]
        return colormap

    def _get_color_from_colormap(self, colormap, elevation):
        normalized_elevation = int(255 * (elevation - self.min_elevation) / (self.max_elevation - self.min_elevation))
        return colormap[normalized_elevation]

    def gen_frame(self, save_path=None):
        terrain_min = self.min_elevation
        terrain_max = self.max_elevation
        level = self.water_level

        flooded = self.flood_terrain(level)
        image = self._create_image(flooded, level)

        if save_path:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            image.save(save_path, format="PNG")
            print(f"Frame saved to {save_path}")

        return image