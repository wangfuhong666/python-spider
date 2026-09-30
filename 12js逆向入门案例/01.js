function _(s, u) {
    return s << u | s >>> 32 - u
}
function r(s, u) {
    var d = (s & 65535) + (u & 65535), R = (s >> 16) + (u >> 16) + (d >> 16);
    return R << 16 | d & 65535
}
function a(s, u, d, R, Q, H) {
    return r(_(r(r(u, s), r(R, H)), Q), d)
}
function m(s, u, d, R, Q, H, X) {
    return a(u & d | ~u & R, s, u, Q, H, X)
}
function i(s, u, d, R, Q, H, X) {
    return a(u & R | d & ~R, s, u, Q, H, X)
}
function l(s, u, d, R, Q, H, X) {
    return a(u ^ d ^ R, s, u, Q, H, X)
}
function v(s, u, d, R, Q, H, X) {
    return a(d ^ (u | ~R), s, u, Q, H, X)
}
function T(s) {
                var u, d = [];
                d[(s.length >> 2) - 1] = void 0;
                for (u = 0; u < d.length; u += 1) {
                    d[u] = 0
                }
                for (u = 0; u < s.length * 8; u += 8) {
                    d[u >> 5] |= (s.charCodeAt(u / 8) & 255) << u % 32
                }
                return d
}
function z(s, u) {
                s[u >> 5] |= 128 << u % 32;
                s[(u + 64 >>> 9 << 4) + 14] = u;
                var d, R, Q, H, X, f = 1732584193, g = -271733879, h = -1732584194, b = 271733878;
                for (d = 0; d < s.length; d += 16) {
                    R = f;
                    Q = g;
                    H = h;
                    X = b;
                    f = m(f, g, h, b, s[d], 7, -680876936);
                    b = m(b, f, g, h, s[d + 1], 12, -389564586);
                    h = m(h, b, f, g, s[d + 2], 17, 606105819);
                    g = m(g, h, b, f, s[d + 3], 22, -1044525330);
                    f = m(f, g, h, b, s[d + 4], 7, -176418897);
                    b = m(b, f, g, h, s[d + 5], 12, 1200080426);
                    h = m(h, b, f, g, s[d + 6], 17, -1473231341);
                    g = m(g, h, b, f, s[d + 7], 22, -45705983);
                    f = m(f, g, h, b, s[d + 8], 7, 1770035416);
                    b = m(b, f, g, h, s[d + 9], 12, -1958414417);
                    h = m(h, b, f, g, s[d + 10], 17, -42063);
                    g = m(g, h, b, f, s[d + 11], 22, -1990404162);
                    f = m(f, g, h, b, s[d + 12], 7, 1804603682);
                    b = m(b, f, g, h, s[d + 13], 12, -40341101);
                    h = m(h, b, f, g, s[d + 14], 17, -1502002290);
                    g = m(g, h, b, f, s[d + 15], 22, 1236535329);
                    f = i(f, g, h, b, s[d + 1], 5, -165796510);
                    b = i(b, f, g, h, s[d + 6], 9, -1069501632);
                    h = i(h, b, f, g, s[d + 11], 14, 643717713);
                    g = i(g, h, b, f, s[d], 20, -373897302);
                    f = i(f, g, h, b, s[d + 5], 5, -701558691);
                    b = i(b, f, g, h, s[d + 10], 9, 38016083);
                    h = i(h, b, f, g, s[d + 15], 14, -660478335);
                    g = i(g, h, b, f, s[d + 4], 20, -405537848);
                    f = i(f, g, h, b, s[d + 9], 5, 568446438);
                    b = i(b, f, g, h, s[d + 14], 9, -1019803690);
                    h = i(h, b, f, g, s[d + 3], 14, -187363961);
                    g = i(g, h, b, f, s[d + 8], 20, 1163531501);
                    f = i(f, g, h, b, s[d + 13], 5, -1444681467);
                    b = i(b, f, g, h, s[d + 2], 9, -51403784);
                    h = i(h, b, f, g, s[d + 7], 14, 1735328473);
                    g = i(g, h, b, f, s[d + 12], 20, -1926607734);
                    f = l(f, g, h, b, s[d + 5], 4, -378558);
                    b = l(b, f, g, h, s[d + 8], 11, -2022574463);
                    h = l(h, b, f, g, s[d + 11], 16, 1839030562);
                    g = l(g, h, b, f, s[d + 14], 23, -35309556);
                    f = l(f, g, h, b, s[d + 1], 4, -1530992060);
                    b = l(b, f, g, h, s[d + 4], 11, 1272893353);
                    h = l(h, b, f, g, s[d + 7], 16, -155497632);
                    g = l(g, h, b, f, s[d + 10], 23, -1094730640);
                    f = l(f, g, h, b, s[d + 13], 4, 681279174);
                    b = l(b, f, g, h, s[d], 11, -358537222);
                    h = l(h, b, f, g, s[d + 3], 16, -722521979);
                    g = l(g, h, b, f, s[d + 6], 23, 76029189);
                    f = l(f, g, h, b, s[d + 9], 4, -640364487);
                    b = l(b, f, g, h, s[d + 12], 11, -421815835);
                    h = l(h, b, f, g, s[d + 15], 16, 530742520);
                    g = l(g, h, b, f, s[d + 2], 23, -995338651);
                    f = v(f, g, h, b, s[d], 6, -198630844);
                    b = v(b, f, g, h, s[d + 7], 10, 1126891415);
                    h = v(h, b, f, g, s[d + 14], 15, -1416354905);
                    g = v(g, h, b, f, s[d + 5], 21, -57434055);
                    f = v(f, g, h, b, s[d + 12], 6, 1700485571);
                    b = v(b, f, g, h, s[d + 3], 10, -1894986606);
                    h = v(h, b, f, g, s[d + 10], 15, -1051523);
                    g = v(g, h, b, f, s[d + 1], 21, -2054922799);
                    f = v(f, g, h, b, s[d + 8], 6, 1873313359);
                    b = v(b, f, g, h, s[d + 15], 10, -30611744);
                    h = v(h, b, f, g, s[d + 6], 15, -1560198380);
                    g = v(g, h, b, f, s[d + 13], 21, 1309151649);
                    f = v(f, g, h, b, s[d + 4], 6, -145523070);
                    b = v(b, f, g, h, s[d + 11], 10, -1120210379);
                    h = v(h, b, f, g, s[d + 2], 15, 718787259);
                    g = v(g, h, b, f, s[d + 9], 21, -343485551);
                    f = r(f, R);
                    g = r(g, Q);
                    h = r(h, H);
                    b = r(b, X)
                }
                return [f, g, h, b]
}
function P(s) {
    var u, d = "";
    for (u = 0; u < s.length * 32; u += 8) {
        d += String.fromCharCode(s[u >> 5] >>> u % 32 & 255)
    }
    return d
}
function J(s) {
    return P(z(T(s), s.length * 8))
}
function oe(s) {
                var u = "0123456789abcdef", d = "", R, Q;
                for (Q = 0; Q < s.length; Q += 1) {
                    R = s.charCodeAt(Q);
                    d += u.charAt(R >>> 4 & 15) + u.charAt(R & 15)
                }
                return d
}
function ie(s) {
    return unescape(encodeURIComponent(s))
}
function re(s) {
    return J(ie(s))
}
let ue=(s)=>{
    return oe(re(s))
}
let get_pwd=(password)=>{
    return ue(password)
}
console.log(get_pwd('123456'))