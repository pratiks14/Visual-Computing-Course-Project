exec(open("Lib/Utils.py").read())
import os
from PIL import Image
import pandas as pd
if not os.path.isdir('Data_Images'):
    
    exec(open("Lib/Utils.py").read())

    os.mkdir('Data_Images')
    os.mkdir('Data_Images/Training')
    os.mkdir('Data_Images/Training/Anger')
    os.mkdir('Data_Images/Training/Disgust')
    os.mkdir('Data_Images/Training/Fear')
    os.mkdir('Data_Images/Training/Happiness')
    os.mkdir('Data_Images/Training/Sadness')
    os.mkdir('Data_Images/Training/Surprise')
    os.mkdir('Data_Images/Training/Neutral')

path_train = "Data/data_train.csv"
Categories = ['Anger', 'Disgust', 'Fear', 'Happiness', 'Sadness', 'Surprise', 'Neutral']
categories_wise_img_cnt = [0] * 7

for df in pd.read_csv(path_train,sep=';', chunksize=2000):
    training_imagesRGB, training_labels= etl_data(df)

    

    training_imagesRGB_trunc = np.floor(training_imagesRGB)
    for k in range(len(Categories)):
        a = training_imagesRGB_trunc[training_labels[:, k] == 1, :, :, :]
        img_cnt = categories_wise_img_cnt[k]
        for i in range(a.shape[0]):
            b = a[i, :, :, :].astype('uint8')
            im = Image.fromarray(b, mode='RGB')
            img_cnt+=1
            im.save("Data_Images/Training/"+Categories[k]+"/Images"+str(img_cnt)+".jpeg", subsampling=0, quality=100)
        categories_wise_img_cnt[k] = img_cnt
    
    



# RESET
for element in dir():
    if element[0:2] != "__":
        del globals()[element]
del element