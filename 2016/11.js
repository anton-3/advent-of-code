const fs = require('node:fs')

function getfilelines(filename) {
    try {
        const data = fs.readFileSync(filename, 'utf8')
        return data.trim().split('\n')
    } catch (err) {
        console.log(err)
    }
}


function print(generators, microchips) {
    for (let i = 0; i < 4; i++) {
        const floor = 4 - i
        process.stdout.write(`F${floor}: `)
        for (const generator of generators[floor-1]) {
            process.stdout.write(`${generator[0].toUpperCase()}G `)
        }
        for (const microchip of microchips[floor-1]) {
            process.stdout.write(`${microchip[0].toUpperCase()}M `)
        }
        console.log()
    }
}

function part1(floors) {

}

// function part1(generators, microchips) {
//     print(generators, microchips)
//     let floor = 0
//     while (generators[0] + generators[1] + generators[2] + microchips[0] + microchips[1] + microchips[2] != '') {
//         const g = generators[floor]
//         const m = microchips[floor]

//     }
// }

const generators = [[], ['hydrogen'], ['lithium'], []]
const microchips = [['hydrogen', 'lithium'], [], [], []]
const floors = ['HG', 'LG', 'HM', 'LM']
// const generators = [['strontium', 'plutonium'], ['thulium', 'ruthenium', 'curium'], [], []]
// const microchips = [['strontium', 'plutonium'], ['ruthenium', 'curium'], ['thulium'], []]

part1(generators, microchips)
