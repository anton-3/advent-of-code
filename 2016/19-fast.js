const fs = require('node:fs')

function getfilelines(filename) {
    try {
        const data = fs.readFileSync(filename, 'utf8')
        return data.trim().split('\n')
    } catch (err) {
        console.log(err)
    }
}

let j = 1
const high = 3014387
for (let i = 4; i < high; i++) {
    if (i == j) {
        j = 1
    } else if (j * 2 < i) {
        j++
    } else {
        j += 2
    }
}
console.log(j)
