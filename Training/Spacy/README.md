## Training Spacy
Requirements:
```
pip install spacy
python -m spacy download en_core_web_sm
```
train/train.py -> It is the script to train the Spacy from feature extraction, 
running it generates the other files and folders present in train folder.

Format :
TRAIN_DATA = [
("hi im sammy from fil how can i help you i am weasly i want to sell fifty percent in a fuming fund  okay it amounts to ten thousand pounds sounds good so may i confirm your details before you place the deal yes sure what is your full name weasly walnut what is the first line of your address and the pincode peter residency public pittensburg one one zero zero  what is the last ffour numbers of the card registered one two five nine of american express yes so i want to read the deal for you i confirm that i want to sell fifty percent of fuming fund which is worth ten thousand pounds from my account one two three four five fix seven yes perfect ",{
'entities':[(539,550,'fund'),(566,585,'amount'),(602,635,'account'),(517,521,'type')]
})]
run.py -> It is a script using which we can check the feature extraction process after training the spacy. 
