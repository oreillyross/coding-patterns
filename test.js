
const grid = [[1,0,-1,1,0,1],
              [1,-1,1,-1,1,-1],
	      [0,0,-1,-1,1,1]]

function plumber(grid) {
  

	let count = 0;
	const visited = new Set();

	for(let i = 0; i < grid[0].length; i++) {
	  if (explore(grid, 0, i)) count += 1;	
	}

	function explore(grid, r,c, visited)  {
            
	    const rowInbounds = 0 <= r && r < grid.length;
	    const colInbounds = 0 <= c && c < grid[0].length;
	    if (!rowInbounds || !colInbounds) return false;
		
	    if (grid[r][c] === -1) return false;
	    
	    const pos = `${r},${c}`;
	    if (visited.has(pos)) return false;
	    visited.add(pos);
	    
	    explore(grid, r + 1, c);
	    explore(grid, r, c - 1);
	    explore(grid, r, c + 1);
	    
	    if (grid[r][c] === 1) {
		    count += 1;
		    return true;
	    }

	}

}

console.log(plumber(grid));  // should be 5