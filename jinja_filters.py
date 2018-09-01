import os
import pathlib

IMAGES_PATH = pathlib.Path('content') / 'images'


def pictures(article):
    for filename in os.listdir(IMAGES_PATH / article.slug):
        yield f'images/{article.slug}/{filename}'
