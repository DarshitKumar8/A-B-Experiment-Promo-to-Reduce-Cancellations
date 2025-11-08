import papermill as pm

pm.execute_notebook(
    'AB_Test.ipynb',
    'AB_Test_Output.ipynb'
)
print("Notebook executed!")
