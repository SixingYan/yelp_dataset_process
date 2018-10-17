BASE_DIR = '/Users/alfonso/Downloads/yelp_dataset/'

SQL_DIR = '/Users/alfonso/Downloads/yelp_dataset_sql/'

MAX_BUFFER = 1000


class DataSetPath(Enum):
    Busincess = BASE_DIR + 'yelp_academic_dataset_review.json'
    User = BASE_DIR + 'yelp_academic_dataset_user'
    Review = BASE_DIR + 'yelp_academic_dataset_review'
    Checkin = BASE_DIR + 'yelp_academic_dataset_checkin'
    Tips = BASE_DIR + 'yelp_academic_dataset_tips'


class BooleanSQL(Enum):
    TrueValue = 1
    FalseValue = 0
