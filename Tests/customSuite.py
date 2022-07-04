from deepchecks.vision.simple_classification_data import load_dataset
from deepchecks.vision.suites import train_test_validation
from deepchecks.vision import Suite

from deepchecks.vision.checks import (ClassPerformance, ConfusionMatrixReport, FeatureLabelCorrelationChange,
                                      HeatmapComparison, ImageDatasetDrift, ImagePropertyDrift, ImagePropertyOutliers,
                                      ImageSegmentPerformance, LabelPropertyOutliers, MeanAveragePrecisionReport,
                                      MeanAverageRecallReport, ModelErrorAnalysis, NewLabels, SimilarImageLeakage,
                                      SimpleModelComparison, TrainTestLabelDrift, TrainTestPredictionDrift)

"""

THIS FILE IS USED TO CREATE CUSTOM SUITE FOR DATASET.
EACH FUNCTION SUITE HAS TO BE NAMED Suite_{v_number}

"""

def func_test(test_1,**extras):
    print(test_1)

def Suite_1()-> Suite:
    
    return Suite(
        'Suite 1',
        NewLabels().add_condition_new_label_ratio_less_or_equal(),
        SimilarImageLeakage().add_condition_similar_images_less_or_equal(),
        HeatmapComparison(),
        TrainTestLabelDrift().add_condition_drift_score_less_than(),
        ImagePropertyDrift().add_condition_drift_score_less_than(),
        ImageDatasetDrift(),
        FeatureLabelCorrelationChange().add_condition_feature_pps_difference_less_than(),
    ),1

if __name__ == "__main__":

    suite= Suite_1()

