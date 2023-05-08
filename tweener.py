from PyQt5.QtWidgets import QDialog, QPushButton, QSlider, QLabel
from PyQt5 import uic
from maya import cmds


class TweenerUI(QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi(r'C:\Users\user\Documents\maya\2023\scripts\tweener.ui', self)

        self.reset_btn = self.findChild(QPushButton, 'reset_button')
        self.reset_btn.clicked.connect(self.reset)

        self.close_btn = self.findChild(QPushButton, 'close_button')
        self.close_btn.clicked.connect(self.close)

        self.slider = self.findChild(QSlider, 'slider')
        self.slider.valueChanged.connect(self.tween)

    def tween(self, percentage, obj=None, attrs=None, selection=True):
        """
           Args:
               percentage:
               obj:
               attrs:
               selection:

           Returns:

           """

        # If obj is not given and selection is set to False, error early
        if not obj and not selection:
            raise ValueError("No object given to tween")

        # if obj is specified, get it from selection
        if not obj:
            obj = cmds.ls(selection=True)[0]

        if not attrs:
            attrs = cmds.listAttr(obj, keyable=True)

        current_time = cmds.currentTime(query=True)

        for attr in attrs:

            # Construct the full name of the attribute with its object
            attrFull = '%s.%s' % (obj, attr)

            # Get the keyframes of the attribute on this object
            keyframes = cmds.keyframe(attrFull, query=True)

            # if not keyframes then continue
            if not keyframes:
                continue

            previous_keyframes = []

            for frames in keyframes:
                if frames < current_time:
                    previous_keyframes.append(frames)

            later_keyframes = [frame for frame in keyframes if frame > current_time]

            if not previous_keyframes and not later_keyframes:
                continue

            if previous_keyframes:
                previous_frames = max(previous_keyframes)
            else:
                previous_frames = None

            next_frame = min(later_keyframes) if later_keyframes else None

            if not previous_frames or not next_frame:
                continue

            previous_value = cmds.getAttr(attrFull, time=previous_frames)
            next_value = cmds.getAttr(attrFull, time=next_frame)

            difference = next_value - previous_value
            weight_difference = (difference * percentage) / 100.0
            current_value = previous_value + weight_difference

            cmds.setKeyframe(attrFull, time=current_time, value=current_value)

    def reset(self):
        self.slider.setValue(50)


window = TweenerUI()
window.show()
