# Buffel-B-g
The mega corporation Buffel &amp; Båg AB has a custom built system for handling meetings which has been around since the beginning of time and which is now deemed too hard to use
--------------------------------------
The mega corporation Buffel & Båg AB has a custom built system for handling meetings which has been around
since the beginning of time and which is now deemed too hard to use. Since management doesn’t really know
how important the system is they have invested far too little resources in the upgrade project and have
decided to hire a single poor contractor (guess who) to solve the most important problems in almost no time.
As a first step, management has asked for an application that works independently of the existing system and
that can be called to get suggestions for suitable meeting times based on the following parameters:
 participants (employee ids), one or multiple
 desired meeting length (minutes)
 earliest and latest requested meeting date and time
 office hours (e.g. 08-17)
The application can be either an HTTP API or a console application.
At regular intervals all information is dumped from the existing system to a number of text files where the
freebusy.txt file contains details on when all employees are busy the next few weeks.
An excerpt from the file can look like this:
170378154979885419149243073079764064027;Colin Gomez
170378154979885419149243073079764064027;2/18/2014 10:30:00 AM;2/18/2014 11:00:00 AM;485D2AEB9DBE3...
139016136604805407078985976850150049467;Minnie Callahan
139016136604805407078985976850150049467;2/19/2014 10:30:00 AM;2/19/2014 1:00:00 PM;C165039FC08AB4...
As it seems, the file has lines in two different formats where the first one contains employee id and display
name and the second format has information on the time slots where the employee is busy and therefore not
available for meetings.
The following can be good to know:
 In the file, all times stated can be treated as local times – no need to adjust for timezone differences
 apparently it is quite common that people work every day of the week
 due to the crappy state of the existing system the file may contain some irregularities, these should
be ignored
 the system only handles meetings that start every whole and half hour, e.g. 08.00, 08.30, 09.00, etc.
Unfortunately, everyone who knew something about the old system have fled the company a long time ago.
Questions regarding how the new API/application should work can however be answered.
Always code as if the person who ends up maintaining
your code will be a violent psychopath who knows
where you live.
”
”
Your solution will be evaluated on aspects like:
• The structure and the quality of the code
• How easy it is to understand
• How you verify that the solution works (tests are encouraged)
Keep in mind that a perfect solution is not the primary goal of the assignment, but rather to see how you
interpret and work on the problem and the code you write.
Link to the file: https://builds.lundalogik.com/api/v1/builds/freebusy/versions/1.0.0/file
