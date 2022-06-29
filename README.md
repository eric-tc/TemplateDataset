# remoteDatasetVersion
Test DataVersioning with remote repository

Test with DVC remote dataset to handle different version of data

# Folder

Data-> Put the Actual Data Acquired
Metadata-> .csv file with all parameters used for data acquisition
test-> Test used to verify data integrity


#How to Connect to a remote Local Dataset 

This code will setup a remote folder for dataset version. It is working as a git remote repository but for large dataset file

1) dvc init {ONLY IF THE FIRST TIME}

2) dvc remote add -d dvc-remote {PATH TO LOCAL REMOTE. Usually path is  /path/to/Local/NameDatasetRemote}

3) Add Dataset folder inside Data/Dataset. Inside Dataset folder you need to add your data. This will be tracked by version {ONLY FIRST TIME}

4) git add Data/Dataset.dvc ./gitignore

5) git commit -am "add dataset version 1"

6) git tag -a 'v1' -m 'raw data' {Used to retrive Dataset with version without Tag}

7) dvc push {Push dataset to remote localtion /path/to/Local/NameDatasetRemote }


# How to retrive a dataset

1) Download a git repository contain Dataset.dvc

2) Inside repository execute dvc pull {This will download latest dataset version}



# How to retrieve a specific dataset version

1) Download a git repository contain Dataset.dvc

2) git checkout v{SPECIFY DATASET VERSION} Example git checkout v1

3) Inside repository execute dvc pull {This will download the selected dataset version}

