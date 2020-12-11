def get_file_lines(filename):
  for lines in filename:
    print (lines)

lines_list = ["Can we pretend that airplanes n the night sky are like shootin stars I could really use a wish right now, wish right now, wish right now Can we pretend that airplanes n the night sky are like shootin' stars I could really use a wish right now, wish right now, wish right now","Yeah, yeah I could use a dream or a genie or a wish To go back to a place much simpler than this Cause after all the partying and smashing and crashing And all the glitz and glam and the fashion","And all the pandemonium and all the madness There comes a time when you fade to the blackness And when you're staring at the phone in your lap And you hoping but them people never call you back","But that's just how the story unfolds You get another hand soon after you fold And when your plans unravel in the sand What would you wish for, if you had one chance?","So airplane airplane sorry I'm late I'm on my way so don't close that gate If I don't make that then I'll switch my flight and I'll be right back at it by the end of the night","Can we pretend that airplanes in the night sky are like shootin' stars I could really use a wish right now, wish right now, wish right now Can we pretend that airplanes in the night sky are like shootin' stars I could really use a wish right now, wish right now, wish right now","Yeah yeah somebody take me back to the days Before this was a job before I got paid Before it ever mattered what I had in my bank Yeah back when I was trying to get a tip at subway","And back then I was rapping for the hell of it But nowadays we rapping to stay relevant I'm guessing if can make some wishes out of airplanes Then maybe oh maybe I'll go back to the days","Before the politics that we call the rap game And back when ain't nobody listened to my mix tape And back before when I tried to cover up my slang But this is for the Decatur what's up Bobby Ray","So can I get a wish to end the politics And get back to the music that started this shit So here I stand and then again I say I'm hoping we can make some wishes outta airplanes","Can we pretend that airplanes in the night sky are like shootin' stars I could really use a wish right now, wish right now, wish right now Can we pretend that airplanes in the night sky are like shootin' stars I could really use a wish right now, wish right now, wish right now", "I could really use a wish right now I, I, I could really use a wish right now Like, like, like shootin' stars I, I, I could really use a wish right now a wish a wish right now"]
for index, lines in enumerate(lines_list, start=1):
       print(index,lines)

def lines_printed_backwards(lines_list):
   for index in reversed(range(len(lines_list))):
      yield index, lines_list[index]
for index, lines in lines_printed_backwards(lines_list):
   print(index,lines)
   
import random

def lines_printed_random(lines_list):
   for index in random.sample(range(len(lines_list)), len(lines_list)):
       yield index, lines_list[index]
for index, lines in lines_printed_random(lines_list):
   print(index,lines)
   
from random import choice


def lines_printed_custom(user_response):

  
  bot_response_yes = ["Yeah, yeah I could use a dream or a genie or a wish To go back to a place much simpler than this Cause after all the partying and smashing and crashing And all the glitz and glam and the fashion And all the pandemonium and all the madness There comes a time when you fade to the blackness And when you're staring at the phone in your lap And you hoping but them people never call you back...SHOULD I KEEP GOING", "But that's just how the story unfolds You get another hand soon after you fold And when your plans unravel in the sand What would you wish for, if you had one chance? So airplane airplane sorry I'm late I'm on my way so don't close that gate If I don't make that then I'll switch my flight and I'll be right back at it by the end of the night...SHOULD I KEEP GOING", "Can we pretend that airplanes in the night sky are like shootin' stars I could really use a wish right now, wish right now, wish right now Can we pretend that airplanes in the night sky are like shootin' stars I could really use a wish right now, wish right now, wish right now Yeah yeah somebody take me back to the days Before this was a job before I got paid Before it ever mattered what I had in my bank Yeah back when I was trying to get a tip at subway...SHOULD I KEEP GOING", "And back then I was rapping for the hell of it But nowadays we rapping to stay relevant I'm guessing if can make some wishes out of airplanes Then maybe oh maybe I'll go back to the days Before the politics that we call the rap game And back when ain't nobody listened to my mix tape And back before when I tried to cover up my slang But this is for the Decatur what's up Bobby Ray So can I get a wish to end the politics And get back to the music that started this shit So here I stand and then again I say I'm hoping we can make some wishes outta airplanes...SHOULD I KEEP GOING"," So can I get a wish to end the politics And get back to the music that started this shit So here I stand and then again I say I'm hoping we can make some wishes outta airplanes Before the politics that we call the rap game And back when ain't nobody listened to my mix tape And back before when I tried to cover up my slang But this is for the Decatur what's up Bobby Ray...SHOULD I KEEP GOING","7 And back then I was rapping for the hell of it But nowadays we rapping to stay relevant I'm guessing if can make some wishes out of airplanes Then maybe oh maybe I'll go back to the days Yeah yeah somebody take me back to the days Before this was a job before I got paid Before it ever mattered what I had in my bank Yeah back when I was trying to get a tip at subway...SHOULD I KEEP GOING","So airplane airplane sorry I'm late I'm on my way so don't close that gate If I don't make that then I'll switch my flight and I'll be right back at it by the end of the night But that's just how the story unfolds You get another hand soon after you fold And when your plans unravel in the sand What would you wish for, if you had one chance?...SHOULD I KEEP GOING","And all the pandemonium and all the madness There comes a time when you fade to the blackness And when you're staring at the phone in your lap And you hoping but them people never call you back Yeah, yeah I could use a dream or a genie or a wish To go back to a place much simpler than this Cause after all the partying and smashing and crashing And all the glitz and glam and the fashion...SHOULD I KEEP GOING"]
  bot_response_no = ["PLEASE PLEASE PLEASE Can we pretend that airplanes in the night sky are like shootin' stars I could really use a wish right now, wish right now, wish right now Can we pretend that airplanes in the night sky are like shootin' stars I could really use a wish right now, wish right now, wish right now?", " I THINK YOU MISUNDERSTOOD WHAT I WAS ASKING....I SAID....Can we pretend that airplanes in the night sky are like shootin' stars I could really use a wish right now, wish right now, wish right now Can we pretend that airplanes in the night sky are like shootin' stars I could really use a wish right now, wish right now, wish right now", "YOU ARE SERIOUSLY RUINING MY VIBE. COME ON....Can we pretend that airplanes n the night sky are like shootin stars I could really use a wish right now, wish right now, wish right now Can we pretend that airplanes n the night sky are like shootin' stars I could really use a wish right now, wish right now, wish right now", "Has anyone ever told you, you are a dream killer", "You are a horrible friend, I'm done here. Bye. FOR-EVE-R " ]

  if user_response ==  "yes":
    return choice(bot_response_yes)
  elif user_response == "no" :
    return choice(bot_response_no)
  else:
    return " You're a terrible listener...should we pretend airplanes are shooting stars?"




print(" I could use a wish right now....")
print(" Can We Pretend That Airplanes In The Night Sky Are Like Shooting Stars???")

user_response = ""

while True:
  user_response = input(" yes or no???: ")
  

  if user_response == 'done':
    break

  
  bot_response = lines_printed_custom(user_response)
  print(bot_response)
