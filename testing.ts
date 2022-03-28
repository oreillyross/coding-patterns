const unsortedArr = [31, 27, 28, 42, 13, 8, 11, 30, 17, 41, 15, 43, 1, 36, 9, 16, 20, 35, 48, 37, 7, 26, 34, 21, 22, 6, 29, 32, 49, 10, 12, 19, 24, 38, 5, 14, 44, 40, 3, 50, 46, 25, 18, 33, 47, 4, 45, 39, 23, 2];

function merge<T>(s: T[] ) {
  // base case for recursive function. i.e. if it is one item in array, array is sorted.
  if (s.length <= 1) {
    return s;
  }
  // divide and conquer, split array in half
  const mid = Math.floor(s.length /2);
  const left = s.slice(0, mid);
  const right = s.slice(mid);
  // recursive case, keep calling merge function until sub-arrays are split over and over
  const left_sorted: any = merge(left);
  const right_sorted: any = merge(right);
  // perform the sorting step using the utility function which merges two sorted arrays. This returns many of the sub arrays sorted
  return _mergeSortedArrays(left_sorted, right_sorted);

}

function _mergeSortedArrays<T>(a: T[], b: T[]) {
    
    const sorted = [];
    // keep finding the smallest element between the two sorted arrays. The shift operation removes the first element, thus making array
    // smaller and adhering to while loop condition
    while (a.length && b.length) {
      sorted.push(a[0] <= b[0] ? a.shift() : b.shift() );
    };

    // this is a short-cut, using ES2106 syntax, it spreads the sorted array, and concatenates the remaining two arrays. Because
    // the condition above in the while loops guarantees only one array could still cnotain values, we can safely spread both arrays
    // which will either append all remaining from one of the arrays and append an empty array which has no effect.
    return [...sorted, ...a, ...b];
};

console.log(merge(unsortedArr))