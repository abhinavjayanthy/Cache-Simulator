import numpy as np

def cachecongi(cache_size,block_size,asso):
	print "Cache Size = ",cache_size
	print "Block Size = ",block_size
	print "Associativity = ",asso
	temp=(cache_size/block_size)
	numOfSets = temp/asso
	print "Number of sets = ",numOfSets
	offset = int(np.log2(block_size))
	print "Offset length = ",offset
	index = int(np.log2(numOfSets))
	print "Index Lenght = ",index
	tag = 32 - index - offset
	print "Tag Length = ",tag
	totalAdd = (numOfSets)*(asso)*(block_size/32)
	print "Total number of address = ",totalAdd

def lruAlgo(sets,asso,x):
	global lru
	pos = 0
	for i in range(asso):
		if(lru[sets][i] == x):
			pos = i
	i = pos
	for i in range(asso):
		lru[sets][i] = lru[sets][i+1]
		lru[sets][asso-1] = x

def output(access,hit):
	print "Number of access =",access
	print "Number of hits = ",hit
	print "Number of Missed = ",access-hit
	hitrate = (hit/float(access))*100
	print "Hit Rate = ",hitrate
	print "Miss Rate = ",100 - hitrate


cnfg = []
lru = []
for i in range(1000):
	lru.append([])
	for j in range(1000):
		lru[i].append(0)
cache = []
add = []
inputfile1 = raw_input("Please enter the Config file with extension:")
confFile = open(inputfile1,'r')
inputfile2 = raw_input("Please enter the Trace file with extension:")
traceFile = open(inputfile2,'rb')
temp = confFile.readlines()
for f in temp:
	cnfg.append(f.split("="))
cache_size = int(cnfg[0][1])
block_size = int(cnfg[1][1])
asso 	   = int(cnfg[2][1])
cachecongi(cache_size,block_size,asso)
no_blocks = cache_size / block_size
no_set = cache_size / (asso * block_size)


for i in range(no_set):
	cache.append([])
	for j in range(asso):
		cache[i].append(0)

for i in range(no_set):
	for j in range(asso):
		lru[i][j] = j

temp = traceFile.readlines()
for f in temp:
	access = 0
	hit = 0
	f = f.split(" ")
	add.append(int(f[0],0))
for i in range(len(add)):
	sets = (add[i]/block_size) % no_set
	tag = int(add[i]/(block_size * no_set))
	access += 1
	result = False
	if (cache[sets][j] == tag):
		result = True
		current_pos = j;
	if result:
		hit += 1
	else:
		j = lru[sets][0]
		cache[sets][j] = tag
		lruAlgo(sets,asso,j)

output(access,hit)