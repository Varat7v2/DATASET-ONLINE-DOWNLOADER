This project contributes mainly in downloading images from online search engine i.e. Google, Baidu, and Bing.

It plays major role while preparing datasets for machine learning models. I have mainly focused on preparing data for classification models i.e. based on keyword provided to search engine and small update on configuration file will allow users to automatically annotate all those downloaed images.

While, I am currently working on automtic annotated dataset preparation for object detection.

Following steps need to be followd to download images abiding within peripehery of this project.

###### **Step 1:** Prepare appropriated keywords in a separate text file according to classname. For instance, for classes dog and cat, two keywords files like dog.txt and cat.txt need to be prepared. For example you can refer to this [folder](https://github.com/Varat7v2/online-dataset-maker/tree/master/keywords/pet_detection). Only major and minor text files need to be manually prepared while the resulting csv file will be created by running the script as shown in Step 2

###### **Step 2:** Create sub-keywords from major keywords along with prefixes and postfixes if available
```
python classifier-keywords-generator.py
```

###### **Step 3:** Allocate generated keywords according to the classes
```
python csv2class-allocator.py
```

###### **Step 3:** Start downloading images online with number of images per keyword as an argument
```
python online-images-download.py --max_number 10
```
