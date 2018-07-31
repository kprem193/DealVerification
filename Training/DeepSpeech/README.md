References:
https://github.com/mozilla/DeepSpeech

## DeepSpeech - CPU Training:

Install Git-LFS :
``` 
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
sudo apt-get install git-lfs
```
Clone DeepSpeech Repo :
```
git clone https://github.com/mozilla/DeepSpeech.git
```
Download the pre-built models (graph file and vocab):
```
wget -O - https://github.com/mozilla/DeepSpeech/releases/download/v0.1.1/deepspeech-0.1.1-models.tar.gz | tar xvfz -
```
### Install the requirements:
```
pip3 install -r requirements.txt
```
If there is an error in installing cryptography run this command:
```
sudo apt-get install build-essential libssl-dev libffi-dev python-dev
pip install cryptography
```
Install sox mp3 handler
```
sudo apt-get install libsox-fmt-mp3
```
Download the pre-built binaries:
```
python3 util/taskcluster.py --target .
```
Prepare the data for training
Make 3 csv files train.csv, test.csv, dev.csv

Format of csv : 'wav_filename', 'wav_filesize', 'transcript'

Run the following command to start the training from scratch:
``` 
python3 ./DeepSpeech.py --checkpoint_dir provide_checkpoint_directory/ --epoch provide_number_of_epoch(10) --train_files train.csv --dev_files dev.csv --test_files test.csv --export_dir provide_the_directory_to_get_output_graph --decoder_library_path ./libctc_decoder_with_kenlm.so
```
Run the following command to start the training the pretrained model :
```
python3 ./DeepSpeech.py --n_hidden 2048 --initialize_from_frozen_model models/output_graph.pb --checkpoint_dir provide_checkpoint_directory/ --epoch provide_number_of_epoch(10) --train_files train.csv --dev_files dev.csv --test_files test.csv --export_dir provide_the_directory_to_get_output_graph --decoder_library_path ./libctc_decoder_with_kenlm.so
```


