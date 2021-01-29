# PoW - 8: Image Processing

## Spatial Transformation

---

A digital image can be viewed as a two-dimensional function f (x, y), and the x-y plane indicates spatial position information, called the spatial domain. Spatial enhancement refers to processing pixels in a small range called its neighborhood. The filtering operation based on the x-y space neighborhood is called spatial domain filtering. An example of such an operation is Image smoothing, a technique that reduces and suppresses image noises. In the spatial domain, neighborhood averaging can generally be used to achieve the purpose of smoothing.

---

### Task 1. Mean Filtering

Mean filtering is a simple, intuitive and easy to implement method of smoothing images, i.e. reducing the amount of intensity variation between one pixel and the next. It is often used to reduce noise in images. The idea of mean filtering is simply to replace each pixel value in an image with the mean (average) value of its neighbors, including itself. This has the effect of eliminating pixel values which are unrepresentative of their surroundings. Mean filtering is usually thought of as a convolution filter. Like other convolutions it is based around a kernel, which represents the shape and size of the neighborhood to be sampled when calculating the mean. Often a 3×3 square kernel is used, as shown in the figure below.

![mean-filter.png](https://github.com/fse-ai/CV_PoW1_Image-processing/blob/master/resources/images/mean-filter-kernel.png)

Note that this filtering is also called 'Low pass filter' and 'image blurring'. This is because the effect is to average out rapid changes in pixel intensity. The blur, or smoothing, of an image removes “outlier” pixels that may be noise in the image. Blurring is an example of applying a low-pass filter to an image. In computer vision, the term “low-pass filter” applies to removing noise from an image while leaving the majority of the image intact. A blur is a very common operation we need to perform before other tasks such as edge detection.

The result of the average smoothing is shown below:

![mean-filter-example.png](https://github.com/fse-ai/CV_PoW1_Image-processing/blob/master/resources/images/mean-filter-example.png)

---

### Task 2. Gaussian Filtering

A gaussian filter is a linear filter used to blur an image and to reduce its noise like the mean filter. The mean filter tends to reduce noise while keeping the edges relatively sharp when compared to the gaussian filter. Gaussian filters are applied over an image using a filter made with gaussian function:

```math
{\displaystyle G(x,y)={\frac {1}{2\pi \sigma ^{2}}}e^{-{\frac {x^{2}+y^{2}}{2\sigma ^{2}}}}}
```

A gaussian filter of kernel size 9 looks like this.

![gaussian-filter.png](https://github.com/fse-ai/CV_PoW1_Image-processing/blob/master/resources/images/gaussian-filter-kernel.png)

Applying a Gaussian blur has the effect of reducing the image's high-frequency components, thus it is a low pass filter.

The result of the gaussian filter is shown below:

![gaussian-filter-example.png](https://github.com/fse-ai/CV_PoW1_Image-processing/blob/master/resources/images/gaussian-filter-example.png)

To create a gaussian filter:

1. Create a numpy vector using linspace method with start = `-(kernel_size // 2)` and end = `(kernel_size // 2 and)`. The number of samples must be equal to `kernel_size`.

2. Calculate the density using the formula of **Univariate Normal Distribution** on each element in the vector.

    ```math
    {\displaystyle f(x) = \frac {1}{\sigma{\sqrt {2 \pi}}} e ^ { { -\frac{1}{2} } ( \frac{x - \mu} {\sigma} ) ^ 2 } }
    ```

3. Compute the outer product of the vector with itself and store it in a new variable named `kernel_2D`.

4. Normalize the values of `kernel_2D` from `0` to `1`.

Your gaussian filter must be ready by now.

Convert the image to grayscale, apply padding and traverse through the image to apply the gaussian filter.

---

### Task 3. Image Thresholding

Thresholding is a type of image segmentation, where we change the pixels of an image to make the image easier to analyze. In thresholding, we convert an image from color or grayscale into a binary image, i.e., one that is simply black and white. Most frequently, we use thresholding as a way to select areas of interest of an image, while ignoring the parts we are not concerned with.

Consider the given image 'gems' and suppose we want to select only the coloured shapes from the grey background of the image. So we have to select the pixels belonging to the shapes 'on', while turning the rest of the pixels 'off', by setting their color channel values to zeros. This can be done providing a threshold manually. All pixels with values smaller than the threshold can be turned 'on' by using a comparison operator <, to compare the blurred image blur to the threshold which returns a binary image called the mask. It has only one channel, and each of its values is either 0 or 1. Here is a visualization of the binary image created by the thresholding operation. Finally, applying the mask to the original colored image would result in an image where the gems are extracted and rest of the image as black.

![threshold-example.png](https://github.com/fse-ai/CV_PoW1_Image-processing/blob/master/resources/images/threshold-example.png)

#### Prerequisites

---

1. Python, NumPy, Skimage, Matplolib
2. Digital Images Basics: FSEai CV Module 1
