import pickle
import tensorflow as tf
import numpy as np
import streamlit as st

model = pickle.load(open('model.pkl', 'rb'))

def prediction(file, img_height=224, img_width=224):
    ## Load an image
    image_inf = tf.keras.utils.load_img(file, target_size=(img_height, img_width))

    ## Rescaling and reshaping image
    x = tf.keras.utils.img_to_array(image_inf)/255
    x = np.expand_dims(x, axis=0)
    image_infs = np.vstack([x])

    ## Predict
    y_pred_inf_proba = model.predict(image_infs, batch_size=10)
    y_pred_inf_cls = np.argmax(y_pred_inf_proba)
    class_names = ['Dark', 'Green', 'Light', 'Medium']
    y_pred_class_name = class_names[np.argmax(y_pred_inf_proba[0])]

    return image_inf, y_pred_class_name

def run():
    st.title('Coffee beans roast level predictor')
    st.write('This page is created to create model to predict roast level of coffee beans ')

    inf_img = st.file_uploader('Upload your coffee beans image', type=["jpg", "jpeg", "png"])

    if inf_img:
        image_inf, predicted_class = prediction(inf_img)

        st.image(image_inf)
        if predicted_class == 'Green':
            st.write(f'The coffee beans is predicted as : {predicted_class} bean')
        else:
            st.write(f'The coffee beans is predicted as : {predicted_class} roasted')

if __name__ == '__main__':
    run()
