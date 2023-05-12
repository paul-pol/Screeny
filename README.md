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

* Screeny.get_mouse_pos
* Screeny.locate_image
* Screeny.read_text
* Screeny.take_screenshot

* Image.__init__
* Image.binarize
* Image.denoise
* Image.get_data
* Image.invert
* Image.locate_image
* Image.read_text
* Image.resize
* Image.show
* Image.to_grayscale
* Image.to_hsv

### Screeny-class

#### Screeny.get_mouse_pos()
        
Returns the current position of the mouse as a tuple of xy-coordinates.

#### Screeny.locate_image(image: str | np.ndarray | Image [, rect: Rect, confidence: float])

Search for an image on the screen. Returns the location of the found image in pixel or False, if no image was found.

#### Screeny.read_text(rect: Rect)

Reads text from a given area on the screen. Returns the founded text as string.

#### Screeny.take_screenshot([rect: Rect])

Takes a screenshot of the complete monitor or a given area as "rect". Returns an Image-Instance.

### Image-Class

#### Image.__init__(image: str | np.ndarray | Image)

Creates a new instance of the Image-Class.

#### Image.binarize(method: str[, threshold: int])

Binarize the image.

#### Image.denoise()

Denoise the image.

#### Image.get_data()

Returns the pixels as numpy-array.

#### Image.invert()

Inverts the image.

#### Image.locate_image(image_to_find: str | np.ndarray | Image[, confidence: float])

Locates an second image in the image and returns the position of the founded image or False if no image was found.

#### Image.read_text([resize_factor: int, whitelist: str])

Reads the text from the image.

#### Image.resize(factor: int)

Resizes the image with a given factor.

#### Image.show([title: str])

Displays the image.

#### Image.to_grayscale()

Converts the image to grayscale.

#### Image.to_hsv()

Converts the image to HSV.