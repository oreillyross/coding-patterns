
const input = [[5,4],[6,4],[6,7],[2,3], [1,1]];



function maxEnvelopes(envelopes) {
  const sorted = envelopes.sort((a,b) => {
      return a[0] - b[0];
  } )

  const max_layers = [];
  let max_len = 1;
  for (let i = 0; i < sorted.length; i++) {
      max_layers[i] = 1;
      for (let j = 0; j < i; j++) {
        if (envelopes[i][0] > envelopes[j][0] && envelopes[i][1] > envelopes[j][1]) {
            max_layers[i] = Math.max(max_layers[i], max_layers[j] + 1);
            
        }  
      }
      max_len = Math.max(max_len, max_layers[i]);
  }

  return max_len;

  

} 

console.log(maxEnvelopes(input))
