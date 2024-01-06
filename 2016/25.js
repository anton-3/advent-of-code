const fs = require('node:fs')

function getfilelines(filename) {
    try {
        const data = fs.readFileSync(filename, 'utf8')
        return data.trim().split('\n')
    } catch (err) {
        console.log(err)
    }
}


function part1(a) {
    let bit = 1
    const lines = getfilelines('25.txt')
    const registers = {
        a: a,
        b: 0,
        c: 0,
        d: 0,
    }
    // console.log(registers)
    for (let i = 0; i < lines.length; i++) {
        const line = lines[i].split(' ')
        const instruction = line[0]
        // console.log(i, lines[i])
        // console.log(`${i}: a = ${registers['a']}, b = ${registers['b']}, c = ${registers['c']}, d = ${registers['d']}, `)
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
                if (isNaN(x)) x = registers[x]
                x = parseInt(x)
                y = line[2]
                if (isNaN(y)) y = registers[y]
                y = parseInt(y)
                if (x !== 0) {
                    i += y-1
                }
                break
            case 'out':
                x = line[1]
                if (isNaN(x)) x = registers[x]
                x = parseInt(x)
                process.stdout.write(String(x))
                if (bit == x) {
                    console.log('\naborting...')
                    return
                }
                bit = x
                break
            case 'PRINT':
                console.log(`${line[1]}: a = ${registers['a']}, b = ${registers['b']}, c = ${registers['c']}, d = ${registers['d']}, `)
                break
        }
        // console.log(registers)
    }
    console.log(`a = ${registers['a']}, b = ${registers['b']}, c = ${registers['c']}, d = ${registers['d']}, `)
}

for (let i = 1; i < 999999999; i++) {
    console.log(`fuckery #${i}`)
    part1(i)
}

