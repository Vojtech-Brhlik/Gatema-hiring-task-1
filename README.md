
## Input file
The input file gives instructions to various drills. The drills then do given actions based on these instructions. Instructions are defined the following way:

    X<x.coords>Y<y.coords>T<drill.num>
Where ***x.coords*** and ***y.coords*** are the coordinates for drilling and ***drill.num*** specifies the drill that should do the task for this line and the following lines. If the following lines are done using the same drill, the inscrution just consists of the X and Y part (without the `T<drill.num>`).
The instruction set begins with:

    (M47, Zacatek bloku vrtani)
and ends with:

    (M47, Konec bloku vrtani)

There are other various lines in the input file, but they are irrelevant to the solution of this task, so we will ignore them.
## Parameters

 **"-funkce1"**
When ran with this parameter, the script looks through the given file and does two things:

 - It looks through the instructions and whenever the X coordinate is higher than 50, incereases the Y coordinate by 10
 - It orders the instruction sets based on the drill number
 
 **"-funkce2"**
When ran with this parameter, the script simply reads all the instruction and prints the highest and lowest values for X and Y  coordinates. 
