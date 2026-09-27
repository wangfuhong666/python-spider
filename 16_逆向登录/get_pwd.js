const JSEncrypt = require('jsencrypt');
function doLogin(password_old,pk) {
    //var password_old = $("#MemberPassword").val();//密码原文
    var encrypt = new JSEncrypt();
    var public_key = pk
    encrypt.setPublicKey(public_key);
    return encrypt.encrypt(password_old);
}
let get_password=(pwd,pk)=>
{
    return doLogin(pwd,pk);
}


