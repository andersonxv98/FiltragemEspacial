import cv2

import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


class Realce:
    def __init__(self, im, name):
        self.im = im
        self.name = name

    def show(self):
        Image.fromarray(self.im).show()
    def calculohistograma(self):
        hI = []
        print(self.im)
        for i  in range(self.im.max()+1):
            hI.append(0)

        for x in range(len(self.im)):
            for y in range(len(self.im[x])):
                pos = (self.im[x,y])
                hI[pos] += 1



        return hI

    def plotHistograma(self):
        hI = self.calculohistograma()
        print("inwsidde plotHistogram", hI)
        intensidades = [i for i in range(len(hI))]
        plt.plot( intensidades, hI)
        plt.xlabel('intensidade')
        plt.ylabel('quantidade')
        plt.title(self.name)
        plt.show()


    def equalizacaoPf(self):
        histogramaOriginal = self.calculohistograma()
        pfAcumulada= []
        lastPAcumulado = 0
        for k in histogramaOriginal: #para cade nivel de cinza no histograma
            p= k/sum(histogramaOriginal)
            lastPAcumulado += p
            pfAcumulada.append(round(lastPAcumulado * self.im.max()))

        return pfAcumulada

    def plotHistogramaEqualizado(self):
        pfAcumuladaEqual = self.equalizacaoPf()
        print("inwsidde plotHistogram", pfAcumuladaEqual)
        intensidades = [i for i in range(len(pfAcumuladaEqual))]
        plt.plot(intensidades, pfAcumuladaEqual)
        plt.xlabel('intensidade')
        plt.ylabel('quantidade')
        plt.title(self.name+'|equalizado')
        plt.show()

    def equalizeImg(self):
        histoEq = self.equalizacaoPf()
        for i in range(len(self.im)):
            for j in range(len(self.im[i])):
                self.im[i][j] = histoEq[self.im[i][j]]

        Image.fromarray(self.im).show()

    def correcaoGamma(self, gamma, c):
        c = c
        compensacao= 1


        gx = pow((c * (self.im+ compensacao)), gamma)
        Image.fromarray(gx).show()

    def negativo(self):
        max_intensit  = self.im.max()
        for i in range(len(self.im)):
            for j in range(len(self.im[i])):
                self.im[i][j] = max_intensit - self.im[i][j]


        Image.fromarray(self.im).show()
