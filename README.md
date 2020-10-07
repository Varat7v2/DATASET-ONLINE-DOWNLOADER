This project contributes mainly in downloading images from online search engine: Google, Baidu, and Bing.

It plays major role while preparing datasets for machine learning models. I have mainly focused on preparing data for classification models i.e. based on keyword provided to search engine and small update on configuration file will allow users to automatically annotate all those downloaed images.

While, I am currently working on automtic annotated dataset preparation for object detection.

Following steps need to be followd to download images abiding within peripehery of this project.

Step 1: Prepare appropriated keywords in a separate text file according to classname. For instance, for classes dog and cat, two keywords files like dog.txt and cat.txt need to be prepared.

Step 2: Convert keywords text file to csv file
Step 3: Start downloading images online with number of images to download per keyword as argument
```
python myonline-images-download.py
```
Step 4: Split entire datasets to three groups: training, validation, and testing dataset 
