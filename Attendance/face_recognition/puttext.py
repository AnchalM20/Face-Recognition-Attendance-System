import cv2 
    
# path 
path = r'C:\Users\admin\Desktop\cutomfaces\dataset\Ujala\frame7.jpg'
    
# Reading an image in default mode 
image = cv2.imread(path) 
    
# Window name in which image is displayed 
window_name = 'Image'
  
# font 
font = cv2.FONT_HERSHEY_SIMPLEX
  
# org 
org = (50, 80) 
  
# fontScale 
fontScale = 2

# Blue color in BGR 
color = (255, 0, 0) 
  
# Line thickness of 2 px 
thickness = 2
   
# Using cv2.putText() method 
image = cv2.putText(image, 'OpenCV', org, font,  
                   fontScale, color, thickness, cv2.LINE_AA) 
   
# Displaying the image 
cv2.imshow(window_name, image)  

key = cv2.waitKey(0)
		
if key == ord("q"):
    cv2.destroyAllWindows()
    