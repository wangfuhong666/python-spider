const crypto =  require('crypto')

let md5_encode = (str) => {
    const obj = crypto.createHash('md5')
    obj.update(str)
    return obj.digest('hex')
}
console.log(md5_encode('123456'))