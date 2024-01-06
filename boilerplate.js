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
    let hash = crypto.createHash('md5').update(string).digest('hex')
    for (let i = 0; i < 2016; i++) {
        hash = crypto.createHash('md5').update(hash).digest('hex')
    }
    return hash
}

function readints(string) {
    return string.match(/\d+|\D+/g).map(x => parseInt(x)).filter(x => !isNaN(x));
}


const lines = getfilelines('test.txt')
for (const line of lines) {
    console.log(line)
}

