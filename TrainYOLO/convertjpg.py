from PIL import Image
import pandas as pd

image_root = '/Users/duxtonlimyeecheng/Documents/Year 3 Final Year/Final Year Project/TrainYOLO/TrainYourOwnYOLO/Data/GTSRB/GTSRB-Final-Training/Final_Training/Images/'
for f in range(0,43):
    # save folder name as the format: 00042
    folder = format(f, '05d')
    csv_path = image_root + folder + '/GT-' + folder + '.csv'
    csv = pd.read_csv(csv_path, sep= ';')
    ppm_name = csv['Filename']
    # len(ppm_name) = how many rows in csv file
    for i in range(0, len(ppm_name)):
        # select 1/3 as testing image
        if i % 3 == 0:
            im = Image.open(image_root + folder + '/' + csv['Filename'][i])
            im.save('TestJPG/' + format(f, '02d') + '_' +
                    csv['Filename'][i].replace('ppm', 'jpg'))
        else:
            im = Image.open(image_root + folder + '/' + csv['Filename'][i])
            im.save('TrainJPG/' + format(f, '02d') + '_' +
                    csv['Filename'][i].replace('ppm', 'jpg'))