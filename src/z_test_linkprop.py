
# Clean way to associate/link several properties, i.e. auto update others when any of them changes?
#   https://stackoverflow.com/questions/53741313/clean-way-to-associate-link-several-properties-i-e-auto-update-others-when-any

def array_accessor(idx, getter):
    @property
    def prop(self):
        return getter(self)[idx]
    @prop.setter
    def prop(self, val):
        getter(self)[idx] = val
    return prop

class AAA:
    def __init__(self):
        self.xy = [0, 0]
    x = array_accessor(0, lambda self: self.xy)
    y = array_accessor(1, lambda self: self.xy)


a = AAA()
print(a.x, a.y, a.xy)
a.x = 1
a.y = 2
print(a.x, a.y, a.xy)
a.xy = [3, 4]
print(a.x, a.y, a.xy)
