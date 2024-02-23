+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.104.05             Driver Version: 535.104.05   CUDA Version: 12.2     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  Tesla T4                       Off | 00000000:00:04.0 Off |                    0 |
| N/A   51C    P8              10W /  70W |      0MiB / 15360MiB |      0%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
                                                                                         
+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|  No running processes found                                                           |
+---------------------------------------------------------------------------------------+

For the different packages the following values where collected:
The 2D fourie transfromation of arrays in the range of 128x128, 256x256, 512x512, 1024x1024 and 2048x2048 where evalueted. Results in order and marked with package to perform task.


Numpy 411 µs ± 102 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
Cupy  160 µs ± 15.4 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
Numpy 1.14 ms ± 41.7 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
Cupy  278 µs ± 60.8 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
Numpy 5.69 ms ± 49.2 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
Cupy  452 µs ± 1.59 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
Numpy 34.9 ms ± 7.75 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
Cupy  1.79 ms ± 92.4 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
Numpy 167 ms ± 19.2 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
Cupy  6.68 ms ± 102 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

