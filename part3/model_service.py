
from tensorflow import keras

def reshape_test_set(x_test_orig):
    """
	Reshapes test set in order to be used in cnn_images_model
	"""

    img_rows = 28
    img_cols = 28
    colour_channels = 1

    x_test = x_test_orig.reshape(x_test_orig.shape[0], img_rows, img_cols, colour_channels)
    return x_test


def make_predictions(x_test_orig):
    """
    Makes predictions on a given dataset using cnn_images_model
    """

    x_test = reshape_test_set(x_test_orig)

    # Load the model
    cnn_image_model = keras.models.load_model('models/cnn_images_model')

    # Make predictions
    preditions = cnn_image_model.predict_classes(x_test)

    return preditions