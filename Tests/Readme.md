# Python Test

Python script to verify data integrity.
Each dataset could have different check

# How it Works



For each new Test Suite or Dataset version you need to createa new test. 
The name have to be test_suite{suite_number}_validate_dataset_v{dataset_version}

Each test will print an output_file with the result of every suite
If some data tests validation fail pytest result a failed test 

pytest test_dataIntegrity.py


# How to Create a New suite  

Have a look inside customSuite.py
