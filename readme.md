# Coffee beans roast level

## Repository Outline
1. coffee_beans_classification.ipynb - The main notebook where all the process writen
2. coffee_Inf.ipynb - notebook for inference testing
3. inf_img.jpg - image used for inference testing


## Objective
- Creating a machine learning model that able to distinct types of roasted coffee beans that have 4 class : green, light, medium, and dark;
- Helping newbie in coffee industry or hobbyist to distinguish types of roasted coffee beans with the created model.

## Project Output
Machine learning model that able to predict coffee beans level into 4 class: green, light, medium, and dark

## Data
Data url : https://www.kaggle.com/datasets/gpiosenka/coffee-bean-dataset-resized-224-x-224/data  
The data is uniformly taken picture of single coffee beans. The beans is centered in the middle of the image, uniform white background with some sadhow over it.

## Method
- We will try to make CNN model from scratch;
- Trying to fine-tune existing model, here we used MobileNetV3 to see if smaller model that already pre-trained can tackle the problem or not.

## Stacks
Tools used : 
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- TensorFlow
- Keras

## Reference
Huggingface deployment : https://huggingface.co/spaces/waskithag/coffee-beans