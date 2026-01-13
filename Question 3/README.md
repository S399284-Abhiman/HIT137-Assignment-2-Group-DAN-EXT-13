# Recursive Koch Polygon Generator 
## Overview
  This program uses Python’s turtle graphics and recursion to generate a geometric pattern based on the Koch curve.
  Instead of a single line, each side of a polygon is recursively modified to create an inward-pointing Koch indentation.
  
  #### The user can control:
 
   •	The number of sides of the starting polygon.
 
   •	The length of each side.

   •	The recursion depth (how many times the Koch indentation recurs).

## How It Works:
  ### Koch Inward Rule

 #### For each straight line:
  
  1.	Divide the line into three equal segments.
     
  2.	Replace the middle segment with two sides of an equilateral triangle pointing inward.
     
  3.	This turns one line into four smaller segments.
     
  4.	The same process is applied recursively based on the chosen depth.

  #### Polygon Construction
  
   •	A regular polygon is drawn
  
   •	Each side of the polygon is replaced by an inward Koch curve.
  
   •	The turtle turns by 360 / number of sides after each side.
  
   •	main block Collects user input and starts the drawing.

   
## Code Structure
  1.	  koch_inward()
      Recursive function that draws a single inward Koch curve.

  2.	    draw_inward_koch_polygon()
      Draws a polygon where each side is a Koch curve.

 ## User Inputs                 

#### Number of sides:	             
  Determines the base polygon (e.g. 3 = triangle, 4 = square).

#### Side length (pixels):	       
  Length of each polygon side.

#### Recursion depth:	              
  Number of recursive subdivisions.


## Example
  Enter the number of sides: 4
  
  Enter the side length (pixels): 300
  
  Enter the recursion depth: 3

## How to Run
1.	Run the program using:
   
2.	    Recursive Function (Koch Polygon).py

3.	Enter the requested values when prompted.




