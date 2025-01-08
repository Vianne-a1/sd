


// Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon 
// SoftDev pd0
// K28 -- Getting more comfortable with the dev console and the DOM
// 2025-01-07t
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) 
{
    var j=30;
    return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
              return x+30;
          }
        };

//create a new node in the tree
var addItem = function(text)
{
    var list = document.getElementById("thelist");
    var newitem = document.createElement("li");
    newitem.innerHTML = text;
    list.appendChild(newitem);
};

//prune a node from the tree
var removeItem = function(n)
{
    var listitems = document.getElementsByTagName('li');
    listitems[n].remove();
};

//color selected elements red
var red = function()
{
    var items = document.getElementsByTagName("li");
    for(var i = 0; i < items.length; i++) {
	items[i].classList.add('red');
    }
};

//color a collection in alternating colors
var stripe = function()
{
    var items = document.getElementsByTagName("li");
    for(var i = 0; i < items.length; i++) {
	if (i%2==0) {
	    items[i].classList.add('red');
	} else {
	    items[i].classList.add('blue');
	}
    }
};


//insert your implementations here for...
// FIB
// FAC
// GCD

// Factorial function (recursive implementation)
function fact(n) {
  if (n == 0) return 1;   // Base case: 0! = 1
  return n * fact(n - 1); // Recursive step: n * (n-1)!
}
// TEST CALLS
fact(1);  // Expected output: 1
fact(5);  // Expected output: 120
fact(10); // Expected output: 3628800

// Fibonacci function (recursive implementation)
function fib(n) {
  if (n == 0) return 0;   // Base case: fib(0) = 0
  if (n == 1) return 1;   // Base case: fib(1) = 1
  return fib(n - 1) + fib(n - 2); // Recursive step: fib(n) = fib(n-1) + fib(n-2)
}
// TEST CALLS
fib(0);  // Expected output: 0
fib(5);  // Expected output: 5
fib(10); // Expected output: 55

// Greatest Common Divisor function (iterative implementation)
const gcd = (a, b) => {
  while (b !== 0) {  // Continue until b becomes 0
      let temp = b;  // Temporarily store b
      b = a % b;     // Update b to the remainder of a divided by b
      a = temp;      // Update a to the old value of b
  }
  return a;          // Return the greatest common divisor
};
// TEST CALLS
gcd(48, 18); // Expected output: 6
gcd(100, 25); // Expected output: 25
gcd(7, 13);  // Expected output: 1 (prime numbers)

// Example of using arrow function syntax
const myFxn = (param1, param2) => {
  return param1 + param2; // Example: returns the sum of the two parameters
};
// TEST CALLS
myFxn(5, 10); // Expected output: 15