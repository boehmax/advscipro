#mpi.py
from mpi4py import MPI
com = MPI.COMM_WORLD
rank = com.Get_rank()
print("Rank" ,rank)
