import pycuda.autoinit
import pycuda.driver as cuda
import numpy as np
from pycuda import gpuarray
from pycuda.compiler import SourceModule

# CUDAカーネルを定義
kernel_code = """
#include <curand_kernel.h>

extern "C" {
    __global__ void generate_random_numbers(float* output, unsigned int seed)
    {
        int tid = blockIdx.x * blockDim.x + threadIdx.x;
        curandState state;
        curand_init(seed, tid, 0, &state);
        output[tid] = curand_uniform(&state);
    }
}
"""

# CUDAカーネルをコンパイル
mod = SourceModule(kernel_code)
generate_random_numbers = mod.get_function("generate_random_numbers")

# パラメータの設定
grid_dim = (100, 1)  # グリッドの次元
block_dim = (100, 1, 1)  # ブロックの次元
total_threads = grid_dim[0] * block_dim[0]

# ホストメモリの作成
output = np.zeros(total_threads, dtype=np.float32)

# デバイスメモリの作成
output_gpu = gpuarray.to_gpu(output)

# 乱数の生成
seed = np.uint32(0)  # 乱数のシード値
generate_random_numbers(output_gpu, seed, block=block_dim, grid=grid_dim)

# 結果をホストにコピー
output_gpu.get(output)

# 結果の表示
output = output.reshape(grid_dim)
print(output)
