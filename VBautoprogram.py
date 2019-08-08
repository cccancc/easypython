# -*- coding: utf-8 -*-
# # Project: VB Auto Programming
# Name: 
# Date: 2019/8/8
# Description: This program will allow user to enter the part 
#                number and brand and look up the corresponding VB Auto part number.

# initialize variables
filename=''
strPartNumber=''
BrandList=[]
listsBrand=[]
dirBrand={}

def main():

    # import data files
    contentBrandA=fileInput('BrandA.txt')
    contentBrandC=fileInput('BrandC.txt')
    contentBrandX=fileInput('BrandX.txt')
    contentBrandVB=fileInput('BrandVB.txt')
    # generate directory of master list
    for i in range(len(contentBrandA)):
         BrandList=[contentBrandA[i],contentBrandX[i],contentBrandC[i]]
         listsBrand.append(BrandList)
         
    dirBrand=dict(zip(contentBrandVB,listsBrand))

    # ask user to input part number from Brand A.C.X
    strPartNumber=str(input("Please input he part number from Brand A, Brand X and Brand C:"))
    # search the Master List
    for value in dirBrand:
        for index in range(len(dirBrand[value])):
            if dirBrand[value][index]==strPartNumber:
                #  print found  VB Auto Part number
                print('BrandVB is:'+value)

# a function to import 4 file
def fileInput(filename):
    # Try to read a txt file and return a list.Return [] if there was a mistake.
    try:
        file = open(filename,'r')
    except IOError:
        error = []
        return error
    content = file.readlines()

    for i in range(len(content)):
        content[i] = content[i][:len(content[i])-1]
    file.close()
    return content

main()