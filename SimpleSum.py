from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size() #same for all ranks

total_nums = 100 #same for all ranks

num = rank

while num < total_nums:
	num += num + size
#print(type(num))

total_sum = 0
total_sum=comm.reduce(num,op=MPI.SUM,root=0) 
if rank == 0:
	print(size)
	print(total_sum)
