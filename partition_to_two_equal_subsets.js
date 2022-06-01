function twoEqualSubSets(nums) {
  const target = Math.floor((nums.reduce((a,b) => a + b) / 2))
  console.log(target);
}

twoEqualSubSets([1,1,2])
