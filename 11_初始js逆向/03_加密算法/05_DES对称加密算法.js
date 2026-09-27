const CryptoJS = require('crypto-js')

// DES 密钥必须是 8 字节
const key = CryptoJS.enc.Utf8.parse('12345678') // 8字节密钥（64位）

// 生成初始化向量（IV，8字节，因为 DES 分组为64位）
const iv = CryptoJS.enc.Utf8.parse('abcdefgq')

// 配置选项（使用 CBC 模式 + PKCS7 填充）
const cfg = {
    mode: CryptoJS.mode.CBC, // DES 同样支持 CBC 模式
    padding: CryptoJS.pad.Pkcs7,
    iv: iv // 传入 IV
}

// --------------------------
// DES 加密
// --------------------------
const encrypted = CryptoJS.DES.encrypt(
    '123456',
    key,
    cfg
).toString()

console.log('加密结果:', encrypted)

// --------------------------
// DES 解密
// --------------------------
const decrypted = CryptoJS.DES.decrypt(
    encrypted,
    key,
    cfg
).toString(CryptoJS.enc.Utf8)

console.log('解密结果:', decrypted)
