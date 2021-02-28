
CLASSNAME_IN_KEYWORD = False
MINOR_KEYWORD_EXISTS = True

### FOR NEW PROJECT CREATE NEW DIRECOTORY TO STORE IMAGES
PROJECT_NAME = 'gender_detection'

# Name classes to classify
CLASS1_NAME = 'male'
CLASS2_NAME = 'female'

MAJOR_KEYWORD_CLASS1 = 'keywords/{}/{}-major-keywords.txt'.format(PROJECT_NAME, CLASS1_NAME)
MINOR_KEYWORD_CLASS1 = 'keywords/{}/{}-minor-keywords.txt'.format(PROJECT_NAME, CLASS1_NAME)

MAJOR_KEYWORD_CLASS2 = 'keywords/{}/{}-major-keywords.txt'.format(PROJECT_NAME, CLASS2_NAME)
MINOR_KEYWORD_CLASS2 = 'keywords/{}/{}-minor-keywords.txt'.format(PROJECT_NAME, CLASS2_NAME)

KEYWORDS_CLASS1 = 'keywords/{}/keywords_class_{}.csv'.format(PROJECT_NAME, CLASS1_NAME)
KEYWORDS_CLASS2 = 'keywords/{}/keywords_class_{}.csv'.format(PROJECT_NAME, CLASS2_NAME)

DATASET_VERSION = 'data_gender'

# Maximum no. of images to download
MAX_NUMBER = 50
SEARCH_ENGINES = {"Google", "Bing"}
BROWSER_DRIVER = "chromedriver"