class Layer:

    def __init__(self, from_display, shape=None, color=0):
        """
        :param from_display: the display from the main code
        :param shape: TopoDS_Shape
        :param color: Quantity color
        """
        self.clear()
        self.color = color
        self.display = from_display
        if shape is not None:
            self.add(shape)

    def add(self, shape):
        self.to_display = {self.count}
        self.to_display = self.display.DisplayShape(shape, color=self.color)[0]
        self.list_to_display.append(self.to_display)
        self.shapes.append(shape)
        self.count += 1
        self.display.Context.Erase(self.to_display, False)

    def clear(self):
        self.list_to_display = []
        self.count = 0
        self.to_display = {self.count}
        self.shapes = []

    def get_shapes(self):
        """
        :return: TopoDS_Shape
        """
        return self.shapes

    def hide(self):
        for shape in self.list_to_display:
            self.display.Context.Erase(shape, False)

    def merge(self, layer, clear=False):
        """
        :param layer: name of the layer to join
        :param clear: bool to clear the layer to join
        :return: None
        """
        for shape in layer.get_shapes():
            self.add(shape)
        if clear is True:
            layer.clear()

    def show(self):
        for shape in self.list_to_display:
            self.display.Context.Display(shape, True)
