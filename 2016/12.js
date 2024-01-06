const fs = require('node:fs')

function getfilelines(filename) {
    try {
        const data = fs.readFileSync(filename, 'utf8')
        return data.trim().split('\n')
    } catch (err) {
        console.log(err)
    }
}


function part1() {
    const lines = getfilelines('12.txt')
    const registers = {
        a: 0,
        b: 0,
        c: 1,
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
                if (isNaN(x)) {
                    registers[y] = registers[x]
                } else {
                    registers[y] = parseInt(x)
                }
                break
            case 'inc':
                x = line[1]
                registers[x]++
                break
            case 'dec':
                x = line[1]
                registers[x]--
                break
            case 'jnz':
                x = line[1]
                y = parseInt(line[2])
                if (registers[x] !== 0) {
                    i += y-1
                }
                break
        }
        // console.log(registers)
    }
    console.log(`a = ${registers['a']}`)
}

part1()

