Unreleased
==========

* New: Added parameter crossCheck to match_features-method.

0.4.1
=====
* New: Method to save image as a file.

0.4.0
=====
* New: ORB-Detector to Image-class
* New: functions to detect keypoints and compute descriptors
* New: functions to match features of two images

0.3.2
=====
* hotfix: Image.locate_image produced an error because of false colorcodes when calling matchTemplate-function from opencv

0.3.1
=====
* hotfix: Image.data() doesn't exist, but was called in image.py

0.3.0
=====
* new: Added module image with OCR-functionalities.
* edit: Cleaned up import-statements for package.
* new: Renamed QPoint-Class to Point.
* new: Install-requirement "pytesseract" for OCR.

0.2.1
=====
* hotfix: implemented check, if an instance of QGuiApplication already exists, because runtime errors could occur.

0.2.0
=====
* new: Functionality to search for an image on the screen or in another image.

0.1.0
=====
* new: CHANGELOG.md
* new: example-script for new function "get_mouse_pos()"
* new: Mouse-class for getting information about the mouse-positio on screen
* new: new sections in README.md (Installation, Usage, API-Reference)
* new: implemented function "get_mouse_pos" in screeny-class

0.0.3
=====
* added __init__.py for automatic detection of package by the setuptools in src-folder
* changed filestructur: removed src-folder for easier build

0.0.2
=====
* added license for 3rd-party-packages
* added an example-file for "How to take a screenshot"
* added some packages to project: numpy, mss, QRect
* Created screeny-module with first function to take screenshot from the screen.

0.0.1
=====
* Added README.md
* Initial commit