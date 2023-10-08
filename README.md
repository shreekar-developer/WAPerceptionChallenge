
# Fall 2023 WA Perceptions Challenge - Shreekar Earanti

This is my Fall 2023 submisson for the Wisconsin Autonomous Perceptions team coding challenge.

## Methodology
I based the solution using the OpenCV Python Package. I used Google Colab to develop and test the solution.

1. I split the picture down the middle into two pictures. I did this to simplify drawing the lines between the cones in future steps. 
2. I converted the image to HSV color space. 
3. I adjusted the lower and upper bounds of the HSV parameters to find only the red hue in the cones and set those. 
4. Then a mask was made from which the contours were found for the red cones. 
5. Then using the contours from the mask, I found the centroids of the cones which will be used to connect them for lines. 
6. I also cut the upper 1/4 section of the picture from the centroid calculation and line drawing as the light reflections and doors were causing extraneous lines to be drawn. 
7. The lines were drawn connecting the centroids of each cone on each side. 
8. After they were drawn, the images were connected back together and were then displayed.

## Some things I tried and why it didn't work/why I changed it
1. One thing I tried was to detect the cones using RGB color space which did not work as well as the HSV color space as with HSV, more details about hues can be accounted for with it being closer to human experience of the color. 
2. Another thing I initially did was keeping the picture as one picture and not splitting it. This resulted in lines being drawn across the center from left to right and vice versa between the cones. To solve this, I split the picture in the middle and reattached it at the end. 
3. I also initially did not cut out the top 1/4 of the image in centroid calculation and line drawing. This resulted in centroids being calculated for the red lights reflecting off the ground of the floor. And then a line would be drawn to this centroid. 
4. I also initially converted the image to grayscale and then used a gaussian blur but this did not help with masking and contour detection so I removed it and converted it to the HSV color space.
5. I also initially only connected the endpoints of the cones but this missed some of them and was not as accurate, so instead the lines connect between each centroid. 

## Packages & Libraries
1. OpenCV
2. Numpy
3. cv2_imshow from Google Colab
