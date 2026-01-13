# Recursive Koch Polygon Generator 
## Overview
  This program uses Python’s turtle graphics and recursion to generate a geometric pattern based on the Koch curve.
  Instead of a single line, each side of a polygon is recursively modified to create an inward-pointing Koch indentation.
  
  The user can control:
 
  •	The number of sides of the starting polygon
 
  •	The length of each side

  •	The recursion depth (how many times the Koch indentation recurs)

## How It Works:
  ### Koch Inward Rule

 #### For each straight line:
  
  1.	Divide the line into three equal segments
     
  2.	Replace the middle segment with two sides of an equilateral triangle pointing inward
     
  3.	This turns one line into four smaller segments
     
  4.	The same process is applied recursively based on the chosen depth
     

