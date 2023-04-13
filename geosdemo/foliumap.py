import folium

class Map(folium.Map):
    """Create a folium map object.

    Args:
        folium (_type_): _description_
    """    
    def __init__(self, center=[20, 0], zoom=2, **kwargs) -> None:
        """Initializes the map object.

        Args:
            center (list, optional): The map center. Defaults to [20, 0].
            zoom (int, optional): The zoom level. Defaults to 2.
        """
        super().__init__(location=center, zoom_start=zoom, **kwargs)


    def add_tile_layer(self, url, name, attribution="", **kwargs):
        """Adds a tile layer to the map.

        Args:
            url (str): The URL of the tile layer.
            name (str): The name of the tile layer.
            attribution (str, optional): The attribution of the tile layer. Defaults to "".
        """
        tile_layer = folium.TileLayer(
            tiles=url,
            name=name,
            attr=attribution,
            **kwargs
        )
        self.add_child(tile_layer)