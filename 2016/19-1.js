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
const elves = {}
for (let i = 0; i < num; i++) {
    elves[i] = true
}
let elf = -1
let done = false
while (!done) {
    elf++
    if (elf == num) elf = 0
    if (elves[elf]) {
        let next = (elf + Math.floor(num/2)) % num
        while (!elves[next]) {
            next = (next+1) % num
            if (next == elf) {
                done = true
                console.log(elf+1)
                break
            }
        }
        elves[next] = false
    }
}
