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

const search1 = 17
const search2 = 61
let answer

const lines = getfilelines('10.txt')
const map = {}
for (const line of lines) {
    const ints = readints(line)
    if (ints.length == 2) {
        console.log(line)
        const [ value, bot ] = ints
        if (!(bot in map)) map[bot] = []
        map[bot].push(value)
        map[bot].sort()
        if (map[bot][0] == search1 && map[bot][1] == search2) {
            answer = bot
            break
        }
    }
}

console.log(map)
const outputs = {}

while (!answer) {
    for (const line of lines) {
        const ints = readints(line)
        if (ints.length == 3) {
            const [ bot, lowNum, highNum ] = ints
            if (!(bot in map)) map[bot] = []
            if (map[bot].length < 2) continue
            console.log(line)
            console.log(bot + ' -', map[bot])
            const whereLow = line.split(' ')[5]
            const whereHigh = line.split(' ')[10]
            if (whereLow == 'bot') {
                const giveBot = lowNum
                if (!(giveBot in map)) map[giveBot] = []
                map[giveBot].unshift(Math.min(...map[bot]))
                console.log(giveBot + ' -', map[giveBot])
            } else {
                console.log('ALKSDJFLKDSAJ')
                outputs[lowNum] = Math.min(...map[bot])
            }
            if (whereHigh == 'bot') {
                const giveBot = highNum
                if (!(giveBot in map)) map[giveBot] = []
                map[giveBot].push(Math.max(...map[bot]))
                console.log(giveBot + ' -', map[giveBot])
            } else {
                console.log('ALKSDJFLKDSAJ')
                outputs[highNum] = Math.max(...map[bot])
            }
            map[bot] = []
        }
    }
    console.log(outputs)
}

if (answer) {
    console.log(`answer is ${answer}`)
} else {
    console.log('fuck my life')
}

console.log(outputs)
