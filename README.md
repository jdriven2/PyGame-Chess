# PyGame-Chess
This is my attempt at making chess with pygame without GPT help, and no tutorials specific to chess.

# Overview:
I started this project on 2/7/24, and have made enough progress to upload it here on 2/9/24.

This is my first unguided coded project of siginifcant size, and since I work on it with my personal and work laptop, I figure github is a good idea.

However, I have never used Github before, despite hearing about a bunch of benefits it provides, I have tried to keep the introduction of more things that I have to learn to a minimum. It turns out emailing myself python files back and forth has gotten to clumsy though, and I am starting to make mistakes in my outline that I dont realize until I am pretty far in, so some sort of branch for different outlines would be super helpful.

# What I have so far:
Basically, I can draw a "board" in pygame. This is accomplished by creating a class called "square", using a function called "drawRow()" to make a row of squares, and then a function called "drawBoard()" to make a stack of rows.

The "drawBoard()" function contains a loop of "drawRow()" functions, and the Square Class contains a method called "draw()". Paramters like where I want the board to be passed, the size of the board, and the number of squares and their color are all passed to the "drawBaord()" function, which gives them to each following function, and ensures everything is correct relative to the first drawn Square.

It works well enough, but since I am new to OOP, once concern I have is that the "Board" and "Rows" should be their own classes, with draw methods themselves. It's something I tried, and then realized meant a lot of big changes, which scared me so I created two versions of my code before and after the change (starting to see why Github makes sense). We will see where that ends up.

Additionally, I have been playing around in parralel with code that is repsonsible for moving a PNG in pygame on a screen. I have got it to move the PNG by essentially attatching it to a rectangle and moving the rectangle, then drawing it on the rectangle every frame. But it currently does not snap to a grid like I would want.

My thoughts on how to do this are:
1: a function that takes in the piece I am holding, and is triggered on the event of the mouseUP, that iterates though the squares and returns the closest square, then takes the piece and teh squares X Y position, and sets the pieces XY to be the squares.
  - requires that the Square and Piece have X Y attributes.
  - requires a way for me to loop through the squares (currently kind of hard because the sqaures are drawn but i dont think that they are stored in like an array or anything, and I am not really sure how to access a specific square or something in the array if I appended them anyway, but I do think regardless of the solution creating the array will at somepoint be required)
  - requires me to "store" the piece ive clicked on somewhere, probably as some sort of global variable.
  - requires some sort of code to tell which piece needs to animate the moving
  - could be slow
  - could be harder
2: make the squares "clickable" and then write a function that takes a piece and a square and gets that info from the last piece and square I have clicked on, and is triggered when a square is clicked.
  - requires squares be clickable
  - requires that the Square and Piece have X Y attributes.
  - requires me to "store" the piece ive clicked on somewhere, probably as some sort of global variable.
  - requires me to "store" the square ive clicked on somewhere, probably as some sort of global variable.
  - might be faster?
  - might be easier?
  - isnt as cool
  - doesnt build the array that will later be useful

okay thats it for now!

