# Large Deal Verification
This is a prototype of solution of problem "Large Deal Verifiaction".

To run the prototype install apache sever 2.x and php 7
Put the files in the required file as per your apache installation


## Speech to Text
index.php -> It is 1st part of prototype which contains Speech to Text Part which uses DeepSpeech.To run upload any wav file in required format (16KHz and mono), if your file is not in required format convert it using ffmpeg
```
ffmpeg -i 111.mp3 -acodec pcm_s16le -ac 1 -ar 16000 out.wav
```
Using Intel® Xeon(R) CPU E3-1230 v5 it takes around the same time as the length of audio. After that time refresh the page.

The Google's output is not dynamic, it is the output of demo call given. To make Google's output dynamic a script is provided "google_speech.py" .

Note : models are not in the repository as the files are large. To download and extract the files run this command in the working directory (the same directory in which index.php is present) ```
wget -O - https://github.com/mozilla/DeepSpeech/releases/download/v0.1.1/deepspeech-0.1.1-models.tar.gz | tar xvfz - ```

### Prerequisites 
``` DeepSpeech : pip3 install DeepSpeech```

## Feature Extraction
index1.php -> It is the second part of prototype which caontains the part of Feature Extraction. It is running Spacy in background for extracting Features It has undergone custom training on our data and it outputs following faetures (type : (type of deal sell/buy/switch), amount: ,fund : , account : ) and also (from and to) in switch type deals.


Training Folder Contains the procedure of Training DeepSpeech and Spacy.

