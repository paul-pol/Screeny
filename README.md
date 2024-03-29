# Screeny
A simple python library for working with computer screens and images.

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

* [Screeny.get_mouse_pos](#screenyget_mouse_pos)
* [Screeny.locate_image](#screenylocate_imageimage-str--npndarray--image--rect-rect-confidence-float)
* [Screeny.read_text](#screenyread_textrect-rect)
* [Screeny.take_screenshot](#screenytake_screenshotrect-rect)
####
* [Image.__init__](#imageinitimage-str--npndarray--image)
* [Image.binarize](#imagebinarizemethod-str-threshold-int)
* [Image.compute_descriptors](#imagecompute_descriptors)
* [Image.denoise](#imagedenoise)
* [Image.detect_features](#imagedetect_features)
* [Image.detect_keypoints](#imagedetect_keypoints)
* [Image.get_data](#imageget_data)
* [Image.invert](#imageinvert)
* [Image.locate_image](#imagelocate_imageimage_to_find-str--npndarray--image-confidence-float)
* [Image.match_features](#imagematch_featuresimage_to_find-str--npndarray--image)
* [Image.read_text](#imageread_textresize_factor-int-whitelist-str)
* [Image.resize](#imageresizefactor-int)
* [Image.save](#imagesavetitle-str-path-str)
* [Image.show](#imageshowtitle-str)
* [Image.show_matches](#imageshow_matchesimage_to_find-str--npndarray--image-matches-list)
* [Image.to_grayscale](#imageto_grayscale)
* [Image.to_hsv](#imageto_hsv)

### Screeny-class

#### Screeny.get_mouse_pos()
        
Returns the current position of the mouse as a tuple of xy-coordinates.

---
#### Screeny.locate_image(image: str | np.ndarray | Image [, rect: Rect, confidence: float])

Search for an image on the screen. Returns the location of the found image in pixel or False, if no image was found.

---
#### Screeny.read_text(rect: Rect)

Reads text from a given area on the screen. Returns the founded text as string.

---
#### Screeny.take_screenshot([rect: Rect])

Takes a screenshot of the complete monitor or a given area as "rect". Returns an Image-Instance.


### Image-Class

#### Image.__init__(image: str | np.ndarray | Image)

Creates a new instance of the Image-Class.

---
#### Image.binarize(method: str[, threshold: int])

Binarize the image.

---
#### Image.compute_descriptors()

Computes the descriptors of the image.

---
#### Image.denoise()

Denoise the image.

---
#### Image.detect_features()

Finds features (keypoints and descriptors) in the image.

---
#### Image.detect_keypoints()

Finds the keypoints of the image.

---
#### Image.get_data()

Returns the pixels as numpy-array.

---
#### Image.invert()

Inverts the image.

---
#### Image.locate_image(image_to_find: str | np.ndarray | Image[, confidence: float])

Locates an second image in the image and returns the position of the founded image or False if no image was found.

---
#### Image.match_features(image_to_find: str | np.ndarray | Image, cross_check: bool)

Matches the features of the image with another image.

---
#### Image.read_text([resize_factor: int, whitelist: str])

Reads the text from the image.

---
#### Image.resize(factor: int)

Resizes the image with a given factor.

---
#### Image.save(title: str[, path: str])

Saves the image on the disk in a given path with a given title.
If no path is specified, the file will be saved in the current active directory.

---
#### Image.show([title: str])

Displays the image.

---
#### Image.show_matches(image_to_find: str | np.ndarray | Image, matches: list)

Show the two images with matches as lines connect points.

---
#### Image.to_grayscale()

Converts the image to grayscale.

---
#### Image.to_hsv()

Converts the image to HSV.
