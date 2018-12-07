class AAA(object):
    def __setattr__(self, attr, value):
        print("set %s to %s" % (attr, value))
        super().__setattr__(attr, value)

aaa = AAA()
aaa.x = 17
print(aaa.x)
aaa.y = 'abc'
aaa.y = '123'