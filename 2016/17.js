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

function getNeighbors(passcode, path) {
    let x = 0
    let y = 0
    for (const c of path) {
        switch (c) {
            case 'R':
                x++
                break
            case 'L':
                x--
                break
            case 'U':
                y--
                break
            case 'D':
                y++
                break
        }
    }
    const currentMD5 = md5(passcode + path)
    const directions = []
    for (let i = 0; i < 4; i++) {
        directions.push(isNaN(currentMD5[i]) && 'a' != currentMD5[i])
    }
    if (x == 0) directions[2] = false
    if (x == 3) directions[3] = false
    if (y == 0) directions[0] = false
    if (y == 3) directions[1] = false

    const neighbors = []
    for (let i = 0; i < 4; i++) {
        if (!directions[i]) continue

        let newDirection
        switch (i) {
            case 0:
                newDirection = 'U'
                break
            case 1:
                newDirection = 'D'
                break
            case 2:
                newDirection = 'L'
                break
            case 3:
                newDirection = 'R'
                break
            default:
                console.error('WHAT THE FUCK')
        }
        neighbors.push(path + newDirection)
    }
    return neighbors
}

function checkGoal(path) {
    let x = 0
    let y = 0
    for (const c of path) {
        switch (c) {
            case 'R':
                x++
                break
            case 'L':
                x--
                break
            case 'U':
                y--
                break
            case 'D':
                y++
                break
        }
    }
    return x == 3 && y == 3
}

function bfs(passcode) {
    const queue = []
    const visited = new Set()
    const start = ''
    visited.add(start)
    queue.push(start)

    let longest = 'no solution found'
    while (queue.length > 0) {
        // console.log('queue: ', queue)
        const currentPath = queue.shift()
        if (checkGoal(currentPath)) {
            longest = currentPath
            continue
        }

        const neighbors = getNeighbors(passcode, currentPath)
        for (const neighbor of neighbors) {
            if (!visited.has(neighbor)) {
                queue.push(neighbor)
                visited.add(neighbor)
            }
        }
    }
    return longest
}

const passcode = 'vwbaicqe'

const path = bfs(passcode)
console.log(path)
console.log(path.length)
