import tensorflow as tf
import cv2
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage.measurements import label
from PIL import Image
from scipy.special import expit

def pipeline(image, sess, X, mode, pred):
    image_WH=(512, 512)
    image = np.copy(image)
    H, W, C = image.shape
    
    if (W, H) != image_WH:
        image = cv2.resize(image, image_WH)
    
    mask_pred = sess.run(pred, feed_dict={X: np.expand_dims(image, 0),
                                          mode: False})
    
    mask_pred = np.squeeze(mask_pred)
    mask_pred = expit(mask_pred)
    return mask_pred

def predict_se(image):
	saver = tf.train.import_meta_graph("dr_unet/models_se/model.ckpt.meta")
	sess = tf.InteractiveSession()
	saver.restore(sess, "dr_unet/models_se/model.ckpt")
	X, mode = tf.get_collection("inputs")
	pred = tf.get_collection("outputs")[0]

	image = np.array(image)

	predicted_image = np.zeros((2848, 4288), dtype=float)
	for i in range(10):
		for j in range(16):
			top_y = i*256
			if (i==9):
				top_y = 2336
			top_x = j*256
			if (j==15):
				top_x = 3776

			image_crop = image[top_y:top_y+512, top_x:top_x+512]
			predicted_crop = pipeline(image_crop, sess, X, mode, pred)
			predicted_image[top_y:top_y+512, top_x:top_x+512] = np.maximum(predicted_image[top_y:top_y+512, top_x:top_x+512], predicted_crop)
	threshold = 0.9
	predicted_image = predicted_image > threshold
	predicted_mask = (predicted_image.astype('uint8'))*255
	predicted_mask = np.stack((predicted_mask,)*3, -1)
	output_image = np.maximum(predicted_mask, image)
	output_save = Image.fromarray(output_image)
	
	return output_save

# image_path = "IDRiD_14.jpg"
# image = Image.open(image_path)
# output_save = predict_se(image)
# output_save.save("predicted_se.jpg", "JPEG")