import numpy as np
import glob

labels = []
samples_a = np.empty((0,32), float)
samples_b = np.empty((0,32), float)
samples_f = []

for filename in glob.glob('*.npz'):
    foo = np.load(filename)
    labels = np.append(labels, foo['labels'])
    samples_a = np.append(samples_a, foo['samples_a'], axis = 0)
    samples_b = np.append(samples_b, foo['samples_b'], axis = 0)
    samples_f = np.append(samples_f, foo['samples_f'])

print labels
print samples_a
print samples_b
print samples_f
