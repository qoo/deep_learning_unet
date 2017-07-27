training image as xx.tif
traning label as xx_mask.tif

Ref:
http://tf-unet.readthedocs.io/en/latest/usage.html
from tf_unet import unet, util, image_util

#preparing data loading
data_provider = image_util.ImageDataProvider("fishes/train/*.tif")

http://tf-unet.readthedocs.io/en/latest/tf_unet.html?highlight=ImageDataProvider#module-tf_unet.layers
class tf_unet.image_util.ImageDataProvider(search_path, a_min=None, a_max=None, data_suffix=u'.tif', mask_suffix=u'_mask.tif')[source]
