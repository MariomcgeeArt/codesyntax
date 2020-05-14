

//This is the code unfixed and me following only what i knew using no documentaion or  help to fix the convention errors
//the code does not currently run 


//syntax corrected looking at js syntax documentation 
function FizzBuzz(target) {
    for (let i = 1; i <= target; i += 1) {
      if (i % 3 === 0 && i % 5 === 0) {
        console.log('FizzBuzz');
      } else if (i % 3 === 0) {
        console.log('Fizz');
      } else if (i % 5 === 0) {
        console.log('Buzz');
      } else {
        console.log(i);
      }
    }
  }
  
  FizzBuzz(15);