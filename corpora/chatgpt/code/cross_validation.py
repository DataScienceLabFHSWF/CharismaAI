from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def calculate_similarity(df1, df2):
    # Concatenate the data from both dataframes for comparison
    concatenated_data = pd.concat([df1, df2])

    # Convert the concatenated data to a list of strings
    data_list = concatenated_data.astype(str).values.flatten().tolist()

    # Use CountVectorizer to convert text data to a matrix of token counts
    vectorizer = CountVectorizer().fit_transform(data_list)

    # Calculate cosine similarity
    similarity_matrix = cosine_similarity(vectorizer)

    # Return the similarity score
    return similarity_matrix[0, 1]  # Assuming you're comparing the first row with the second

# Usage example:
file1 = pd.ExcelFile('revised_4_1.xlsx')
file2 = pd.ExcelFile('revised_4_2.xlsx')

sheets_file1 = file1.sheet_names
sheets_file2 = file2.sheet_names

for sheet_name in sheets_file1:
    if sheet_name in sheets_file2:
        df1 = file1.parse(sheet_name)
        df2 = file2.parse(sheet_name)

        similarity_score = calculate_similarity(df1, df2)
        print(f"Similarity between {sheet_name} in file1 and file2 is: {similarity_score}")
