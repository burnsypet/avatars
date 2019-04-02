from PIL import Image


class Part:
    def __init__(self, selection):
        self.filepath = selection
        self.image = self.__find_image(self.filepath)

    def __find_image(self, filepath):
        image = Image.open(filepath)
        print(filepath)
        return image
