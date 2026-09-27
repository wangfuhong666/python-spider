// 导入 crypto-js 第三方加密库，并把这个模块对象保存到 crypto_js 变量中
const crypto_js = require('crypto-js')

// 把字符串形式的密钥按照 UTF-8 编码转换成 CryptoJS 可以使用的 WordArray 数据对象
// 这个 key 后面会作为 AES 加密或解密时使用的密钥
const key = crypto_js.enc.Utf8.parse(
    '1234567890abcdef1234567890abcdef'
)
// 把字符串形式的初始化向量 IV 按 UTF-8 编码转换成 CryptoJS 可以使用的 WordArray 数据对象
// CBC 加密模式需要使用 IV
//固定IV
//const iv = crypto_js.enc.Utf8.parse('1234567890123456')
//随机iv
const iv = crypto_js.lib.WordArray.random(16)
// 创建一个配置对象 cfg，用来统一保存 AES 加密时使用的参数
const cfg = {
    // 指定 AES 的工作模式为 CBC 模式
    mode: crypto_js.mode.CBC,

    // 指定数据不足一个 AES 数据块时，使用 PKCS7 方式进行填充
    padding: crypto_js.pad.Pkcs7,

    // 指定 CBC 模式使用的初始化向量为上面定义的 iv
    iv: iv,
}
const tmp = crypto_js.AES.encrypt('123456',key,cfg).toString()
console.log(tmp)
const de = crypto_js.AES.decrypt(tmp,key,cfg).toString(crypto_js.enc.Utf8)
console.log(de)