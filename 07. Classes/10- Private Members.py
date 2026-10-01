
# Make attributes private using double underscore __
class TagCloudPrivate:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0)+1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloudPrivate()

cloud.add("Python")
cloud.add("Python")
cloud.add("Python")
print(cloud["PYTHON"])  # 3
print(cloud.__tags["PYTHON"])  # KeyError: 'PYTHON'

# When we don't want to expose tags user __tags, then we cannot access it directly like this:
# print(cloud.__tags["PYTHON"])  # KeyError: 'PYTHON'
# print(cloud.__tags)  # AttributeError: 'TagCloudPrivate' object has no attribute '__tags'

# To access the private attributes, we can use the following:
print(cloud.__dict__)  # {'_TagCloudPrivate__tags': {'python': 2}}
print(cloud._TagCloudPrivate__tags)  # This will work now
