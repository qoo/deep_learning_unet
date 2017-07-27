# import cv2
# import numpy as np
# import os
# import pickle
# from matplotlib import pyplot as plt
#
# srcFolder = 'C:/Users/CYEH1/OneDrive - Monsanto/deep_learning_unet/sample files/'
# filename = 'circle0_mask.tif'
# image = cv2.imread(srcFolder + filename)
# plt.imshow(image)
# plt.show()




# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.widgets as widgets
#
# def onselect(eclick, erelease):
#     if eclick.ydata>erelease.ydata:
#         eclick.ydata,erelease.ydata=erelease.ydata,eclick.ydata
#     if eclick.xdata>erelease.xdata:
#         eclick.xdata,erelease.xdata=erelease.xdata,eclick.xdata
#     ax.set_ylim(erelease.ydata,eclick.ydata)
#     ax.set_xlim(eclick.xdata,erelease.xdata)
#     fig.canvas.draw()

# import scipy.misc
#
# fig = plt.figure()
# ax = fig.add_subplot(111)
# #im = scipy.misc.imread(srcFolder + filename)
# im = cv2.imread(srcFolder + filename)
#
# arr = np.asarray(im)
# plt_image=plt.imshow(arr)
# rs=widgets.RectangleSelector(
#     ax, onselect, drawtype='box',
#     rectprops = dict(facecolor='red', edgecolor = 'black', alpha=0.5, fill=True))
# plt.show()
