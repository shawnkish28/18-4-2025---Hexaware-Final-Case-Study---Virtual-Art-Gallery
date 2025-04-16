class Artwork:
    def __init__(self, artwork_id, title, description, creation_date, medium, image_url):
        self._artwork_id = artwork_id
        self._title = title
        self._description = description
        self._creation_date = creation_date
        self._medium = medium
        self._image_url = image_url

    # Getters
    @property
    def artwork_id(self):
        return self._artwork_id

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @property
    def creation_date(self):
        return self._creation_date

    @property
    def medium(self):
        return self._medium

    @property
    def image_url(self):
        return self._image_url

    # Setters
    @artwork_id.setter
    def artwork_id(self, artwork_id):
        self._artwork_id = artwork_id

    @title.setter
    def title(self, title):
        self._title = title

    @description.setter
    def description(self, description):
        self._description = description

    @creation_date.setter
    def creation_date(self, creation_date):
        self._creation_date = creation_date

    @medium.setter
    def medium(self, medium):
        self._medium = medium

    @image_url.setter
    def image_url(self, image_url):
        self._image_url = image_url

    # Add this method to make print() and str() show artwork details nicely
    def __str__(self):
        return (
            f"\nArtwork ID   : {self.artwork_id}\n"
            f"Title        : {self.title}\n"
            f"Description  : {self.description}\n"
            f"Created On   : {self.creation_date}\n"
            f"Medium       : {self.medium}\n"
            f"Image URL    : {self.image_url}"
        )

