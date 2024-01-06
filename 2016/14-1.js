const fs = require('node:fs')
const crypto = require('crypto')

function getfilelines(filename) {
    try {
        const data = fs.readFileSync(filename, 'utf8')
        return data.trim().split('\n')
    } catch (err) {
        console.log(err)
    }
}
function md5(string) {
    return crypto.createHash('md5').update(string).digest('hex')
}

const salt = 'ihaygndm'
const hashes = []
const max = 25000
for (let i = 0; i < max; i++) {
    hashes.push(md5(salt+i))
}

const triples = {}
const fives = {}
for (let j = 0; j < max; j++) {
    const hash = hashes[j]
    for (let i = 0; i < hash.length - 2; i++) {
        if (hash[i] === hash[i+1] && hash[i+1] === hash[i+2]) {
            if (!(Object.hasOwn(triples, j))) triples[j] = hash[i]
            if (i < hash.length - 4 && hash[i+2] === hash[i+3] && hash[i+3] === hash[i+4]) {
                if (!(Object.hasOwn(fives, j))) fives[j] = hash[i]
            }
        }
    }
}

let keys = []
for (const i in triples) {
    for (const j in fives) {
        const a = parseInt(i)
        const b = parseInt(j)
        if (triples[i] == fives[j] && b > a && b - 1000 <= a) {
            keys.push(a)
            break
        }
    }
}

let sortedKeys = [...new Set(keys)]
sortedKeys.sort((a, b) => a - b)
console.log(sortedKeys)
console.log(sortedKeys[63])

// 137191 HIGH
// 11682 LOW
