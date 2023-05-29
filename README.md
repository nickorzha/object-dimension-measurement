# Objects Dimensions Measurement
Objects dimensions measurement can be very useful for measuring the object's dimension without any ruler (ofcourse !). 
#### Machines got eyes 👁

<img src = "https://github.com/adrian-krol/object-dimension-measurement/blob/master/Results/objects_size_result.gif" width=450>
<img src = "https://github.com/adrian-krol/object-dimension-measurement/blob/master/Results/result_objects2.jpg" width=350>

### What's Inside?
<ol>
<li><b><u>Important!</u> Place a refernece object at the left-most side
measure it's dimensions (only of this object). We should be able 
to easily find this reference object in an image, either based on 
the placement of the object (such as the reference object always 
being placed in the top-left corner of an image) or via appearances 
(like being a distinctive color or shape, unique and different from
all other objects in the image). </b></li>
<li><b>Find the edges of objects using Canny edge Detection.</b></li>
<li><b>Find and grab The Contours using imutils library function.</b></li>
<li><b>Sort the contours in x-axis direction</b></li>

<li><b> Grab the quarter (which will always be the first contour in the sorted list), and use it to define our pixels_per_metric, which we define as:<br>
              pixels_per_metric = object_width / know_width</b></li>
 
 <li><b>Bound the contours using a rectangle (box) and obtain the corners of box.</b></li>
  <li><b>Calculate the size of objects using the dimensions of box(contours).</b></li>

</ol>
<br><small>TIPS : Don't forget to dilate and erode after edge detection</small>
