# google-landmark-retrieval-challenge
This is the repo for the Google Landmark Retrieval Challenge.

Download the datasets from following links:

https://www.kaggle.com/c/8396/download/index.csv.zip

https://www.kaggle.com/c/8396/download/sample_submission.csv.zip

https://www.kaggle.com/c/8396/download/test.csv.zip

Extract it into folder called datasets, maintaining the following hierarchy:
Datasets/
	index,csv
	sample_submission.csv
	test.csv

Also create an Empty folder structure as follows:

Images/
	index
	test

To download the images run:

			python download_images.py 'Datasets/index.csv' 'Images/index/'

