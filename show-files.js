const fs = require('fs');
let arr=[];
fs.readdirSync("./posts/").sort().reverse()
    .forEach((i) => {
		if(i.substring(i.lastIndexOf('.'))==".md"){
			// console.log(i)
			arr.push(i)
		}
	})

fs.writeFileSync('links.json',JSON.stringify(arr))
// console.log(arr)

