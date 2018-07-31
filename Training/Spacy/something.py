from __future__ import unicode_literals, print_function

import plac
import random
from pathlib import Path
import spacy


output_dir='/home/sangeetha/Desktop/spa/prem'
    with open('test_data.txt', 'r') as myfile:
    	data=myfile.read().replace('\n', '')
    # test the trained model
    #test_text = 'you are speaking to susan how can i assist you im steven from intex corporation okay let me confirm you details may i have you full name steven robert may i have last four digits of registered bank yes surely one zero nine eight okay now we are done with it we can proceed with the dealing i want to sell ten percent of my tata fund and invest thirty five thousand pounds in greenwich fund okay the ten percent worth of tata fund is thirty thousand pounds okay let reverify the deal you want to invest invest thirty five thousand pounds in greenwich fund with associated number one nine nine two and sell ten percent of my tata fund worth thirty thousand pounds okay fine i confirm itokay do you want any other assistance no thank you thank you'
    doc = nlp(data)
    print("entities in '%s'" % data)

        print("Loading from", output_dir)
        nlp2 = spacy.load(output_dir)
        doc2 = nlp2(data)
        for ent in doc2.ents:
            print(ent.label_, ent.text)
