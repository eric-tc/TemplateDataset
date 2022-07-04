from deepchecks.vision.simple_classification_data import load_dataset
from deepchecks.vision.suites import train_test_validation
import dvc.api
import os
from customSuite import *
import pytest

from pathlib import Path
# path to dataset
datasetPath= "/home/Develop/Dataset/DatasetVersioning/testDataset/Data/Dataset"

# HOW IT WORKS

"""

For each new Test Suite or Dataset version you need to createa new test. 
The name have to be test_suite{suite_number}_validate_dataset_v{dataset_version}

Each test will print an output_file with the result of every suite
If some data tests validation fail pytest result a failed test 

pytest test_dataIntegrity.py


"""

def change_dataset_version(version_number):
    tag="v"+str(version_number)
    nameDvc= "../Data/Dataset.dvc"

    os.system("pwd")        
    os.system("git checkout {} {}".format(tag,nameDvc))
    os.system("dvc pull")

def create_result_folder():
    Path("results").mkdir(
        parents=True, exist_ok=True)

    

def test_suite1_validate_dataset_v1(capsys):
    
    create_result_folder()
    version_number= 1
    
    suite,suite_number= Suite_1()

    with capsys.disabled():
        
        change_dataset_version(version_number)
        
        # #When load a dataset you will get A VisionData Class
        # # VisionData 
        train_ds = load_dataset(datasetPath, train=True, object_type='VisionData', image_extension='jpg')
        test_ds = load_dataset(datasetPath, train=False, object_type='VisionData', image_extension='jpg')

        suite= train_test_validation()

        result = suite.run(train_ds,test_ds)

        result.save_as_html("results/output_suite{}_datasetV{}.html".format(str(suite_number),str(version_number)))

        assert result.passed()


def test_suite1_validate_dataset_v2(capsys):
    
    version_number= 2
    suite,suite_number= Suite_1()

    with capsys.disabled():
        
        change_dataset_version(version_number)
        
        # #When load a dataset you will get A VisionData Class
        # # VisionData 
        train_ds = load_dataset(datasetPath, train=True, object_type='VisionData', image_extension='jpg')
        test_ds = load_dataset(datasetPath, train=False, object_type='VisionData', image_extension='jpg')

        suite= train_test_validation()

        result = suite.run(train_ds,test_ds)

        result.save_as_html("results/output_suite{}_datasetV{}.html".format(str(suite_number),str(version_number)))

        assert result.passed()

