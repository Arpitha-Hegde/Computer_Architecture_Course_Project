import operator

import matplotlib.pyplot as plt
import os, time, sys, numpy

def generating_outputs():
    output_files = ['a.out','diagonal.o','sparse.o']
    for i in range():
            f = open("output"+str(i)+'_'+str(k), "w+")
            sys.stdout = f
            os.system()
            f.close()
            time.sleep(1)


def dl1_analysis(file_name):

    # creating empty lists to be used

    dl1_block_size, dl1_associativity, dl1_cache_size, config_combined, dl1_replacement_policy,y = [], [], [], [], [], []
    dl1_repl_rate, dl1_miss_rate, dl1_wb_rate, data = [], [], [], []
    dict1 = {}

    # reading the string from the file and parsing it.

    output_file = open(file_name, "r")
    output_string = output_file.read()
    output_file.close()
    x = output_string.split("# -config                     # load configuration from a file")
    for i in x[1:]:
        y.append(i.split())

    #  creating the list of miss_rates, WB_rates and configurations
    k = 0
    for i in y:
        configuration = i[i.index('-cache:dl1') + 1].split(":")
        config = (configuration[1], configuration[2], configuration[3], configuration[4])
        data.extend([" - ".join(config)])
        dl1_cache_size.extend([float(configuration[1])])
        dl1_block_size.extend([float(configuration[2])])
        dl1_associativity.extend([float(configuration[3])])
        dl1_miss_rate.extend([float(i[i.index('dl1.miss_rate') + 1])])
        dl1_repl_rate.extend([float(i[i.index('dl1.repl_rate') + 1])])
        dl1_wb_rate.extend([float(i[i.index('dl1.wb_rate') + 1])])
        dict1[data[k]] = dl1_miss_rate[k]
        k += 1

    return data, dl1_miss_rate, dl1_wb_rate, dict1

def dl1_miss_rate_plots(data, miss_rate_1, miss_rate_2, miss_rate_3, cpi, type_of_graph = 'none'):
    if type_of_graph == 'none':
        plt.figure()
        plt.plot(data, miss_rate_1, 'ro--', label="Full Martix")
        plt.plot(data, miss_rate_2, 'go--', label="Diagonal Matrix")
        plt.plot(data, miss_rate_3, 'bo--', label="Sparse Matrix")
        plt.title("Miss rate for different matrix multiplication for different confiugrations", fontsize='x-large')
        plt.ylabel("Miss rate", fontsize='large')
        plt.xlabel("cache size - block size - associativity", fontsize='large')
        plt.legend()
        plt.show()
    elif type_of_graph == 'associativity':
        list1, list2, list3, list4 = [], [], [], []
        for i in range(0,6):
            x = 2**i
            y = int(256/x)
            string = str(y) + " - 128 - "+ str(x) + " - l"
            list1.extend([string])
            list2.extend([miss_rate_1[data.index(string)]])
            list3.extend([miss_rate_2[data.index(string)]])
            list4.extend([miss_rate_3[data.index(string)]])
        print(list1, list2,list3,list4)
        y_pos = numpy.arange(len(list1))
        fig = plt.figure()
        x1 = plt.bar(y_pos-0.2, list2, width = 0.2, align= 'center', color = 'r')
        x2 = plt.bar(y_pos, list3, width = 0.2, align='center', color = 'b')
        x3 = plt.bar(y_pos+0.2 , list4, width = 0.2, align = 'center', color = 'g')
        plt.xticks(y_pos, list1, fontsize = 'large')
        plt.title("Miss rate for different matrix multiplication for different confiugrations", fontsize = 'x-large')
        plt.ylabel("Miss rate", fontsize = 'large')
        plt.xlabel("cache size - block size - associativity", fontsize = 'large')
        plt.legend((x1,x2,x3),("Full matrix","Diagonal matrix","sparse matrix"), fontsize = 'x-large')
        plt.show()
    elif type_of_graph == 'block_size':
        list1, list2, list3, list4 = [], [], [], []
        for i in range(4, 8):
            x = 2 ** i
            y = int(8192 / x)
            string = str(y) + " - "+ str(x)+ " - 4 - l"
            list1.extend([string])
            list2.extend([miss_rate_1[data.index(string)]])
            list3.extend([miss_rate_2[data.index(string)]])
            list4.extend([miss_rate_3[data.index(string)]])
        print(list1, list2, list3, list4)
        y_pos = numpy.arange(len(list1))
        fig = plt.figure()
        x1 = plt.bar(y_pos - 0.2, list2, width=0.2, align='center', color='r')
        x2 = plt.bar(y_pos, list3, width=0.2, align='center', color='b')
        x3 = plt.bar(y_pos + 0.2, list4, width=0.2, align='center', color='g')
        plt.xticks(y_pos, list1, fontsize='x-large')
        plt.title("Miss rate for different matrix multiplication for different configurations", fontsize='x-large')
        plt.ylabel("Miss rate", fontsize='xx-large')
        plt.xlabel("N sets - block size - associativity", fontsize='xx-large')
        plt.legend((x1, x2, x3), ("Full matrix", "Diagonal matrix", "Sparse matrix"), fontsize='x-large')
        plt.show()
    elif type_of_graph == "cache_size":
        list1, list2, list3, list4 = [], [], [], []
        for i in range(1, 11):
            x = 2 ** i
            string = str(x) + " - 128 - 32 - l"
            list1.extend([string])
            list2.extend([miss_rate_1[data.index(string)]])
            list3.extend([miss_rate_2[data.index(string)]])
            list4.extend([miss_rate_3[data.index(string)]])
        print(list1, list2, list3, list4)
        y_pos = numpy.arange(len(list1))
        fig = plt.figure()
        x1 = plt.bar(y_pos - 0.2, list2, width=0.2, align='center', color='r')
        x2 = plt.bar(y_pos, list3, width=0.2, align='center', color='b')
        x3 = plt.bar(y_pos + 0.2, list4, width=0.2, align='center', color='g')
        plt.xticks(y_pos, list1, fontsize='x-large')
        plt.title("Miss rate for different matrix multiplication for different configurations", fontsize='x-large')
        plt.ylabel("Miss rate", fontsize='xx-large')
        plt.xlabel("cache size - block size - associativity", fontsize='xx-large')
        plt.legend((x1, x2, x3), ("Full matrix", "Diagonal matrix", "sparse matrix"), fontsize='x-large')
        plt.show()
    elif type_of_graph == "replacement_policy":
        list1, list2, list3, list4 = [], [], [], []
        y_pos = numpy.arange(len(data))
        fig = plt.figure()
        x1 = plt.bar(y_pos - 0.2, miss_rate_1, width=0.2, align='center', color='r')
        x2 = plt.bar(y_pos, miss_rate_2, width=0.2, align='center', color='b')
        x3 = plt.bar(y_pos + 0.2, miss_rate_3, width=0.2, align='center', color='g')
        plt.xticks(y_pos, data, fontsize='x-large')
        plt.title("Miss rate for different matrix multiplication for different configurations", fontsize='x-large')
        plt.ylabel("Miss rate", fontsize='xx-large')
        plt.xlabel("cache size - block size - associativity", fontsize='xx-large')
        plt.legend((x1, x2, x3), ("Full matrix", "Diagonal matrix", "sparse matrix"), fontsize='x-large')
        plt.show()
    return

def dl2_analysis(file_name):
    dl2_block_size, dl2_associativity, dl2_cache_size, config_combined = [], [], [], []
    dl2_repl_rate, dl2_miss_rate, dl2_wb_rate, data = [], [], [], []
    dict2 = {}
    output_file = open(file_name, "r")
    output_string = output_file.read()
    output_file.close()
    y = []
    x = output_string.split("# -config                     # load configuration from a file")
    for i in x[1:]:
        y.append(i.split())
    k = 0
    for i in y:
        config_combined.extend([i[i.index('-cache:dl2')+1]])
        configuration = i[i.index('-cache:dl2')+1].split(":")
        config = (configuration[1],configuration[2],configuration[3], configuration[4])
        data.extend([" - ".join(config)])
        dl2_cache_size.extend([configuration[1]])
        dl2_block_size.extend([configuration[2]])
        dl2_associativity.extend([configuration[3]])
        dl2_miss_rate.extend([float(i[i.index('dl2.miss_rate') + 1])])
        dl2_repl_rate.extend([float(i[i.index('dl2.repl_rate') + 1])])
        dl2_wb_rate.extend([float(i[i.index('dl2.wb_rate') + 1])])
        dict2[data[k]] = dl2_miss_rate[k]
        k += 1
    return data, dl2_miss_rate, dl2_wb_rate, dict2

def dl2_miss_rate_plots(data, miss_rate_1, miss_rate_2=0, miss_rate_3=0, cpi=0, type_of_graph = 'none'):
    if type_of_graph == 'none':
        plt.figure()
        plt.plot(data, miss_rate_1, 'ro--', label="Full Martix")
        plt.plot(data, miss_rate_2, 'go--', label="Diagonal Matrix")
        plt.plot(data, miss_rate_3, 'bo--', label="Sparse Matrix")
        plt.title("Miss rate for different matrix multiplication for different confiugrations", fontsize='x-large')
        plt.ylabel("Miss rate", fontsize='large')
        plt.xlabel("cache size - block size - associativity", fontsize='large')
        plt.legend()
        plt.show()
    elif type_of_graph == 'associativity':
        list1, list2, list3, list4 = [], [], [], []
        for i in range(0,5):
            x = 2**i
            y = int(16/x)
            string = str(y) + " - 128 - "+ str(x) + " - l"
            list1.extend([string])
            list2.extend([miss_rate_1[data.index(string)]])
            list3.extend([miss_rate_2[data.index(string)]])
            list4.extend([miss_rate_3[data.index(string)]])
        print(list1, list2,list3,list4)
        y_pos = numpy.arange(len(list1))
        fig = plt.figure()
        x1 = plt.bar(y_pos-0.2, list2, width = 0.2, align= 'center', color = 'r')
        x2 = plt.bar(y_pos, list3, width = 0.2, align='center', color = 'b')
        x3 = plt.bar(y_pos+0.2 , list4, width = 0.2, align = 'center', color = 'g')
        plt.xticks(y_pos, list1, fontsize = 'large')
        plt.title("Miss rate for different matrix multiplication for different confiugrations", fontsize = 'x-large')
        plt.ylabel("Miss rate", fontsize = 'large')
        plt.xlabel("cache size - block size - associativity", fontsize = 'large')
        plt.legend((x1,x2,x3),("Full matrix","Diagonal matrix","sparse matrix"), fontsize = 'x-large')
        plt.show()
    elif type_of_graph == 'block_size':
        list1, list2, list3, list4 = [], [], [], []
        for i in range(6, 16):
            x = 2 ** i
            y = int(65536 / x)
            string = str(y) + " - "+ str(x)+ " - 32 - l"
            list1.extend([string])
            list2.extend([miss_rate_1[data.index(string)]])
            list3.extend([miss_rate_2[data.index(string)]])
            list4.extend([miss_rate_3[data.index(string)]])
        print(list1, list2, list3, list4)
        y_pos = numpy.arange(len(list1))
        fig = plt.figure()
        x1 = plt.bar(y_pos - 0.2, list2, width=0.2, align='center', color='r')
        x2 = plt.bar(y_pos, list3, width=0.2, align='center', color='b')
        x3 = plt.bar(y_pos + 0.2, list4, width=0.2, align='center', color='g')
        plt.xticks(y_pos, list1, fontsize='x-large')
        plt.title("Miss rate for different matrix multiplication for different confiugrations", fontsize='x-large')
        plt.ylabel("Miss rate", fontsize='xx-large')
        plt.xlabel("cache size - block size - associativity", fontsize='xx-large')
        plt.legend((x1, x2, x3), ("Full matrix", "Diagonal matrix", "sparse matrix"), fontsize='x-large')
        plt.show()
    elif type_of_graph == "cache_size":
        list1, list2, list3, list4 = [], [], [], []
        for i in range(1, 11):
            x = 2 ** i
            string = str(x) + " - 128 - 32 - l"
            list1.extend([string])
            list2.extend([miss_rate_1[data.index(string)]])
            list3.extend([miss_rate_2[data.index(string)]])
            list4.extend([miss_rate_3[data.index(string)]])
        print(list1, list2, list3, list4)
        y_pos = numpy.arange(len(list1))
        fig = plt.figure()
        x1 = plt.bar(y_pos - 0.2, list2, width=0.2, align='center', color='r')
        x2 = plt.bar(y_pos, list3, width=0.2, align='center', color='b')
        x3 = plt.bar(y_pos + 0.2, list4, width=0.2, align='center', color='g')
        plt.xticks(y_pos, list1, fontsize='x-large')
        plt.title("Miss rate for different matrix multiplication for different confiugrations", fontsize='x-large')
        plt.ylabel("Miss rate", fontsize='xx-large')
        plt.xlabel("cache size - block size - associativity", fontsize='xx-large')
        plt.legend((x1, x2, x3), ("Full matrix", "Diagonal matrix", "sparse matrix"), fontsize='x-large')
        plt.show()
    elif type_of_graph == "replacement_policy":
        list1, list2, list3, list4 = [], [], [], []
        y_pos = numpy.arange(len(data))

        fig = plt.figure()
        x1 = plt.bar(y_pos - 0.2, miss_rate_1, width=0.2, align='center', color='r')
        x2 = plt.bar(y_pos, miss_rate_2, width=0.2, align='center', color='b')
        x3 = plt.bar(y_pos + 0.2, miss_rate_3, width=0.2, align='center', color='g')
        plt.xticks(y_pos, data, fontsize='x-large')
        plt.title("Miss rate for different matrix multiplication for different confiugrations", fontsize='x-large')
        plt.ylabel("Miss rate", fontsize='xx-large')
        plt.xlabel("cache size - block size - associativity", fontsize='xx-large')
        plt.legend((x1, x2, x3), ("Full matrix", "Diagonal matrix", "sparse matrix"), fontsize='x-large')
        plt.show()

    elif type_of_graph == 'outorder':
        y_pos = numpy.arange(len(data))
        fig = plt.figure()
        # x1 = plt.bar(y_pos - 0.2, miss_rate_1, width=0.2, align='center', color='b')
        # x2 = plt.bar(y_pos, cpi, width=0.2, align='center', color='r')
        # plt.xticks(y_pos, data, fontsize='xx-large')
        x1 = plt.plot(data, miss_rate_1, 'b', label = 'miss rate')
        x2 = plt.plot(data, cpi, 'r', label = 'cpi')
        plt.title("cpi and miss rate for diagonal matrix", fontsize='x-large')
        plt.ylabel("CPI and miss rate", fontsize='xx-large')
        plt.xlabel("config", fontsize='xx-large')
        # plt.legend((x1, x2), ("taken", "not-taken"), fontsize='x-large')
        plt.legend()
        plt.show()



        # fig = plt.figure()
        # x1 = plt.bar(y_pos, miss_rate_1, width=0.2, align='center', color='b')
        # # x2 = plt.bar(y_pos, cpi, width=0.2, align='center', color='r')
        # plt.xticks(y_pos, ["Out of order and cache optimized","Only cache optimized", "Default"], fontsize='x-large')
        # # x1 = plt.plot(data, miss_rate_1, 'b', label = 'miss rate')
        # # x2 = plt.plot(data, cpi, 'r', label = 'cpi')
        # plt.title("miss rate for in order and out of order execution", fontsize='x-large')
        # plt.ylabel("miss rate", fontsize='xx-large')
        # plt.xlabel("", fontsize='xx-large')
        # # plt.legend((x1, x2), ("taken", "not-taken"), fontsize='x-large')
        # # plt.legend()
        # plt.show()
    return



def out_order_analysis(file_name):

    # creating empty lists to be used

    dl1_block_size, dl1_associativity, dl1_cache_size, config_combined, dl1_replacement_policy,y = [], [], [], [], [], []
    dl1_repl_rate, dl1_miss_rate, dl1_wb_rate, data, cpi = [], [], [], [], []
    dict1 = {}

    # reading the string from the file and parsing it.

    output_file = open(file_name, "r")
    output_string = output_file.read()
    output_file.close()
    x = output_string.split("# -config                     # load configuration from a file")
    for i in x[1:]:
        y.append(i.split())

    #  creating the list of miss_rates, WB_rates and configurations
    k = 0
    for i in y:
        config_combined=[]
        # configuration_out_order = i[i.index('-res:imult') + 1]
        # configuration = [i[i.index('-issue:wrongpath') + 1]]
        # data.extend([" - ".join(configuration)])
        config_combined.extend(['L2N' if i[i.index('-cache:dl2')+1] != 'dl2:1:1024:128:l' else 'L2O'])
        config_combined.extend(['L1N' if i[i.index('-cache:dl1')+1] != 'dl1:64:128:4:l' else 'L1O'])
        config_combined.extend([i[i.index('-issue:inorder')+1]])
        data.extend(["-".join(config_combined)])
        dl1_miss_rate.extend([float(i[i.index('dl1.miss_rate') + 1])])
        dl1_repl_rate.extend([float(i[i.index('dl1.repl_rate') + 1])])
        dl1_wb_rate.extend([float(i[i.index('dl1.wb_rate') + 1])])
        cpi.extend([float(i[i.index('sim_CPI') + 1])])
        dict1[data[k]] = [dl1_miss_rate[k], cpi[k]]
        k += 1

    return data, dl1_miss_rate, cpi

if __name__ == "__main__":
    # dl2_analysis("output")
    # generating_outputs()
    # input = input("Input [Y] when ever the files are ready to be anyalyzed: ")
    # if input == 'Y':
    #     for k in range(1,3):
    dl1_1 = out_order_analysis("sparse")
    # dl1_2 = dl2_analysis("output3_2.txt")
    # dl1_3 = dl2_analysis("output3_3.txt")
    # sorted_dict = sorted(dl1_1[3].items(), key = operator.itemgetter(1))
    # print(sorted_dict)
    # x = dl1_1[0][dl1_1[1].index(min(dl1_1[1]))]
    print(dl1_1)
    dl2_miss_rate_plots(miss_rate_1=dl1_1[1], cpi=dl1_1[2], data=dl1_1[0] ,type_of_graph="outorder")


