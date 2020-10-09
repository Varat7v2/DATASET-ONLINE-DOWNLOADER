
PROJECT_NAME = 'pet_detection'

# Name classes to classify
CLASS1_NAME = 'dog'
CLASS2_NAME = 'cat'

MAJOR_KEYWORD_CLASS1 = 'keywords/{}/{}-major-keywords.txt'.format(PROJECT_NAME, CLASS1_NAME)
MINOR_KEYWORD_CLASS1 = 'keywords/{}/{}-minor-keywords.txt'.format(PROJECT_NAME, CLASS1_NAME)

MAJOR_KEYWORD_CLASS2 = 'keywords/{}/{}-major-keywords.txt'.format(PROJECT_NAME, CLASS2_NAME)
MINOR_KEYWORD_CLASS2 = 'keywords/{}/{}-minor-keywords.txt'.format(PROJECT_NAME, CLASS2_NAME)

KEYWORDS_CLASS1 = 'keywords/{}/keywords_class_{}.csv'.format(PROJECT_NAME, CLASS1_NAME)
KEYWORDS_CLASS2 = 'keywords/{}/keywords_class_{}.csv'.format(PROJECT_NAME, CLASS2_NAME)

DATASET_VERSION = 'data_v1'

# Maximum no. of images to download
MAX_NUMBER = 5
SEARCH_ENGINES = {"Google", "Bing"}