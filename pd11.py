import pandas as pd

data = {
    'Name': ['nithin', 'nithya', 'nikhil', 'nishanth', 'nihal','Bleh','Bison','Jackson','Micah','Torch','Trip'],
    'Age': [20, 22, 22, 20, 23, 80, 90, 100, 34, 23, 56],
    'Subject': ['be', 'msc', 'bca', 'mtech', 'bsc','llm','llb','mca','ma','ba','bba'],
    'Marks': [85.5, 80.5, 95.5, 75.5, 65.5,45.5,78.9,100,69.3,59,34.5]
}

df = pd.DataFrame(data)

print(df.info())
# Display Dataset Information