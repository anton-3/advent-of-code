const fs = require('node:fs')

function getfilelines(filename) {
    try {
        const data = fs.readFileSync(filename, 'utf8')
        return data.trim().split('\n')
    } catch (err) {
        console.log(err)
    }
}

const num = 5
const elves = new Set()
for (let i = 0; i < num; i++) {
    elves.add(i+1)
}
// const elves = []
// for (let i = 0; i < num; i++) {
//     elves.push(i)
// }
let elf = 0
let opp = Math.floor(num/2)
while (elves.size > 1) {
    elf++
    opp++
    if (elf > num) elf = 1
    else if (opp > num) opp = 1
    while (!elves.has(opp)) opp--
    console.log(elves, elf, opp)
    elves.delete(opp)
    opp++
}
console.log(Array.from(elves)[0])
