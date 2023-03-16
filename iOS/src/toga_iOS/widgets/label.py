from rubicon.objc import CGSize
from travertino.size import at_least

from toga.colors import TRANSPARENT
from toga_iOS.colors import native_color
from toga_iOS.libs import NSLineBreakByWordWrapping, NSTextAlignment, UILabel
from toga_iOS.widgets.base import Widget


class Label(Widget):
    def create(self):
        self.native = UILabel.new()
        self.native.lineBreakMode = NSLineBreakByWordWrapping

        # Add the layout constraints
        self.add_constraints()

    def set_alignment(self, value):
        if value:
            self.native.textAlignment = NSTextAlignment(value)

    def set_color(self, value):
        self.native.textColor = native_color(value)

    def set_background_color(self, color):
        if color == TRANSPARENT or color is None:
            self.native.backgroundColor = native_color(TRANSPARENT)
        else:
            self.native.backgroundColor = native_color(color)

    def set_font(self, font):
        self.native.font = font._impl.native

    def set_text(self, value):
        self.native.text = self.interface.text

    def rehint(self):
        # Width & height of a label is known and fixed.
        # print("REHINT label", self, self.native.fittingSize().width, self.native.fittingSize().height)
        fitting_size = self.native.systemLayoutSizeFittingSize(CGSize(0, 0))
        self.interface.intrinsic.width = at_least(fitting_size.width)
        self.interface.intrinsic.height = fitting_size.height
