# Scanlendar


## Description

Calendar PWA that uses NLP to let you type in a event, scan a paragraph or paper containing an event with OCE, or share plain text, and it will infer the calendar event and give you a Link to add it to your calendar.

## Demo _Coming Soon_


## What problem does Scanlendar solve?
### Case Study
Consider the following situation:

+ The date is Monday Jan 10, 2030
+ You're in a call with a friend and he tells you the date of an upcoming event that you must attend, and then he hangs up.
+ You quickly write down the event in your notes app on your smartphone to not forget.
+ You wrote a note in your notes app that contained the following
  + > 2 hour meeting with John about virtual teaching and e-learning on Zoom a week from today at noon

___
Transferring this plain text event in casual language to the calendar app on your phone should be mindless and easy
  + __Issue__: _yet it isn't, because it would require continuously switching between two apps and typing in details in multiple text boxes._
  +
This is what out app would do with the text in the note containing the event:

| Place in Text                   | Event Details                                            |
| ------------------------------- | -------------------------------------------------------- |
| Meeting with John               | __Title__: Meeting with John                             |
| virtual teaching and e-learning | __Description__: E-learning and virtual teaching on Zoom |
| a week from today               | __Start Date__: Monday Jan 17, 2030                      |
| N/A                             | __End Date__: Monday Jan 17, 2030                        |
| at noon                         | __Start Time__: 12:00pm                                  |
| 2 hour                          | __End Time__: 2:00pm                                     |

Try it!

<style>.addToCalendar {background-color:#44c76700; transition: all 0.3s ease-in-out;border-radius:8px;border:1px solid #18ab29;display:inline-block;cursor:pointer;color:lightgrey;font-family:Arial;font-size:16px;padding:10px 15px;text-decoration:none;text-shadow:0px 1px 0px #2f6627;}.addToCalendar:hover {background-color:#5cbf2a85; text-decoration: none; color: white;}.addToCalendar:active {position:relative;top:1px;}</style><a href="https://calendar.google.com/calendar/render?action=TEMPLATE&dates=20300118T050000Z%2F20300117T180000Z&details=E-learning%20and%20virtual%20teaching%20on%20Zoom&text=Meeting%20with%20John" class="addToCalendar">Add to Calendar</a>


### Authors
Eric Zhu, April, Samhith-Kakara, Yonah Aviv

Copyright (C) 2021  Scanlendar
