from mpi4py import MPI

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Define data for each process
    data = rank + 1  # Just an example data, you can replace it with your data

    # Perform the reduction operation to get the sum
    total_sum = comm.reduce(data, op=MPI.SUM, root=0)

    # Print result from rank 0
    if rank == 0:
        print("Total sum calculated from all ranks:", total_sum)

if __name__ == "__main__":
    main()

