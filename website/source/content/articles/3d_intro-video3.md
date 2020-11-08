Title: Ice Cream Tutorial Part 1 - Modelling
Author: Anthony Gallas
Date: 16/07/2020
Category: 3D Modelling
Tags: 3D, 3D modelling, modelling, Ice Cream, Ice Cream Project
Slug: ice-cream-part1-modelling
Series: 3D Modelling
Series_index: 06
Sortorder: 06

{% youtube naCSTLMeQZ0 [560] [315] %}


## Introduction
This documentation is intended as a text guide to accompany the first video in the "Ice Cream Tutorial" series.

**If you are continuing on from the "Getting Started" series, go to File drop-down in the top left corner of Blender's interface.</br>
Select New and General. Then Delete the default cube, camera, and light.**

![iceCreamIntro](../img/intro-video3/iceCreamIntro.png)

## Step 1 - Add a Cone Object

First, lets make the cone that we will put our ice cream into.

**Press Shift+A to bring up the add menu.  Select "_Mesh_" and "_Cone_".**

![iceCreamStep1](../img/intro-video3/iceCream1Step1.JPG)

**In the lower left hand corner your will see a black box that says "Add Cone".  Click on that to open it.**<br>
_NOTE: If you click anywhere else, after adding Your cone, that box will dissapear, just delete your object and re-add it to get it back._

![iceCreamStep1-1](../img/intro-video3/iceCream1Step1-1.JPG)

**Set Cone Values to:<br>
 Vertices: 12<br>
 Radius 1: 1m<br>
 Radius 2: 0m<br>
 Depth: 2.5m<br>
 Rotation X: 180**

_NOTE: Vertices should always be set to the lowest amount needed to get the general shape you want._

![iceCreamStep1-2](../img/intro-video3/iceCream1Step1-2.JPG)

## Step 2 - Hollow Out The Cone

**In the upper-left hand corner, where it says "_Object Mode_", click the drop-down menu and select "_Edit Mode_"**<br>
_NOTE: The Hotkey to go between "Object Mode" and "Edit Mode" is **TAB**_

![iceCreamStep2](../img/intro-video3/iceCream1Step2.JPG)

Next to the drop-down list, you will see 3 buttons.  "Vertice Select","Edge Select", and "Face Select". **Click on "Face Select"**.

![iceCreamStep2-1](../img/intro-video3/iceCream1Step2-1.JPG)

**Left-Click on the top flat portion of your cone to select it.**<br>
**Then press "I" to create an inset in your cone and move your mouse to adjust; Left-Click to set**<br>  _How thick you make this is how thick your cone will be._

![iceCreamStep2-2](../img/intro-video3/iceCream1Step2-2.JPG)

![iceCreamStep2-3](../img/intro-video3/iceCream1Step2-3.JPG)

**Press "_Numpad 1_" to see the side-view of the cone.<br>
 Press "_E_" (_E for Extrude_) to extrude the top face of your cone and pull it down to near the bottom of your cone. Left-click to set<br>
 Press "_S_" to scale the bottom inward towards the center of the cone until it dissapears inside the cone. Left-click to set.**

![iceCreamStep2-4](../img/intro-video3/iceCream1Step2-4.JPG)

![iceCreamStep2-5](../img/intro-video3/iceCream1Step2-5.JPG)

![iceCreamStep2-6](../img/intro-video3/iceCream1Step2-6.JPG)

**Press _TAB_ to go back to "_Object Mode_".**  **Left-click on your cone and press "_Numpad ._"** to refocus on it.

Finally, **right-click on your cone and click "_Shade-Smooth_."**

![iceCreamStep2-7](../img/intro-video3/iceCream1Step2-7.JPG)

## Step 3 - Add Ice Cream to Cone

**Press _Shift+A_ and under "_Mesh_" select "_UV Sphere_".**

![iceCreamStep3](../img/intro-video3/iceCream1Step3.JPG)

**Set UV Sphere Values to:<br>
 Segments: 16<br>Rings: 9<br>Radius: 1m<br>**

_ADVICE: The squarer the faces of your sphere are, typically the better._

 ![iceCreamStep3-1](../img/intro-video3/iceCream1Step3-1.JPG)

**Press _G_, then _Z_ to move your sphere up to the top of the cone. Left-click to set**<br>

![iceCreamStep3-2](../img/intro-video3/iceCream1Step3-2.JPG)

**Press _S_ to scale the sphere so that it fits inside the cone**

![iceCreamStep3-3](../img/intro-video3/iceCream1Step3-3.JPG)

How many scoops of ice cream is up to you.  This tutorial covers 3 scoops.<br>
**To add another scoop, with your sphere selected, press _Shift+D_ to duplicate, then _Z_ to move it straight up. Left-click to set**

![iceCreamStep3-4](../img/intro-video3/iceCream1Step3-4.JPG)

Once you have it where you like it, then **press _S_ to scale it in and make it slightly smaller.**

![iceCreamStep3-5](../img/intro-video3/iceCream1Step3-5.JPG)

**Repeat this process for each new scoop.**

![iceCreamStep3-6](../img/intro-video3/iceCream1Step3-6.JPG)

## Step 4 - Naming the shapes in your object

In the upper right hand corner of the interface, you will see a window with a list of the default names of all the shapes used for your ice cream cone model.<br>
Notice how each object becomes highlighted when you click on them in the list.

![iceCreamStep4](../img/intro-video3/iceCream1Step4.JPG)

It is important to rename these to objects to easily keep track of all your shapes and what they are.

**Double-click the object, from the list, that is your bottoms ice cream scoop.**  Most likey it will be named "Sphere."<br>
**Rename this to something unique.  Let's call it "_Bottom Cream_".**<br>
**Make unique names for all the other shapes**
![iceCreamStep4-1](../img/intro-video3/iceCream1Step4-1.JPG)

![iceCreamStep4-2](../img/intro-video3/iceCream1Step4-2.JPG)

## Step 5 - Add Subsurface Modifer to Cone and Spheres

**Select your top ice cream sphere.**<br>
**Select Modifer Properties and open the _Add Modifer_ drop down menu.<br>Select "_Subdivision Surface_"**

![iceCreamStep5](../img/intro-video3/iceCream1Step5.JPG)

![iceCreamStep5-1](../img/intro-video3/iceCream1Step5-1.JPG)

**Set _Render_ to 3 and _ViewPort_ to 3 and click _Apply_**

![iceCreamStep5-2](../img/intro-video3/iceCream1Step5-2.JPG)

**Select the rest of your shapes, one by one, and repeat Step 5 for each one.**

![iceCreamStep5-3](../img/intro-video3/iceCream1Step5-3.JPG)

## Conclusion

In Part 2 we will cover materials and sculpting and turn our ice cream cone into something like this:

![iceCreamStepConcl](../img/intro-video3/iceCream1Concl.JPG)
