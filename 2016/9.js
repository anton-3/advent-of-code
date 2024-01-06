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
    const line = getfilelines('9.txt')[0]
    let result = []
    let pointer = 0
    while (pointer < line.length) {
        const c = line[pointer]
        if (c != '(') {
            result.push(c)
            pointer++
        } else {
            let right = pointer
            while (line[right] != ')') right++
            const marker = line.slice(pointer+1, right)
            const nums = marker.split('x').map(x => parseInt(x))
            const numChars = nums[0]
            const numRepeats = nums[1]
            const repeatSection = line.slice(right+1, right+1+numChars)
            for (let i = 0; i < numRepeats; i++) {
                for (const c of repeatSection) {
                    result.push(c)
                }
            }
            console.log(nums, marker, pointer, right, repeatSection)
            pointer += (right-pointer) + 1 + numChars
        }
    }
    console.log(result.length)
}

function countString(string, numRepeats, memo) {
    if (string+numRepeats in memo) {
        return memo[string+numRepeats]
    }
    let count = 0
    for (let j = 0; j < numRepeats; j++) {
        for (let i = 0; i < string.length; i++) {
            const c = string[i]
            if (c != '(') {
                count++
                continue
            }
            let right = i
            while (string[right] != ')') right++
            right++
            const marker = string.slice(i+1, right)
            const [numChars, numRepeats] = marker.split('x').map(x => parseInt(x))
            const repeatSection = string.slice(right, right+numChars)
            count += countString(repeatSection, numRepeats, memo)
            i = right + numChars - 1
        }
    }
    memo[string+numRepeats] = count
    return count
}

function part2() {
    let line = getfilelines('9.txt')[0]
    console.log(countString(line, 1, {}))
    return
}

part2()
