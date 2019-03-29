import numpy as np
import os
import cv2
import classify_model 

theModel = None

def classifyImage(imagePath):
	global theModel
	if theModel == None:
		theModel = classify_model.getWeightedModel()

	# Gets the image from the path and formats it to be the same as the training data
	original = cv2.imread(imagePath)
	formattedImage = classify_model.formatImage(original)

	try:
		# Generates the predictions for the specified image
		prediction = theModel.predict(np.array( [formattedImage,] ) )
		# Finds the highest probability prediction and returns the corresponding label
		result = classify_model.class_names[np.argmax(prediction[0])]
	except:
		result = 'Failed Classification'

	return result

