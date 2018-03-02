# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)
import os
#SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']

# Load config from the AWS Elastic Beanstalk Environemnt Variables for RDS
# NOTE: all the RDS env variables are automatically set by Beanstalk when
# an RDS database is added. 
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://%s:%s@%s/%s" % (
    os.environ['RDS_USERNAME'],
    os.environ['RDS_PASSWORD'],
    os.environ['RDS_HOSTNAME'],
    os.environ['RDS_DB_NAME'])

# Uncomment the line below if you want to work with a local DB
#SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True
