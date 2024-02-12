const fs = require('fs');
let arr = [];
fs.readdirSync("./posts/").sort().reverse()
	.forEach((i) => {
		if (i.substring(i.lastIndexOf('.')) == ".md") {
			// console.log(i)
			arr.push(i)
		}
	})
// console.log(arr)
fs.writeFileSync('links.json',JSON.stringify(arr))