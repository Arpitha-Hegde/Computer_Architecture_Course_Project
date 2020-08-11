Since we are optimizing our parameters and have a large number of combinations, we have written a pearl script for the same.
1) Copy the pearl script and the .out file to '$DIR/simplescalar/build/simplesim-3.0'

It takes two command line arguements-
a)argv[0]= name of simulator and it's arguements ($sim)
b)argv[1]= name of benchmark and it's arguements ( which is an xxx.out file) ($bench)
For eg. argv[0] can be 'sim-outorder' and argv[1] can be 'a.out'

We have defined the ilb1 and ilb2 to maintain homogenuity across simulators.

In our pearl script,for the dl1 and dl2 caches,we keep the cache size constant for one of them and we vary the following parameters <nsets>:<bsize>:<assoc> using i,j and k variable which iterate in a nested for loop. The variables vary in powers of 2. For example,for 32 sets, 512 block size and 4 way associative cache the inputs for i,j and k will be 5,9,2 respectively.
NOTE: Any flags in the simulator must be edited into the script itself and cannot be given in the command line.

2) After adjusting the required cache size(s)in the pearl file,for generating the data execute the following with appropriate arguements without the inverted commas.

'./script.pl $sim $bench > output.txt 2>&1'

NOTE: '> output.txt 2>&1' is to redirect the output to a txt file from which we were able to generate the graphs using a python script. The python script is modified each time according to the output generated in the output.txt file.

