class Text(str):
    def duplicate(self):
        return self + self


text = Text("Hello")
print(text.duplicate())  # HelloHellox


class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)


trackable_list = TrackableList()
trackable_list.append("Hello")
print(trackable_list)  # ['Hello']
trackable_list.append("World")
print(trackable_list)  # ['Hello', 'World']
