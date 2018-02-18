# Create Scenes with lights and music with Alexa from a Raspberry Pi



## Apart from the code here a few other things are needed.

1. A server running https which can host this server, because Alexa only speaks HTTPS. 
2. A Amazon Developer Accocunt, you need to create some Alexa intents to connect to 
   The Scenes created in the scenes/scenes.py file, the intent name has to be the 
   same as the scene name. (And ofc a Alexa skill which you can host locally on your own alexa)
3. Alexa needs music links to be able to play it back, you can find mp3 files online of your favorite
   songs, or come up with another way to provide links to music for alexa. 


## A few remarks. 

The Scenes contains 4 fields, all of them are optional.. but leaving them empty creates quite the 
pointless scene.
1. The name of the scene, it has to match the intent Alexa sends.
2. The Message Alexa will read before starting your scene
3. A list of music links, Alexa will play one at random.
4. A function which controlls your lamps.

I've made it easy, i hope, to create functions that controll the lamps.
The pre_process.py file and lamps.py file in scenes will create a HOUSE object 
containing all the lamps with a bunch of helper functions to set different 
attributes such as color, blinking, turning them of and on and some effects.
(This is for the philips hue lamps). You can go look in the lamp_functions.py 
file for example of how a function might look. 


The reason for the bash script is: 

For some reason when i've left the server running for prolonged  amounts of time (Days)
it just stopped responding, it dies. I'm guessing it has something to do with the way 
i handle calling the lamp function, it has to be called in a new process so not to block
the rest of the program and i'm perhaps not handling that in a good manner. But instead of doing it properly i just let the bashscript restart the server whenever it dies. 


Regarding the music. I'd love to be able to play spotify instead of having to hunt for
links online containing the music i want, buut i couldn't get it working with spotify if anyone has any idé how i can go about making it work, please do tell! 

