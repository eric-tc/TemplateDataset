from deepchecks.vision.simple_classification_data import load_dataset
from deepchecks.vision.suites import train_test_validation
import dvc.api
import os

# path to dataset
datasetPath= "/home/Develop/Dataset/DatasetVersioning/testDataset/Data/Dataset"

for i in range(1,3,1):

    tag="v"+str(i)
    nameDvc= "../Data/Dataset.dvc"

    os.system("pwd")        
    os.system("git checkout {} {}".format(tag,nameDvc))
    os.system("dvc pull")

    

    # #When load a dataset you will get A VisionData Class
    # # VisionData 
    train_ds = load_dataset(datasetPath, train=True, object_type='VisionData', image_extension='jpg')
    test_ds = load_dataset(datasetPath, train=False, object_type='VisionData', image_extension='jpg')

    suite= train_test_validation()

    result = suite.run(train_ds,test_ds)

    result.save_as_html("output{}.html".format(str(i)))