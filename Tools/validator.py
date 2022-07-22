import os
import importlib
import pandas
import warnings
warnings.filterwarnings('ignore')

individual_result_df = pandas.DataFrame(
    columns=["Employee_Full_Name", "Question", "Correct", "Incorrect"])
list_of_method_and_input_output = {'odd_or_even': {1: False, 2: True, 0: True},
                                   'is_number': {'1': True, '10007766a777': False}}


def get_py_files(src='submission'):
    cwd = os.getcwd()  # Current Working directory
    py_files = []
    for root, dirs, files in os.walk(src):
        for file in files:
            if file.endswith(".py"):
                py_files.append(os.path.join(cwd, root, file))
    return py_files


def dynamic_import(module_name, py_path):
    module_spec = importlib.util.spec_from_file_location(module_name, py_path)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    return module


list_of_py_files = get_py_files()

for index, py_file in enumerate(list_of_py_files):
    employee_full_name = (py_file.split('\\')[-1].split('_sub')[0])
    package = dynamic_import(py_file.split('\\')[-1], py_file)
    for method_name in list_of_method_and_input_output.items():
        correct = 0
        incorrect = 0
        for input_and_output in method_name[1].items():
            actual_method_pointer = getattr(package, method_name[0])
            res = actual_method_pointer(input_and_output[0])  # Key
            if res == input_and_output[1]:
                correct = correct + 1
            else:
                incorrect = incorrect + 1

        current_row = {'Employee_Full_Name': employee_full_name, 'Question': method_name[0],
                       "Correct": correct, 'Incorrect': incorrect}
        individual_result_df = individual_result_df.append(current_row, ignore_index=True)
overall_result_df = individual_result_df.groupby('Employee_Full_Name')['Correct', 'Incorrect'].sum()


writer = pandas.ExcelWriter('Result.xlsx', engine='xlsxwriter')
overall_result_df.to_excel(writer, sheet_name='overall_result')
individual_result_df.to_excel(writer, sheet_name='test_case_wise_result', index = False)
writer.save()