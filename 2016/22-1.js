const fs = require('node:fs')

function getfilelines(filename) {
    try {
        const data = fs.readFileSync(filename, 'utf8')
        return data.trim().split('\n')
    } catch (err) {
        console.log(err)
    }
}

function readints(string) {
    return string.match(/\d+|\D+/g).map(x => parseInt(x)).filter(x => !isNaN(x));
}

const lines = getfilelines('22.txt')
lines.shift()
lines.shift()

const used = []
const avail = []
for (let i = 0; i < 38; i++) {
    used.push(Array(28))
    avail.push(Array(28))
}
let i = 0
for (const line of lines) {
    const ints = readints(line)
    const x = ints[0]
    const y = ints[1]
    used[x][y] = ints[3]
    avail[x][y] = ints[4]
    i++
}

let count = 0
for (let i = 0; i < 38; i++) {
    for (let j = 0; j < 28; j++) {
        for (let k = 0; k < 38; k++) {
            for (let l = 0; l < 28; l++) {
                if (i == k && j == l) continue
                const aUsed = used[i][j]
                if (aUsed == 0) continue
                // const aAvail = avail[i][j]
                // const bUsed = used[k][l]
                const bAvail = avail[k][l]
                if (aUsed <= bAvail) count++
            }
        }
    }
}
console.log(count)

