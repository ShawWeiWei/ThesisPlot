from fileconf import *
from inputUtils import *
from plotUtils import *
from check import *
if __name__ == "__main__":
    file_conf = ExcitoryCouple(50, 0.27, 36, -25, "Square")
    input_util = input(file_conf)
    plot_util = visualize(input_util)
    plot_util.plotSpiralWaves()
    # plot_util.testPlot()
    keyvalue = {"gc_ex":[1,2,3]}
    def test(key,value,obj):
        func_name = "set_"+key
        func = getattr(obj,func_name)
        for a in value:
            func(a)


#    test("gc_ex",[1,2,3],file_conf)
#    listTupleToArray([1,2,3],[2,3,4])


