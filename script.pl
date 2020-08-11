#!/usr/bin/perl -w

# (1) quit unless we have the correct number of command-line args
$num_args = $#ARGV + 1;
#if ($num_args != 2) {
#    print "\nUsage: script.pl sim-file .oFile\n";
#    exit;
#}
$sim=$ARGV[0];
$bench=$ARGV[1];
=pod
#testing different block sizes for data cache 1
for(my $i=6; $i<11; $i++){
	my $cache_size = 2**$i;
	for(my $j=3; $j<11; $j++){
		my $block_size = 2**$j;
		for(my $k=1; $k<8; $k++){
			my $assoc = 2**$k;	
			system("./$sim -cache:dl1 dl1:$cache_size:$block_size:4:l -cache:dl2 dl2:$cache_size:$block_size:4:l -cache:il1 il2:256:16:4:l -cache:il2 il2:1024:32:8:l -bpred nottaken $bench");
		##usage -cache <no of sets> : <block_size> : <associativity of cache> : <replacement strategy 'l'-lru 'f'-FIFO, 'r'-random>
		
		}
	}
}

#testing different replacement policies for data cache 1
system("./$sim -cache:dl1 dl1:64:128:4:l -cache:dl2 dl2:1024:64:4:l -cache:il1 il2:256:16:4:l -cache:il2 il2:1024:32:8:l -issue:inorder true $bench");
system("./$sim -cache:dl1 dl1:128:32:4:l -cache:dl2 dl2:1024:64:4:l -cache:il1 il2:256:16:4:l -cache:il2 il2:1024:32:8:l -issue:inorder true $bench");
system("./$sim -cache:dl1 dl1:128:32:4:l -cache:dl2 dl2:1:1024:128:l -cache:il1 il2:256:16:4:l -cache:il2 il2:1024:32:8:l -issue:inorder true $bench");
system("./$sim -cache:dl1 dl1:64:128:4:l -cache:dl2 dl2:1:1024:128:l -cache:il1 il2:256:16:4:l -cache:il2 il2:1024:32:8:l -issue:inorder true $bench");
system("./$sim -cache:dl1 dl1:64:128:4:l -cache:dl2 dl2:1024:64:4:l -cache:il1 il2:256:16:4:l -cache:il2 il2:1024:32:8:l $bench");
system("./$sim -cache:dl1 dl1:128:32:4:l -cache:dl2 dl2:1024:64:4:l -cache:il1 il2:256:16:4:l -cache:il2 il2:1024:32:8:l $bench");
system("./$sim -cache:dl1 dl1:128:32:4:l -cache:dl2 dl2:1:1024:128:l -cache:il1 il2:256:16:4:l -cache:il2 il2:1024:32:8:l $bench");
system("./$sim -cache:dl1 dl1:64:128:4:l -cache:dl2 dl2:1:1024:128:l -cache:il1 il2:256:16:4:l -cache:il2 il2:1024:32:8:l $bench");

for(my $p=2; $p<6; $p++){
	my $ruu = 2**$p;
=cut
	system("./$sim -cache:dl1 dl1:64:128:4:l -cache:dl2 dl2:1:1024:128:l -bpred nottaken -issue:wrongpath false -ruu:size 64 -lsq:size 32 $bench 5");
	system("./$sim -cache:dl1 dl1:64:128:4:l -cache:dl2 dl2:1:1024:128:l -issue:inorder true $bench 5");
	system("./$sim $bench 5");


	##usage -cache <no of sets> : <block_size> : <associativity of cache> : <replacement strategy 'l'-lru 'f'-FIFO, 'r'-random>



