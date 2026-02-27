# In order for the tests to work, you should first run `maturin develop` in the cmu_graphics_rust directory and then run this file using uv
import cmu_graphics_rust

# a square with no holes
multipoly = [[[(0.0, 0.0), (0.0, 1.0), (1.0, 1.0), (1.0, 0.0), (0.0, 0.0)]]]

print(cmu_graphics_rust.union(multipoly, multipoly))
print(cmu_graphics_rust.union_alt([multipoly]))
