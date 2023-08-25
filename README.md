
# Project Title : Mapping The Unmapped
## Introduction:
It introduces a geospatial hashing algorithm intends to address the problem based on Nepal's context and geography. 

## How It Works:
The address is divided into four parts. The first part is District Number. It is generated from the district number of land line . The second part determines whether the location is Metropolitian, Sub Metropolitian, Municipality and Sub Municipality along with their name . Their name is written in the shortcut form. In three letters on shortcut form. Thirdly, there is a special place called landmark in our location. We extract the nearest landmark from the given location co-ordinates on the basis of distance. Landmark with shortest distance is selected and full name of landmark is written. 

The main hashing of location is done in the forth part. 
Here we find the distance between given coordinates and nearest landmark. After that,  we use BASE64 encoded vegenere ciphers to encrypt the distance. 
After that, the distance and the degree between two points: the chosen nearest landmark and the desired co-ordinate point is calculated. The calculated distance and degree are converted into BASE-64 to shorten the length of the resulting values. Then, the shortened values are encoded with the help of vegenere cipher. Then, the combination of district, city, landmark and encoded values gives the required combination. i.e xxx-xxx-xxxxxxxxxxxx-xx-xx format