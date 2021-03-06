# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 23:29:55 2018

@author: Monika Asawa
"""

import pandas as pd
import numpy as np


'This function will generate the product category entities'
def loadProducts():
    
    df = pd.read_csv('products_export.csv')
    
    Products = pd.DataFrame(df, columns=['Handle','Type'])
    print(Products.head())
    
    # mark "Other Exiciting Products" values as missing for Product having missing Product Category
    Products['Type'] = Products['Type'].replace(np.NaN,'Other_Exiciting_Products')
    
    grouped = Products.groupby(['Type'])
    
    ProductsEn = {}
    
    for name, group in grouped:
        print(name)
        sunDF=group['Handle']
        ProductsEn[name] = sunDF.values.T.tolist()  

    print(ProductsEn)
     
    return ProductsEn

def loadProductCategories():
    
    print("loadProductCategories called")
    ProductsEn = loadProducts()
    
    response = ""
    for key in ProductsEn.keys():
      response +=  "," + key 
    response = response[1:]
    print(response)
    
    return response
    
def loadProductTitle(productCategory):
    
    ProductsEn = loadProducts()
    
    response = ProductsEn[productCategory]

    print(response)
    
    return response
    
    
    