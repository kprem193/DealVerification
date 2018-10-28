from __future__ import unicode_literals, print_function

import plac
import random
from pathlib import Path
import spacy


output_dir='/home/sangeetha/Desktop/spa/prem'
    with open('test_data.txt', 'r') as myfile:
    	data=myfile.read().replace('\n', '')
    doc = nlp(data)
    print("entities in '%s'" % data)

        print("Loading from", output_dir)
        nlp2 = spacy.load(output_dir)
        doc2 = nlp2(data)
        for ent in doc2.ents:
            print(ent.label_, ent.text)
