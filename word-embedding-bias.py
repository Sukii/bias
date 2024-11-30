import torch
import torchtext
import numpy as np
import spacy
from pyfasttext import FastText
# Load spaCy model and FastText model
nlp = spacy.load("en_core_web_lg")
model = FastText()
model.load_model("/content/sample_data/cc.de.300.bin")
glove = torchtext.vocab.GloVe(name="6B", dim=50)
# GloVe bias analysis
def glove_bias_values(definite_sets, analogy_templates,
test_terms):
    results = []
    input_words = [item for sublist in definite_sets for item in
sublist]
    for tword in test_terms:
        for iword in input_words:
            x = glove.vectors[glove.stoi[iword]]
            y = glove.vectors[glove.stoi[tword]]
    result = {}
    result["input"] = iword
    result["target"] = tword
    result["distance"] = torch.norm(y - x).item()
    result["cosine"] = cos_sim(x, y)
    results.append(result)
    return results

results_glove = glove_bias_values(definite_sets, analogy_templates,
test_terms)
output_glove = """# Glove output for Gender bias:
| input | manager |executive |doctor | lawyer | programmer | scientist| soldier |
supervisor | rancher| janitor| firefighter | officer|
"""
# Create a dictionary to store cosine similarity values for each target
word
target_columns = {target: [] for target in test_terms}
for result in results_glove:
    input_word = result['input']
for target in test_terms:
    if target == result['target']:
        target_columns[target].append(round(result['cosine'],
5))
# Populate the output_glove with the values from the dictionary
for input_word in definite_sets[0]:
    row = f"{input_word}"
for target in test_terms:
    row += f"{target_columns[target].pop(0)}|"
    output_glove += row + "\n"
# Display the table
display (Markdown(output_glove))
