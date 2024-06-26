# PLAIN
(**P**)ropelled (**L**)inkage (**A**)ircraft (**I**)ntercommunication (**N**)ighthawk

&nbsp;


## Table of Contents
* [Planning](Planning.md)
* [Phase 0](#phase_0)
* [Phase 1](#phase_1)
* [Phase 2](#phase_2)
* [Phase 3](#phase_3)
* [Phase 4](#phase_4)
* [Launching](#launching)
* [Analysis](#analysis)
* [Final reflection](#Tying_it_all_together)


&nbsp;

## Phase_0
### Week 1
#### Reflection

This week we worked on our planning document. We created, outlined, and filled in most of our google doc. We drew up our first sketches and calculated the cost of parts while also starting to outline our timeline. This week was mainly talking with Afton's group and brainstorming how we wanted to do the linkage.

#### Images
![sketch1](images/sketch1.png)
![sketch2](images/sketch3.png)

### Week 2
#### Reflection

This week we completed our planning document. We finished the timeline, code blocks, and the rest of the google doc. Then we created a github repo and moved all of the information from the doc to the github planning document. We fleshed out a more concrete plan with aftons group and made our schedueles so that there was a lot of overlap and we would check in every now and then. 

#### Images
![cbd](images/steeringCBD.png)

### Week 3
#### Reflection

This week we prototyped the PLAIN with shop materials. Vinnie was out sick this week so Matthias had to take charge and created our prototype. Matthias made it out of wood, styrofoam, a 9v battery, and a motor. The prototype did not fly and was not areodynamic at all. The only thing that worked was the switch that was soldiered to the motor and turned it on. We decided that it was best to move on with the project and not waste too much time trying to made a working prototype. 

#### Images
![prototype](images/prototype.png)

## Phase_1
### Week 4
#### Reflection

This week we worked together to make the first prototype in CAD. A general style was followed rather than planning for real world functionality. The only thing that was made to realistic standards was the air foil of the aft horizontal stabilizers. The air foil was made with a spline and modeling a common RC plane air foil.

#### Images
![cadprototype](images/cadprototype1.png)

### Week 5
#### Reflection

This week Vinnie started the code, and as a proof of concept he wanted to wire a potentiometer to a motor and have it cotrol the speed using the map function. He also orderd the RC components to hopefully start working on it ASAP. Matthias started a new CAD design and thought it would be a good idea to make the fuselage deign layer by layer and then connect them by two pins.

#### Images
![potcode](images/potcode.png)
![ribs](images/RibDesign.png)

### Week 6
#### Reflection

This week we cut and built the prototype for the rib design. The laser printed pins didn't fit tightly all the way through and there was no plan on how to connect the wings so it turned out just to be a losely fitting body. Vinnie also worked on getting the RC to function and eventually got a succesful wireless conection and it turned on lights on command. It was hard initially because he didn't know to pullup or to pulldown and forgot that it would function the same a normal button.   


#### Images
![ribprototype](images/ribprototype.jpg)
![rlights](images/rclights.gif)

## Phase_2
### Week 7
#### Reflection

This week Matthias tried to fix the prototype while Vinnie worked on getting the RC to give signals that he was able to recieve and use as inputs in his code. The rib prototype did not end up looking redeemable to matthias and after much frustration it was scrapped. Vinnie got a servo to be able to turn using only RC as inputs. He used code from earlier in the year to make the process easier. 

#### Images
![rcinputscode](images/rcinputscode.png)

### Week 8
#### Reflection

This week Matthias tried a new cad design that HIGHLY resembled a neighboring groups CAD. Aside from the apparent problems, the biggest one was that the design he was "inspired by" was meant to be a glider and in no way had the design intention of gaining speed and producing lift with a motor. Vinnie continued working with the RC and expirimented with the wiring. He also ordered the motor so that he could start working on it. 

#### Images
![copycat](images/Copycatdesign.png)

## Phase_3
### Week 9
#### Reflection

This week we were supposed to work on linkage with Afton's team but both of our groups were not ready to link yet. Matthias scrapped the copycat design and then started working on a more solid design that we will hopefully use in the final version. Vinnie started working on voltage dividers so there could be one power source that powers the pico and motors together. This required much googling and circuit planning.

#### Images
![winglite](images/Wing2.png)

### Week 10
#### Reflection

This week we were supposed to code the delink protocol and complete the prototype with link. Neither of these things happened because Matthias was still working on his design for CAD and hadn't laser cut it yet. Vinnie was still working on the voltage dividers and experimenting with Mr. Miller's resitor book with many different types of resistors. Matthias also put the servo mount on to the bottom of the wings so that it would be easy to control the flap movement, this idea was also used by Matthew and Afton on their first iteration.

#### Images
![badcad](images/LMAO.png)
![resistors](images/resistors.jpg)

### Week 11
#### Reflection

This week we were supposed to touch up the delink/motor/rc, figuring out weight, first successful solo flights. None of these were acheivable. The link had not been finished, yet alone started with Afton's group. The motor came but Vinnie was busy trying to figure out voltage dividers. The RC needed the motor to be finished, and the PLAIN hadn't been fabricated so the weight and flight could not be acheived. This week matthias got closer to the finished product in CAD and Vinnie realized he didn't actually need the voltage divider from the 9v because the actual motor needed many more amps than a 9v with many outputs had to offer. Vinnie started to catch up on the documentation. 

#### Images
![closercad](images/FusalageXWings.png)

## Phase_4
### Week 12
#### Reflection

This week we were supposed to plan with Afton’s team for linked takeoff but we could neither link nor takeoff. Matthias worked on the last weight reductions and was close to done. Vinnie kept working on the documentaion and caught up to the current date. Vinnie also searched the back for a battery and charger that they could use in the PLAIN. 

#### Images
![hollowing](images/Wing1.png)

### Week 13
#### Reflection

This week we decided to scrap the connection launch because both teams were to far behind to have enough time to test and get good results. Matthias worked on making the wings thinner and hopefully reducing the weight of the plain overall, the wing change was also realized because we did not need such a tall airfoil and the length was going to be more important. This was achieved by changing the shape of the airfoil making every part of the airfoil 1mm thick. Vinnie started setting up the motor and soldered the right connector on the battery so that it worked with the motor. He started looking online for the code for the specific motor and found a few examples.

#### Images
![thick wing](images/Wing1thick.png)
![thin wing](images/newthinwing.png)
![batteryandmotor](images/batteryandmotor.jpg)

### Week 14
#### Reflection

This week we both decided it would be a good idea to move on from the round design of our fusalage to a more square design that would be both easier to make and would allow for all of our electronics to fit better in the fusalage and have a better centre of mass. Matthias also found a new design that we agreed was a good idea to model off of. With the new design Matthias decided to move the servos onto the fusalage and put the wings onto the top of the plain which we believe would allow for more lift. This week Vinnie got his wisdom teeth removed so he was not able to work on the PLAIN.

#### Images
![modeldesign](images/Modeleddesign.png)
![roundfuslage](images/roundfuslage.png)
![first square iteration](images/Frontpeice.png)

### Week 15
#### Reflection

This week Matthias worked on readjusting the plain to make it more aerodynamic and changing the way that the front was angled and adding more supports for the wing connection. Additionally, Matthias put on the back of the fusalage and used a friction fit design which incorperated a 2.45mm diameter metal rods in order to connect the peices together. Matthias used both sketches and fillets in order to make the plain more aerodynamic and also had trouble because the bottom corners of the fuslage were too thin so he had to add a little more filling on the inside of the plain, he did this by using a conic as the top and using the bottom edge of the fuselage to create a sketch then extruded that sketch 2mm into the fuslage to fix the thin issue. This week Vinnie got the motor code working and was able to turn on the motor with the remote control. The code made it so that one button increased the value from 50(rest) to 100(full trottle) by 1 per 0.05 seconds and then decrease by .75 per 0.05 seconds if a second button was pressed. The hardest part was figuring out how to format the motor controller in the code and it required a line that said: dval = int(val)*65535/100. This line converted from bianary to a value the motor controller could use.  

#### Images
![back fuslage](images/Backp2picture.png)
![Aerodynamic fuslage](images/Moreaerodyncicfuslge.png)
![Sketch explination](images/Smartexplination.png)
![Motorcode1](images/motorcode1.png)

## Launching
### Week 16
#### Reflection

This week Matthias and Vinnie went to texas and visited Big Bend national park for spring break. 

#### Images
![Texas trip](images/IMG_4200.jpg)
![Texas Trip v2](images/IMG_3933.jpg)

### Week 17
#### Reflection

We were not ready for launching because we didn't print yet. The code part wasn't done either and was still in the breadboard stage. This week Matthias finished up some last kinks on the PLAIN in order to have printed parts by next week. Matthias pushed out the friction fit connector on the back fusalage all the way to 11mm and on the front to 31mm in order to maximize the connection aspect from both ends. Vinnie worked on setting up the servos to work with the RC controller. He got two servos attached and then was able to make both them go towards 180 with a button on the controller and both go towards 0 with a second button. The setup was not that tricky and he used old servo code from earlier in the project which worked fine. 

#### Images
![Servocode1](images/servocode1.png)
![backconnection](images/Backconnection.png) 
![Front connecter](images/Frontconnecter31mm.png)

### Week 18
#### Reflection

This week we got closer to the final product. The CAD was printed over the weekend and the code was moving along. As the parts were printed Matthias noticed some things were not working right. this was expected from our first draft, one thing Matthias immediately recognized was the the flaps would not be able to rotate very well and it would be hard to put them into the wings the way it was designed. Matthias decided the change the design in order to make it rotate better through the use of hinge pin design(seen below). This method needed to have a rod in the middle of the pins in order to make the rotation perfect so Matthias used one of the rods given to him by matthew. Vinnie worked on finishing the data collecting part of the project. After he completed and tested the data collection then the code was finally done. He forgot how the data collection software needed to be used and had to spend some time reviewing the old assignment. 

#### Images
![codefinal](images/codefinal.png)
![wing change](images/Wing1picutrfpdoc.png)
![Hingepin](images/Hingepindesign.png)


## Analysis
### Week 19
#### Reflection

We could not analize what we didn't have, so we continued to try and finish the PLAIN. This week we finished the re-vitalized CAD and started assmbeling on friday. We kept both the front and back fusalage but the friction fits didn't quite work and we had to use hot glue to get the rods to fit. We also accidently printed two left wings which made the PLAIN unable to be assembled completely. There were also no holes for the wires from the motor to enter through the front back into the cockpit to connect with the PICO. This week Matthias had to print out the right wing after forgetting to put it into the print me. after finishing up what Matthias had started last week, we were able to put all our new parts in the print me and started assembling the changed design that friday. Vinnie took pictures of the wiring so that he could start soldering the permanant board together so that it would fit in the PLAIN. 

#### Images
![wires](images/wiresforswitch.jpg)


### Week 20
#### Reflection

This week we printed the correct set of wings. With all the parts finally materialized we could put it together for real. We threw the completed PLAIN shell back and forth to test the lift and even without the extra weight from the circuit board it did not glide at all. This is when we realized we might have a problem. Unfortunately, the whole PLAIN ened up weighing far too much and even if we added extra length to the wings, the weight to length of wings ratio would not work if we wanted the plain to fly. Vinnie worked on the wiring for the project and came in during his 6th period in order to have more time to work. He got almost all the wiring done and just had to add one more servo. The main problem for Vinnie was not being able to find the small needle nose pliers the lab to assist with soldering the wires. His patients was also tested when certain wires wouldn't soldier together without springing away. Sometimes he used his fingers which hurt. 

#### Images
![planefront](images/junkplainfront.jpg)
![planeback](images/junkplainback.jpg)
![pciotop](images/picotop.jpg)

### Week 21
#### Reflection

This week we still held out hope for the printed shell to work with the electronics, which was honestly a waste of time. We put the finished electronics in the shell and the weight alone was a red flag. We did a couple practice tosses to eachother and it was the same as throwing a baseball; there was no lift whatsoever. Matthias tried to think of alternative ideas to pivot onto because with all of the electronics in the PLAIN wouldn't have enough lift and it would weigh too much. Although we were pretty sure the PLAIN wouldn't work, we still insterted all of the electronics and tossed it, to our dismay, the plain would most likely never fly. Vinnie finished the circuit and had fully fabricated all the the compenents. He tested the hardware and it worked when plugged into the computer, but when it was running off of the battery there was not enough power to keep everything running. He then figured out that he needed to send the motor control power through the pico instead of straight from the battery which drew too many amps because of the way it was hooked up. At the end of the week the system was fully funtioning off of the batteries and could be controlled anywhere. Vinnie also created a plane out of cardboard, duct tape, and dowles as a joke. (foreshadowing)

#### Images
![picobottom](images/picobottom.jpg)
![Pivot](images/Pivotimagev4.png)


### Week 22
#### Reflection

This week no work got done Because of the AP exams

#### Images
![apexams](images/apexams.png)


### Week 23
#### Reflection

This week we realized that if we didn't have a succesful flight, we would get a C. This forced us to decide to use the cardboard PLAIN as our final project. The plane glided fairly well and was big enough to support the extra weight of the pico and batteries. Matthias worked on a motor mount for the new PLAIN, he got the diameter of the wooden rod we were putting it on, and then Matthias measured the dimensions of the motor and made a design(seen below) that would be able to connect the motor to the mount, Matthias added a fillet going out toward the PLAIN in order to give the motor mount more stability. Vinnie focused on cutting out a hole for the pico and battery on the main wings in order to keep the center of mass in the same spot it was before the extra hardware was added. Once the motor mount was printed we found out that the holes were a little too close together, so we used the drill to make the holes bigger and then used bolts with a small radius at an angle to get away with the holes still not being perfectly lined up. We then test launched a couple of times, the first being very succesful until the motor stalled. The second one was thrown with a downward angle and went straight into the ground and broke the propeller. The data collection was succesful, however Vinnie forgot to copy all the data before switching the device back to write mode so it was lost. It was evaluated that the motor stalling was a voltage issue because the battery we had was rated 3-4 volts beneath the recommended battery voltage for our specific motor. Afton agreed to lend us an extra battery of his that met the recomended minimum voltage.   

#### Images
![cardboardplane](images/cardboardplane.jpg)
![tail](images/tail.jpg)
![propeller](images/propeller.jpg)
![oldcardboardsealed](images/oldcardboardsealed.jpg)
![oldcockpit](images/oldcockpit.jpg)
![brokenprop](images/brokenprop.jpg)
![flight](images/flight1.gif)
![Motormount](images/Motormount.png)

### Week 24
#### Reflection

This week we worked on catching up on the documentation and then rearranged the cockpit in order to fit the new battery. On thrusday we went outside to launch and the PLAIN did fairly well, clearly producing lift, until it banked to the left and crashed. The reason for the bank was the battery was placed a little too far to the left and because it is the heaviest component attached, it dragged the whole thing to the left. The motor was spinning much faster with the new battery and didn't have the error where the throttle decreased on its own. It might've been better to start at 75% power and then increase as needed through the flight because we also changed the angle of attack by angling the motor up a little bit. The PLAIN completely destroyed itself upon landing and became unusable for a second flight. The data collection was succesful and shows the acceleration during the flight. However in order to create a smoother graph for a shorter flight, the rate at which the data was collected could have been speed up a good bit. It is also frustrating that the PLAIN can't be tested twice in the same period because of the way it breaks. This could have been changed by throwing it at a different angle, and then not throwing it off the biggest hill for the first test of the day (test flight 3). The pico and electronics still functioned after the crash and only the dowells and prop were damaged. In the graph you can see the spike of acceleration during the crash and it experienced a little over 2 Gs, and then ended up upside down because the Z acceleration at rest switched (-9.8 to 9.8). You can also see Vinnie forgot to kill the motor throttle before the crash and did it a couple seconds after.  

#### Images
![newcockpit](images/newcockpit.jpg)
![sealedinsides](images/sealedinsides.jpg)
![data](images/datagraphs.png)
![crash](images/planecrash.jpg)
![aftermath](images/floppyplain.jpg)
![flight3](images/flight3.gif)


## Tying_it_all_together
### Setbacks
#### General

From the start of this project, we had very lofty ambitions. The inital idea that we would work with Afton and Matthew and have our planes launch together and split midair didn't come to fruition because both teams were too far behind at the point where we needed to work together. The final functionality of the project was also limited when we chose to create a plane out of PLA and didn't consider the required weight-wingspan-trust ratio to produce lift. Throughout the project we spent too much time socailizing amongst our isle-mates and would routinely fall behind on our weekly goals. At the beginning this was ok because we would just make up most of it, but it eventually all added up and we realized our planning schedule would not be met. There were also minor impacts that took away some time such as sugeries, trips, and AP tests, but these were not the main cause of falling as far behind as we did. The project became more salvagable when we gave up on linking with Afton's group for takeoff. It also wouldn't have been feasible even if we had more time because the fundemental designs of the two planes are different, making the areodynamics complicated and off-balance due to the different weights. The true realization that we would need to switch to the cardboard plane was when everything was fully printed. It was really heavy and we didn't think the flaps all the way through which meant, knowing that we needed a succesful flight, there was no upside to sticking with the printed plane shell. After switching there were a few minor setbacks such as the first battery not being able to supply the correct ammount of voltage, which resulted in the motor losing RPMs in an unpredictable manner. Another setback was that the prop was highly susceptible to breaking, giving us a limited amount of test flights. This then led to the final hurrah of the PLAIN where we threw it off the top of the big hill which, despite acheiving lift and recording data as expected, banked to the left because of the weight distribution. If the prop hadn't have been so easily broken we would have thrown it on the flat ground, ensuring survival of the frame, and then observed that it banked left. Then we would have moved the insides around until it flew straight and then we could be comfortable in sending it off the big hill. One final setback was that Vinnie forgot to store the data off of the pico onto his computer after the first 2 test flights. This sucked because the code was written to reset the spreadsheet after every power cycle of the pico, meaning the data collected from the succesful first flight could not be evaluated. 

#### CAD

The CAD was flawed from the start when there was not enough time brainstorming a functional design and a lot of time was wasted on half finished designs that were half thought through. Unfortunatly, neither of us had come up with an idea that we had could either agree upon or something that we believed was going to work, because of this big oversight, our project was difficult to complete. This all came down to communcation, neither one of us communicted to each other about what the CAD design should look like, or what we wanted from the CAD, this led to the overall error and multiple designs. At certian points, the CAD would not be up to one of our standards of what we A: thought a conventional plane could look like, and B: believed would actually fly. This descrepincy in ideas led Matthias to make over 3 itterations on the CAD, fianlly settling on our final design. We also learned at the end of the project that realistically, no plane with the constraints we had such as using PLA and a 440mm max wingspan would be able to fly or achieve any sort of thrust. Overall, both of us learned valuable things about time-management and communication that will help us improve as engineers and students.

#### Code

The code/hardware part took longer than it should have because in addition to fraternizing with teams outside his own, Vinnie didn't make a clear plan for all the exact parts he needed and ended up stagering his orders (and made the mistake of ordering from ali-express) which created a couple weeks where he couldn't move on to the next stage of the project. Vinnie also got hung up on some voltage issues and wasted time trying to make a voltage divider that allowed him to only use one battery, which wasn't necessary because he needed an extra battery to run the motor anyways. A second setback was spending time on the servo code just to remove the flaps from the project all together when we switched to the cardboard plane. There weren't too many setbacks during when he was making the custom circuit board but when it was all done it barely wouldn't run because there were too many outputs drawing current directly from the battery. This was a quick fix and was solved by putting the RC reciever power through the pico instead of drawing it straight from the battery. 

### Successes
#### General

The final PLAIN produced a lot of lift and was clearly capable of a longer flight if the weight was distributed evenly. The PLAIN also collected data during the flight and could be controlled from a good distance with the remote controler. We completed our proof of concepts individually which helped as the project developed. We also learned a lot of things individually which improved our skills as engineers and will help us with our capstone projects. We improved communication a lot which helped with morale and showed a wanting to succede. There were many small wins along the way such as getting the RC working and creating a working airfoil in CAD that each improved our skills and inspired us to finish the project. We grew together, not apart which might have been what of the biggest successes along with being able to say we had a succesful flight in the end.    

#### CAD

While in the end, we used a non-CAD design, the things that Matthias learned in CAD will be helpful in the future. He learned about using planes in order to mold the design into what he intended, He used the loft tool in all the designs in order to create the back fusalage and it was something that he learned how to use this year and that made CAD design a lot easier. By the end of the project we needed a motor mount quickly, and in less than 20 minutes, Matthias was able to take the dimensions of the motor and the pole and create a motor mount that would be sutable and strong for the PLAIN. This was crucial to the process because we were running out of time and needed to get our plane in the air for a test run. This also was a culmination of knowledge and practice throughout the year, at the beginning of the year there was no chance Matthias was doing that as fast as he did, but by the end after plenty of practice this task felt like a breeze. Link to CAD [Here](https://cvilleschools.onshape.com/documents/3238cdf8a1991a2a3ab7aaf8/w/c31861085483687205792ad4/e/04aacecd12e49e444d40facb?renderMode=0&uiState=665a4a9a3dfa484453cba158) 


#### Code

In general, Vinnie's part of project went smoothly and he put a lot of work into it (especially during the last 4 weeks). He created a succesful prototype with a DC motor he found in the lab before the offical brushless motor arrived from China. He got the RC kit working within the same week it arrived and was able to control servos in no time. After getting a line of the formatting code from Afton who was using the same motor, he was able to control the brushless motor's throttle and even included a kill switch. He used his code for data collection from earlier in the year and was able to recording accurate acceleration values. He then mapped a button on the remote control to start collecting data and a second button to stop collecting data. This was an addition that made his life so much easier and one that many other groups wished they had. The creation of the custom circuit board went smoothly and he was very dedicated to finishing it as soon as possible, working on it during both second period and sixth period every day for a couple weeks. In the end he got his part of the project fully done to the standards of what was planned in the start minus the linkage. He got two servos (meant for the flaps) and a brushless motor (for the prop) to be controlled by a remote controller that could also start and stop accurate data collection. The final code is linked [here](raspberry-pi/finalplain.py). Finished circuit diagram:
![circuitdiagram](images/circuitdiagramplain.png)
