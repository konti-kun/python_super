import inspect 

class SuperSuperCls(object):
    def method(self):
        print("SuperSuperのmethodを実行しました.")

class SuperClsA(SuperSuperCls):
    def method(self):
        print ("SuperClsAのmethodを実行しました。")
        super(SuperClsA, self).method()

class SuperClsB(SuperSuperCls):
    def method(self):
        print("SuperClsBのmethodを実行しました。")
        super(SuperClsB, self).method()

class SubClsAB(SuperClsA,SuperClsB):
    def method(self):
        super(SubClsAB,self).method()

sub_inst=SubClsAB()
sub_inst.method()
x = inspect.getmembers(sub_inst, inspect.ismethod)
print(str(x[0][1]).split()[2])

