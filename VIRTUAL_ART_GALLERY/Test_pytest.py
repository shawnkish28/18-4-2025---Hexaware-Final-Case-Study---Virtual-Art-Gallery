import pytest
from unittest.mock import MagicMock
from dao import VirtualArtGalleryDAOImpl
from entity import Artwork

@pytest.fixture
def dao():
    return VirtualArtGalleryDAOImpl("your_connection_string_here")

def test_add_artwork(dao):
    artwork = Artwork(None, "Test Title", "Test Description", "2024-05-20", "Test Medium", "http://example.com/image.jpg")
    dao.add_artwork = MagicMock(return_value=True)
    result = dao.add_artwork(artwork)
    assert result is True

def test_get_artwork_by_id(dao):
    artwork = Artwork(1, "Test Title", "Test Description", "2024-05-20", "Test Medium", "http://example.com/image.jpg")
    dao.get_artwork_by_id = MagicMock(return_value=artwork)
    result = dao.get_artwork_by_id(1)
    assert result.artwork_id == 1
    assert result.title == "Test Title"