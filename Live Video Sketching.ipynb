{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Using TensorFlow backend.\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4.2.0\n"
     ]
    }
   ],
   "source": [
    "import keras\n",
    "import cv2\n",
    "import numpy as np\n",
    "import matplotlib\n",
    "print (cv2.__version__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import numpy as np\n",
    "\n",
    "# Our sketch generating function\n",
    "def sketch(image):\n",
    "    # Convert image to grayscale\n",
    "    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)\n",
    "    \n",
    "    # Clean up image using Guassian Blur\n",
    "    img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)\n",
    "    \n",
    "    # Extract edges\n",
    "    canny_edges = cv2.Canny(img_gray_blur, 30, 60)\n",
    "    \n",
    "    # Do an invert binarize the image \n",
    "    ret, mask = cv2.threshold(canny_edges, 240, 255, cv2.THRESH_BINARY_INV)\n",
    "    \n",
    "    return mask\n",
    "\n",
    "\n",
    "# Initialize webcam, cap is the object provided by VideoCapture\n",
    "# It contains a boolean indicating if it was sucessful (ret)\n",
    "# It also contains the images collected from the webcam (frame)\n",
    "cap = cv2.VideoCapture(0)\n",
    "cap2 = cv2.VideoCapture(1)\n",
    "# Get the Default resolutions\n",
    "frame_width = int(cap.get(3))\n",
    "frame_height = int(cap.get(4))\n",
    "\n",
    "while True:\n",
    "    ret, frame = cap.read()\n",
    "    ret1, frame1 = cap2.read()\n",
    "    cv2.imshow('Original', (frame))\n",
    "    cv2.imshow('Our Live Sketcher', sketch(frame))\n",
    "    if cv2.waitKey(1) == 13: #13 is the Enter Key\n",
    "        break\n",
    "        \n",
    "# Release camera and close windows\n",
    "cap.release()\n",
    "cap2.release()\n",
    "cv2.destroyAllWindows()      "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
