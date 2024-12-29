import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np

# Load the MRI image (replace 'your_image.nii' with your image file path)
img = nib.load('Dataset\sub-0003_T1w.nii.gz')

# Extract the image data as a numpy array
image = img.get_fdata()

# Display a histogram of pixel intensities
plt.hist(image.flatten(), bins=100, color='gray', alpha=0.7)
plt.title('Intensity Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.show()
