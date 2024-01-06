const fs = require('node:fs/promises')

async function getfilelines(filename) {
    try {
        const data = await fs.readFile(filename, { encoding: 'utf8' })
        return data.trim().split('\n')
    } catch (err) {
        console.log(err)
    }
}

function printScreen(screen) {
    console.log()
    for (const row of screen) {
        for (const pixel of row) {
            process.stdout.write(pixel ? '#' : '.')
        }
        console.log()
    }
}

function createScreen() {
    const screen = []
    for (let i = 0; i < 6; i++) {
        screen.push(Array(50).fill(false))
    }
    return screen
}

function rotateArray(array, distance) {
    for (let i = 0; i < distance; i++) {
        array.unshift(array.pop())
    }
}

function countScreen(screen) {
    let count = 0
    for (const row of screen) {
        for (const pixel of row) {
            if (pixel) {
                count++
            }
        }
    }
    return count
}


const lines = await getfilelines('8.txt')
let screen = createScreen()
printScreen(screen)
for (const line of lines) {
    if (line.startsWith('rect')) {
        const rect = line.split(' ')[1].split('x').map(x => parseInt(x))
        console.log(rect)
        for (let i = 0; i < rect[1]; i++) {
            for (let j = 0; j < rect[0]; j++) {
                screen[i][j] = true
            }
        }
    } else if (line.startsWith('rotate row')) {
        const row = screen[parseInt(line.split('=')[1].split(' ')[0])]
        const distance = parseInt(line.split(' ')[4])
        rotateArray(row, distance)
    } else {
        const n = parseInt(line.split('=')[1].split(' ')[0])
        const column = []
        const distance = parseInt(line.split(' ')[4])
        for (let i = 0; i < 6; i++) {
            column.push(screen[i][n])
        }
        rotateArray(column, distance)
        for (let i = 0; i < 6; i++) {
            screen[i][n] = column[i]
        }
    }
    printScreen(screen)
}

console.log(countScreen(screen))
