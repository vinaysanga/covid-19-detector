# covid-19-detector using X-rays

This website demonstrates the concept of detecting covid-19 infection from the Posteroanterior(PA) X-rays. It uses Resnet-50 for Classification of the images. This should not be used for primary diagnostics as this is a Proof-of-Concept that chest x-rays can be used to detect the covid infection.

Dataset used : [covid-chestxray-dataset](https://github.com/ieee8023/covid-chestxray-dataset)

Kernel inspired from : [Coronavirus disease 2019 (COVID-19) X-Ray Scanner](https://github.com/ajsanjoaquin/COVID-19-Scanner)

## Steps to run:
1. Clone or download the repo and then cd to the folder.
```
git clone https://github.com/vinaysanga/covid-19-detector-using-x-rays.git
cd covid-19-detector-using-x-rays
```
2. Install the required packages using, 
```
pip3 install -r requirements.txt
```
3. Download ```'export.pkl'``` file by following instructions from ```'/models/instructions.txt'```.
3. Run the project using
```
python3 app.py
```
4. Click to link shown in terminal to open it into your web browser.

Fin..
