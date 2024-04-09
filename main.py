import os

from realce import Realce
from ruidos import Ruidos
import cv2
from filtros import Filtros
def main():

    #exercicio4

    #exercicio6
    for imagem in os.listdir("./images4"):
        img = cv2.imread('./images4/'+imagem, cv2.IMREAD_GRAYSCALE)
        #filtro = Filtros(img)
        ruido = Ruidos(img)
        #ruido.plotHistograma()
        img_gaussian = ruido.plotGaussian()
        filtro = Filtros(img_gaussian)
        #f1 = filtro.filtroGaussiano(2)
        f1 = filtro.filtroGaussiano(3)
        f2 = filtro.filtroGaussiano(5)
        f3 = filtro.filtroGaussiano(7)


        filtro.filtroMedia(3)
        filtro.filtroGaussianoIMG(3)
        filtro.filtroDaMediana()
        filtro.filtroModa()
        filtro.filtroPassaAlta3p3()

        print("O filtro gaussiano reduzio melhor a presença de ruído quando aplicado na imagem o ruido gaussino (apesar de não ter reduzido todo o ruido)"
              ". Mas dentre todos os filtros esse é o que aparentemente obteve visualmente um melhor desempenho")
        return
        '''
        err_max =ruido.erromaximo(img_gaussian)
        err_md_abs = ruido.errmomedioabsoluto(img_gaussian)
        err_md_sqr= ruido.erromedioquadratico(img_gaussian)
        raiz_err_md_sq =ruido.raizdoerromedioquadratico(img_gaussian)
        err_md_sqr_norm = ruido.erromedioquadraticonormalizado(img_gaussian)
        jaccard = ruido.coeficientedeJaccard(img_gaussian)
        '''




    #EXERCICIO 7 Equalização de IMAGEM
    '''
    for imagem in os.listdir("./images"):
        img = cv2.imread('./images/'+imagem, cv2.IMREAD_GRAYSCALE)
        realce = Realce(img, imagem)
        realce.show()
        realce.plotHistograma()
        realce.plotHistogramaEqualizado()
        realce.equalizeImg()


    #exercicio9
    for imagem in os.listdir("./images4"):
        img = cv2.imread('./images4/'+imagem, cv2.IMREAD_GRAYSCALE)
        ruido = Ruidos(img)
        ruido.plotHistograma()
        im_gausss =ruido.plotGaussian()
        realce = Realce(im_gausss, imagem)
        #realce.show()
        #realce.negativo()
        realce.correcaoGamma(0.04, 1)
        realce.correcaoGamma(0.4, 1)
        realce.correcaoGamma(2.5, 1)
        realce.correcaoGamma(10, 1)
        #realce.correcaoGamma(25, 1)
        #realce.correcaoGamma(100, 1)

    print("realçar com a correção gamma  permitiu melhorar a qualidade da imagem com o valor de gamma igual a 10, utilização de realce para corrigir uma imagem degradada depende do tipo de realce e quais caraceristicas está sendo buscada para realce.")
    '''
main()