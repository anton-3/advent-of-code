const fs = require('node:fs')

function getfilelines(filename) {
    try {
        const data = fs.readFileSync(filename, 'utf8')
        return data.trim().split('\n')
    } catch (err) {
        console.log(err)
    }
}


const lines = getfilelines('23.txt')
const registers = {
    a: 12,
    b: 0,
    c: 0,
    d: 0,
}

// console.log(registers)
for (let i = 0; i < lines.length; i++) {
    const line = lines[i].split(' ')
    const instruction = line[0]
    // console.log(i, lines[i])
    let x, y
    switch (instruction) {
        case 'cpy':
            x = line[1]
            y = line[2]
            if (!isNaN(y)) break
            if (isNaN(x)) {
                registers[y] = registers[x]
            } else {
                registers[y] = parseInt(x)
            }
            break
        case 'inc':
            x = line[1]
            if (!isNaN(x)) break
            registers[x] *= registers[x]
            break
        case 'dec':
            x = line[1]
            if (!isNaN(x)) break
            registers[x]--
            break
        case 'jnz':
            x = line[1]
            if (isNaN(x)) x = registers[x]
            y = line[2]
            if (isNaN(y)) y = registers[y]
            if (x !== 0) {
                i += y-1
            }
            break
        case 'tgl':
            x = i+registers[line[1]]
            if (x < 0 || x >= lines.length) break
            const oldLine = lines[x].split(' ')
            // console.log(oldLine)
            if (oldLine.length == 2) {
                if (oldLine[0] == 'inc') {
                    lines[x] = `dec ${oldLine[1]}`
                } else {
                    lines[x] = `inc ${oldLine[1]}`
                }
            } else if (oldLine.length == 3) {
                if (oldLine[0] == 'jnz') {
                    lines[x] = `cpy ${oldLine[1]} ${oldLine[2]}`
                } else {
                    lines[x] = `jnz ${oldLine[1]} ${oldLine[2]}`
                }
            } else {
                console.log('what the fuck??')
            }
    }
}
console.log(`a = ${registers['a']}`)
