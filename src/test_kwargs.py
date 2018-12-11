# Understanding kwargs in Python
#   https://stackoverflow.com/questions/1769403/understanding-kwargs-in-python
class KK:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

a = KK(x=1, y=2, xy=[1,2])
print(a.__dict__)

for key in a.__dict__:
    print(getattr(a, key))
