import random
import hashlib
import json
from PIL import Image
from part import Part


class Avatar:
    def __init__(self):
        self.seed = None
        self.filename = None
        with open('assets.json') as data:
            self.assets = json.load(data)

    def __inputs(self, inputs):
        # if this is none then we can just come up with it ourselves
        if 'filename' in inputs:
            if isinstance(inputs['filename'], str):
                self.filename = inputs['filename']

        if 'seed' in inputs:
            self.seed = inputs['seed']
        else:
            print('reeeee')

    def __get_part(self, component):
        max_variation = len(self.assets[component])
        variation = random.randint(0, max_variation - 1)
        selection = self.assets[component][variation]
        part = Part(selection)
        return part

    def __compose(self, parts):
        # composit into the image in order
        image = None
        for part in parts:
            if image is None:
                image = part.image
            else:
                image = Image.alpha_composite(image, part.image)
        return image

    def __digest(self, seed):
        seed = seed.encode('utf-8')
        digest = hashlib.sha224(seed).hexdigest()
        return digest

    def create(self, inputs):
        self.__inputs(inputs)
        components = self.assets.keys()
        seed = self.__digest(self.seed)
        random.seed(seed)
        parts = []
        for component in components:
            p = self.__get_part(component)
            parts.append(p)
        avatar = self.__compose(parts)
        if self.filename is None:
            self.filename = 'avatar'
        avatar.save(self.filename + '.png', 'PNG')
        return avatar
