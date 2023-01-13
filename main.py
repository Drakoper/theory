from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

exercises = {
    'Понятие машинного обучения. Отличие машинного обучения от других областей программирования': ['1.png', '2.png', '3.png']
}

def getAnswer(exercise):
    for i in exercises[exercise]:
        img = mpimg.imread('./'+i)
        image = Image.open('./'+i)
        plt.figure(figsize=((image.size[0]/20), (image.size[1]/20)))
        plt.imshow(img)
