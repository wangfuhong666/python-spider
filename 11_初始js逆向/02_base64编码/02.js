
let base64_encode = (str) => {
    return Buffer.from(str, "utf-8").toString("base64");

}
let base64_decode = (str) => {
    return Buffer.from(str, "base64").toString("utf-8");
}