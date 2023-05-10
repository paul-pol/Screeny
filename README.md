# Screeny
A simple python library for working with screens and images.

## Installation

```sh
pip install screeny
```

## Usage

```python
from screeny import Screeny

sc = Screeny()
img = sc.take_screenshot()
```

## API-Reference

* [screeny.take_screenshot](#screenytake_screenshotrect-qrect--none)
* [screeny.get_mouse_pos](#screenyget_mouse_pos)
* screeny.locate_image_on_screen
* screeny.locate_image_in_image


### screeny.take_screenshot(rect: QRect = None)

Takes a screenshot of the complete monitor or a given area as "rect".
Returns the image as a numpy-array.

### screeny.get_mouse_pos()
        
Returns the current position of the mouse as a tuple of xy-coordinates.

### screeny.locate_image_on_screen(image: str | type[np.array], rect: QRect = None, confidence: float = 0.8)

Search for an image on the screen.
Returns the location of the found image in pixel or False, if no image was found.

### locate_image_in_image(img_to_find: str | type[np.array], in_img_to_search: str | type[np.array], confidence: float = 0.8)

Search for an image in another image and returns the location of the found image in pixels.
Returns False, if no image was found.
