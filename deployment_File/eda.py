import streamlit as st
import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt

def plot_images(label):
    folder_path = 'train/' + label  # Updated folder path
    fig = plt.figure(figsize=(15, 12))
    columns = 5
    rows = 4
    st.write('Class : ', label)
    
    try:
        images = [img for img in os.listdir(folder_path) if img.endswith(('.jpg', '.jpeg', '.png'))]
        for index in range(20):  # Show 20 images
            if index < len(images):
                img_path = os.path.join(folder_path, images[index])
                ax = fig.add_subplot(rows, columns, index + 1)
                image = plt.imread(img_path)
                plt.imshow(image)
                plt.axis('off')
        
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error loading images: {str(e)}")

def run():
    # Make title
    st.title('Coffee beans roast level predictor')
    st.write('This page is created to create model to predict roast level of coffee beans ')
    
    plot_images('Green')
    plot_images('Light')
    plot_images('Medium')
    plot_images('Dark')

    st.write('''
                - The main difference of each class of coffee beans is it's color and the color of it's crack, while the shape of each class is similar;
                - We guess that any color space used will give similar performance because of our image characteristic that able to be differentiate with it's color alone, all the images got one object in the middle (coffee beans) with white bacground and some shadow;
                - In the wild, usually image of coffee beans is a full image filled with coffee beans, not a singular coffee beans with white background. So maybe our model will be a bit confused if it meet this kind of image in the future.    
             ''')

if __name__ == '__main__':
    run()