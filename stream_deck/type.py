from json import dumps
from typing import Optional

from .keys import ActionKey, ImageKey


class ButtonEvents:
  onPress: Optional[ActionKey]
  onRelease: Optional[ActionKey]

  def __init__(self, onPress: ActionKey, onRelease: ActionKey) -> None:
    self.onPress = onPress
    self.onRelease = onRelease

  def __str__(self) -> str:
    return dumps(self, default=vars, indent=2)


class ButtonText:
  default: Optional[str]
  pressed: Optional[str]

  def __init__(self, default: str, pressed: str) -> None:
    self.default = default
    self.pressed = pressed

  def __str__(self) -> str:
    return dumps(self, default=vars, indent=2)


class ButtonImages:
  default: Optional[ImageKey]
  pressed: Optional[ImageKey]

  def __init__(self, default: ImageKey, pressed: ImageKey) -> None:
    self.default = default
    self.pressed = pressed

  def __str__(self) -> str:
    return dumps(self, default=vars, indent=2)


class Type:
  events: ButtonEvents
  text: ButtonText
  images: ButtonImages

  def __init__(self, events: ButtonEvents, text: ButtonText, images: ButtonImages) -> None:
    self.events = ButtonEvents(**events)
    self.text = ButtonText(**text)
    self.images = ButtonImages(**images)

  def __str__(self) -> str:
    return dumps(self, default=vars, indent=2)
