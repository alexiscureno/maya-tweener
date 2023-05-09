![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Autodesk](https://a11ybadges.com/badge?logo=autodesk)
![Qt](https://img.shields.io/badge/Qt-%23217346.svg?style=for-the-badge&logo=Qt&logoColor=white)

# Tweener UI
## maya-tweener

This is a simple UI for tweening animation values in Maya using a PyQt5 interface. The UI consists of a slider and two buttons: "reset" and "close".

## Getting Started

### Prerequisites

To use this UI, you'll need to have the following software installed:
* Autodesk Maya (tested on version 2023)
* Python 3.7 or higher
* PyQt5

### Installing

To install the PyQt5 module, you can use pip:
`maya -script tweener.py`

This will open the UI window, where you can select the object and attributes you want to tween, and adjust the tween amount using the slider.
Pressing the "Reset" button will reset the slider value to 50, and the "Close" button will close the UI window.

## Usage

Once you have the script and UI file in your chosen directory, you can run the script by opening Maya and running the following command in the Python console:
```
import tweenerUI
import importlib

tweenerUI.TweenWindow().show()
```

* The UI window will appear. Select the object and attributes you want to tween, and adjust the tween amount using the slider.
* Press the "Set Key" button to apply the twee.
* To reset the slider value, press the "Reset" button.
* To close the UI window, press the "Close" button.

Alternatively, you can create a shelf button in Maya and add the above code to the command field of the button.

## Contributing

This project is open source and contributions are welcome. 
To contribute, please fork the repository, make your changes, and submit a pull request.

