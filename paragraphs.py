import re
import textract
import numpy as np

from pandas import DataFrame


text = '200309-sustainable-finance-teg-final-report-taxonomy-annexes_en.pdf'

# Extract raw text from PDF file
raw_text = textract.process(text.decode(), method='pdfminer')

# Split by paragraph and remove blank spaces
text_split = re.split('\n\n', raw_text.decode())
stripped = [x.strip() for x in text_split]

# Store paragraphs in a Pandas DataFrame
df = DataFrame(stripped, columns=['paragraph'])

# Convert the emptly strings to NaN so that we can drop them
df['paragraph'].replace('', np.nan, inplace=True)
df.dropna(subset=['paragraph'], inplace=True)

# Save to csv
df.to_csv('paragrapsh.csv')
