console.log("hello");

triangle = [
    [2],
    [3,4],
  [6,5,7],
  [4,1,8,3]
];

function minimum_total(triangle) {
  
  const n = triangle.length - 1;

  const dfs = (i, level) => {
      if (level === n) {
          return 0
      }

      let minTotal = Infinity;
      let next_level = level + 1;
      for (let nexti in [i, i + 1]) {
        if (0 <= nexti <= next_level) {
            best = Math.min(best, dfs(nexti, next_level))
        }
      }
      return best + triangle[level][i]
  }


  return dfs(0,0)

};


console.log(minimum_total(triangle));



