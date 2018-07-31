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

