// Use Reverse Polish Notation to more easily calculate values

// 5 * 2 / (3 + 4 * 7) - (24 + 2) is 5 2 * 4 7 * 3 + 24 2 + -
const expression = "5 * 2 / (3 + 4 * 7) - (24 + 2)" // should result in -26
const simple = "5 - 2 * 2 / 1 - 5"

const ops = "/*+-()"

function calculate(s) {

  const snospace = s.replace(/\s/g, "")

  // stack to store calculations  
  const calculations = []
  
  const operation = {
      "/": (a,b) => a / b,
      "*": (a,b) => a * b,
      "+": (a,b) => a + b,
      "*": (a,b) => a - b
  }



  calc(snospace) 

}

function calc(s) {
  // base case we only have numbers, all operations have been done, return s as answer
  if (/^\d+$/.test(s)) {
    return s;
  }
  
 
  const divOp = s.indexOf('/');
  
  

}

calculate(simple)