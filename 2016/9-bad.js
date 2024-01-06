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

function part2() {
    let line = getfilelines('sample9.txt')[0]
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
            right++
            const nums = marker.split('x').map(x => parseInt(x))
            const numChars = nums[0]
            const numRepeats = nums[1]
            const repeatSection = line.slice(right, right+numChars)
            line = line.slice(0, right) + repeatSection.repeat(numRepeats-1) + line.slice(right)
            // console.log(nums, pointer, right, repeatSection)
            pointer += (right-pointer)
        }
    }
    console.log(result.length)
}

part2()
