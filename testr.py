import numpy as np
npz_data = np.load('ihdp_npci_1-100.test.npz')
print(list(npz_data.keys()))
if __name__ == "__main__":
    x = np.load('../results/example_ihdp/evaluation.npz',allow_pickle=True)
    print(x)