const fs = require('node:fs')

function getfilelines(filename) {
    try {
        const data = fs.readFileSync(filename, 'utf8')
        return data.trim().split('\n')
    } catch (err) {
        console.log(err)
    }
}

const num = 3014387
const elves = []
for (let i = 0; i < num; i++) {
    elves.push(i)
}
let elf = -1
let done = false
while (elves.length > 1) {
    elf++
    if (elf == num) elf = 0
    const elfI = elves.indexOf(elf)
    if (elfI == -1) continue
    const nextI = (elfI + Math.floor(elves.length/2)) % elves.length
    // console.log(elves, elfI, nextI)
    elves.splice(nextI, 1)
}
console.log(elves[0]+1)
