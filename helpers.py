import folium
#selium used to save image from web
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import numpy as np
import cv2
#import earth engine api and authenticate/initizlize
import ee
from google.oauth2.service_account import Credentials 
from google.oauth2 import service_account
# ee.Authenticate()
credentials = Credentials.from_service_account_file('./static/jsonkey.json', scopes=['https://www.googleapis.com/auth/cloud-platform'])
ee.Initialize(credentials=credentials)

# Define a method for displaying Earth Engine image tiles to folium map.
def add_ee_layer(self, ee_image_object, vis_params, name):
    map_id_dict = ee.Image(ee_image_object).getMapId(vis_params)
    folium.raster_layers.TileLayer(
        tiles = map_id_dict['tile_fetcher'].url_format,
        attr = 'Map Data © <a href="https://earthengine.google.com/">Google Earth Engine</a>',
        name = name,
        overlay = True,
        control = True
    ).add_to(self)


def getBeforeAndAfterImages(coordinates):
    #DATA FOR BEFORE
    dataset = ee.ImageCollection("JAXA/ALOS/PALSAR/YEARLY/FNF")\
    .filterDate('2007-01-01', '2007-01-31')\
    .median()
    #select the forest non forest data layer
    forestNonForest = dataset.select('fnf')
    #create visualization
    forestNonForestVis = {
        'min':1.0,
        'max':3.0,
        'palette': ['006400', 'FEFF99', '0000FF']
    }
    # Add EE drawing method to folium.
    folium.Map.add_ee_layer = add_ee_layer
    #Create a folium map object
    my_map = folium.Map(location = [float(coordinates[0]),float(coordinates[1])], zoom_start = 4) #(y,x),(s,w) south America: -20,-60
    #add the layer to the map object
    my_map.add_ee_layer(forestNonForest, forestNonForestVis, 'Forest/Non-Forest')
    #Add a layer contorl panel
    my_map.add_child(folium.LayerControl())
    #saving and displaying image
    my_map.save('/Users/sasankgamini/Desktop/CruzHacks/deforestationMap.html')
    mapurl = "file:///Users/sasankgamini/Desktop/CruzHacks/deforestationMap.html" #You have to give full path to your HTML file
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    # chrome_options.add_argument('window-size=1600,900')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(mapurl)
    time.sleep(3)
    driver.save_screenshot("static/outputBefore.png")
    driver.quit()





    #DATA FOR After
    dataset1 = ee.ImageCollection("JAXA/ALOS/PALSAR/YEARLY/FNF")\
    .filterDate('2017-01-01', '2017-01-31')\
    .median()
    #select the forest non forest data layer
    forestNonForest1 = dataset1.select('fnf')
    #create visualization
    forestNonForestVis1 = {
        'min':1.0,
        'max':3.0,
        'palette': ['006400', 'FEFF99', '0000FF']
    }
    # Add EE drawing method to folium.
    folium.Map.add_ee_layer = add_ee_layer
    #Create a folium map object
    my_map1 = folium.Map(location = [float(coordinates[0]),float(coordinates[1])], zoom_start = 4) #(y,x),(s,w) south America: -20,-60
    #add the layer to the map object
    my_map1.add_ee_layer(forestNonForest1, forestNonForestVis1, 'Forest/Non-Forest')
    #Add a layer contorl panel
    my_map1.add_child(folium.LayerControl())
    #saving and displaying image
    my_map1.save('/Users/sasankgamini/Desktop/CruzHacks/deforestationMap.html')
    mapurl1 = "file:///Users/sasankgamini/Desktop/CruzHacks/deforestationMap.html" #You have to give full path to your HTML file
    chrome_options1 = Options()
    chrome_options1.add_argument('--headless')
    # chrome_options1.add_argument('window-size=1600,900')
    driver1 = webdriver.Chrome(options=chrome_options1)
    driver1.get(mapurl)
    time.sleep(3)
    driver1.save_screenshot("static/outputAfter.png")
    driver1.quit()



    #Getting Before Image
    imageBefore = cv2.imread('static/outputBefore.png')
    imageBefore = cv2.resize(imageBefore, (600,480))
    #convert to hsv to make it easier to find range of green
    hsvimage = cv2.cvtColor(imageBefore, cv2.COLOR_BGR2HSV) 
    #converting hsv values to np arrays
    lowgreen = np.array([(36,0,0)])
    highgreen = np.array([(86,255,255)])
    #finding all green pixels(black/white image)
    mask = cv2.inRange(hsvimage, lowgreen, highgreen)
    #took original image and multiplied it with the black/white image(mask image) and black pixels ended up being the same since it has a value of zero
    finalImageBefore = cv2.bitwise_and(imageBefore,imageBefore,mask=mask)



    #Getting After Image
    imageAfter = cv2.imread('static/outputAfter.png')
    imageAfter = cv2.resize(imageAfter, (600,480))
    #convert to hsv to make it easier to find range of green
    hsvimage = cv2.cvtColor(imageAfter, cv2.COLOR_BGR2HSV) 
    #converting hsv values to np arrays
    lowgreen = np.array([(36,0,0)])
    highgreen = np.array([(86,255,255)])
    #finding all green pixels(black/white image)
    mask = cv2.inRange(hsvimage, lowgreen, highgreen)
    #took original image and multiplied it with the black/white image(mask image) and black pixels ended up being the same since it has a value of zero
    finalImageAfter = cv2.bitwise_and(imageAfter,imageAfter,mask=mask)


    #finding all black pixels(black/white image) in before image
    beforeImageGrayscale = cv2.cvtColor(finalImageBefore, cv2.COLOR_BGR2GRAY)
    #finding coordinates of black pixels in before image
    # coordsBlackBefore = np.column_stack(np.where(beforeImageGrayscale == 0))

    #finding all black pixels(black/white image) in after image
    afterImageGrayscale = cv2.cvtColor(finalImageAfter, cv2.COLOR_BGR2GRAY)
    #finding coordinates of black pixels in after image
    # coordsBlackAfter = np.column_stack(np.where(afterImageGrayscale == 0))

    #finding coords where there is black in after image, and green in before image
    coordsBlackDifference = np.column_stack(np.where((afterImageGrayscale == 0) & (beforeImageGrayscale != 0)))


    #plotting red where there used to be trees
    deforestationImage = imageAfter.copy()
    for coord in coordsBlackDifference:
        deforestationImage[coord[0],coord[1]] = (0,0,255)

    #Saving Images
    cv2.imwrite('static/BeforeImage.png', imageBefore)
    cv2.imwrite('static/AfterImage.png', imageAfter)
    cv2.imwrite('static/result.png', deforestationImage)

    # cv2.imshow('Image Before Deforestation',imageBefore)
    # cv2.imshow('Image After Deforestation',imageAfter)
    # cv2.imshow('Representation', deforestationImage)
    # cv2.waitKey()
    # cv2.destroyAllWindows()