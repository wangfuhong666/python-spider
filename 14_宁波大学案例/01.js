var CryptoJS = CryptoJS || function (n, f) {
    var c = {}, q = c.lib = {}, u = function () {
    }, v = q.Base = {
        extend: function (a) {
            u.prototype = this;
            var e = new u;
            a && e.mixIn(a);
            e.hasOwnProperty("init") || (e.init = function () {
                    e.$super.init.apply(this, arguments)
                });
            e.init.prototype = e;
            e.$super = this;
            return e
        }, create: function () {
            var a = this.extend();
            a.init.apply(a, arguments);
            return a
        }, mixIn: function (a) {
            for (var e in a) a.hasOwnProperty(e) && (this[e] = a[e]);
            a.hasOwnProperty("toString") && (this.toString = a.toString)
        }
    }, r = q.WordArray = v.extend({
        init: function (a, e) {
            a = this.words = a || [];
            this.sigBytes = e != f ? e : 4 * a.length
        }, toString: function (a) {
            return (a || w).stringify(this)
        }, concat: function (a) {
            var e = this.words, d = a.words, g = this.sigBytes;
            a = a.sigBytes;
            this.clamp();
            if (g % 4) for (var p = 0; p < a; p++) e[g + p >>> 2] |= (d[p >>> 2] >>> 24 - p % 4 * 8 & 255) << 24 - (g + p) % 4 * 8; else if (65535 < d.length) for (p = 0; p < a; p += 4) e[g + p >>> 2] = d[p >>> 2]; else e.push.apply(e, d);
            this.sigBytes += a;
            return this
        }, clamp: function () {
            var a = this.words, e = this.sigBytes;
            a[e >>> 2] &= 4294967295 << 32 - e % 4 * 8;
            a.length = n.ceil(e / 4)
        }
    }), x = c.enc = {}, w = x.Hex = {}, b = x.Latin1 = {
        parse: function (a) {
            for (var e = a.length, d = [], g = 0; g < e; g++) d[g >>> 2] |= (a.charCodeAt(g) & 255) << 24 - g % 4 * 8;
            return new r.init(d, e)
        }
    }, y = x.Utf8 = {
        parse: function (a) {
            return b.parse(unescape(encodeURIComponent(a)))
        }
    }, t = q.BufferedBlockAlgorithm = v.extend({
        reset: function () {
            this._data = new r.init;
            this._nDataBytes = 0
        }, _append: function (a) {
            "string" == typeof a && (a = y.parse(a));
            this._data.concat(a);
            this._nDataBytes += a.sigBytes
        }, _process: function (a) {
            var e = this._data, d = e.words, g = e.sigBytes, p = this.blockSize, b = g / (4 * p),
                b = a ? n.ceil(b) : n.max((b | 0) - this._minBufferSize, 0);
            a = b * p;
            g = n.min(4 * a, g);
            if (a) {
                for (var t = 0; t < a; t += p) this._doProcessBlock(d, t);
                t = d.splice(0, a);
                e.sigBytes -= g
            }
            return new r.init(t, g)
        }, _minBufferSize: 0
    });
    q.Hasher = t.extend({
        cfg: v.extend(), blockSize: 16
    });
    var A = c.algo = {};
    return c
}(Math);
(function () {
        var n = CryptoJS, f = n.lib.WordArray;
        n.enc.Base64 = {
            stringify: function (c) {
                var f = c.words, u = c.sigBytes, v = this._map;
                c.clamp();
                c = [];
                for (var r = 0; r < u; r += 3) for (var n = (f[r >>> 2] >>> 24 - r % 4 * 8 & 255) << 16 | (f[r + 1 >>> 2] >>> 24 - (r + 1) % 4 * 8 & 255) << 8 | f[r + 2 >>> 2] >>> 24 - (r + 2) % 4 * 8 & 255, w = 0; 4 > w && r + .75 * w < u; w++) c.push(v.charAt(n >>> 6 * (3 - w) & 63));
                if (f = v.charAt(64)) for (; c.length % 4;) c.push(f);
                return c.join("")
            }, _map: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/\x3d"
        }
    })();
CryptoJS.lib.Cipher || function (n) {
    var f = CryptoJS, c = f.lib, q = c.Base, u = c.WordArray, v = c.BufferedBlockAlgorithm, r = f.enc.Base64,
        x = f.algo.EvpKDF, w = c.Cipher = v.extend({
            cfg: q.extend(), createEncryptor: function (d, a) {
                return this.create(this._ENC_XFORM_MODE, d, a)
            }, init: function (d, a, b) {
                this.cfg = this.cfg.extend(b);
                this._xformMode = d;
                this._key = a;
                this.reset()
            }, reset: function () {
                v.reset.call(this);
                this._doReset()
            }, finalize: function (d) {
                d && this._append(d);
                return this._doFinalize()
            }, keySize: 4, ivSize: 4, _ENC_XFORM_MODE: 1, _DEC_XFORM_MODE: 2, _createHelper: function (d) {
                return {
                    encrypt: function (b, p, c) {
                        return ("string" == typeof p ? e : a).encrypt(d, b, p, c)
                    }
                }
            }
        });
    c.StreamCipher = w.extend({
        blockSize: 1
    });
    var b = f.mode = {}, y = function (d, a, b) {
        var g = this._iv;
        g ? this._iv = n : g = this._prevBlock;
        for (var c = 0; c < b; c++) d[a + c] ^= g[c]
    }, t = (c.BlockCipherMode = q.extend({
        createEncryptor: function (d, a) {
            return this.Encryptor.create(d, a)
        }, init: function (d, a) {
            this._cipher = d;
            this._iv = a
        }
    })).extend();
    t.Encryptor = t.extend({
        processBlock: function (d, a) {
            var b = this._cipher, g = b.blockSize;
            y.call(this, d, a, g);
            b.encryptBlock(d, a);
            this._prevBlock = d.slice(a, a + g)
        }
    });
    t.Decryptor = t.extend({});
    b = b.CBC = t;
    t = (f.pad = {}).Pkcs7 = {
        pad: function (a, b) {
            for (var d = 4 * b, d = d - a.sigBytes % d, g = d << 24 | d << 16 | d << 8 | d, c = [], e = 0; e < d; e += 4) c.push(g);
            d = u.create(c, d);
            a.concat(d)
        }
    };
    c.BlockCipher = w.extend({
        cfg: w.cfg.extend({
            mode: b, padding: t
        }), reset: function () {
            w.reset.call(this);
            var d = this.cfg, a = d.iv, d = d.mode;
            if (this._xformMode == this._ENC_XFORM_MODE) var b = d.createEncryptor; else b = d.createDecryptor, this._minBufferSize = 1;
            this._mode = b.call(d, this, a && a.words)
        }, _doProcessBlock: function (a, b) {
            this._mode.processBlock(a, b)
        }, _doFinalize: function () {
            var a = this.cfg.padding;
            if (this._xformMode == this._ENC_XFORM_MODE) {
                a.pad(this._data, this.blockSize);
                var b = this._process(!0)
            } else b = this._process(!0), a.unpad(b);
            return b
        }, blockSize: 4
    });
    var A = c.CipherParams = q.extend({
        init: function (a) {
            this.mixIn(a)
        }, toString: function (a) {
            return (a || this.formatter).stringify(this)
        }
    }), b = (f.format = {}).OpenSSL = {
        stringify: function (a) {
            var d = a.ciphertext;
            a = a.salt;
            return (a ? u.create([1398893684, 1701076831]).concat(a).concat(d) : d).toString(r)
        }
    }, a = c.SerializableCipher = q.extend({
        cfg: q.extend({
            format: b
        }), encrypt: function (a, b, c, e) {
            e = this.cfg.extend(e);
            var d = a.createEncryptor(c, e);
            b = d.finalize(b);
            d = d.cfg;
            return A.create({
                ciphertext: b,
                key: c,
                iv: d.iv,
                algorithm: a,
                mode: d.mode,
                padding: d.padding,
                blockSize: a.blockSize,
                formatter: e.format
            })
        }
    }), f = (f.kdf = {}).OpenSSL = {}, e = c.PasswordBasedCipher = a.extend({
        cfg: a.cfg.extend({
            kdf: f
        })
    })
}();
(function () {
        for (var n = CryptoJS, f = n.lib.BlockCipher, c = n.algo, q = [], u = [], v = [], r = [], x = [], w = [], b = [], y = [], t = [], A = [], a = [], e = 0; 256 > e; e++) a[e] = 128 > e ? e << 1 : e << 1 ^ 283;
        for (var d = 0, g = 0, e = 0; 256 > e; e++) {
            var p = g ^ g << 1 ^ g << 2 ^ g << 3 ^ g << 4, p = p >>> 8 ^ p & 255 ^ 99;
            q[d] = p;
            u[p] = d;
            var B = a[d], H = a[B], I = a[H], z = 257 * a[p] ^ 16843008 * p;
            v[d] = z << 24 | z >>> 8;
            r[d] = z << 16 | z >>> 16;
            x[d] = z << 8 | z >>> 24;
            w[d] = z;
            z = 16843009 * I ^ 65537 * H ^ 257 * B ^ 16843008 * d;
            b[p] = z << 24 | z >>> 8;
            y[p] = z << 16 | z >>> 16;
            t[p] = z << 8 | z >>> 24;
            A[p] = z;
            d ? (d = B ^ a[a[a[I ^ B]]], g ^= a[a[g]]) : d = g = 1
        }
        var J = [0, 1, 2, 4, 8, 16, 32, 64, 128, 27, 54], c = c.AES = f.extend({
            _doReset: function () {
                for (var a = this._key, d = a.words, c = a.sigBytes / 4, a = 4 * ((this._nRounds = c + 6) + 1), e = this._keySchedule = [], f = 0; f < a; f++) if (f < c) e[f] = d[f]; else {
                    var g = e[f - 1];
                    f % c ? 6 < c && 4 == f % c && (g = q[g >>> 24] << 24 | q[g >>> 16 & 255] << 16 | q[g >>> 8 & 255] << 8 | q[g & 255]) : (g = g << 8 | g >>> 24, g = q[g >>> 24] << 24 | q[g >>> 16 & 255] << 16 | q[g >>> 8 & 255] << 8 | q[g & 255], g ^= J[f / c | 0] << 24);
                    e[f] = e[f - c] ^ g
                }
                d = this._invKeySchedule = [];
                for (c = 0; c < a; c++) f = a - c, g = c % 4 ? e[f] : e[f - 4], d[c] = 4 > c || 4 >= f ? g : b[q[g >>> 24]] ^ y[q[g >>> 16 & 255]] ^ t[q[g >>> 8 & 255]] ^ A[q[g & 255]]
            }, encryptBlock: function (a, b) {
                this._doCryptBlock(a, b, this._keySchedule, v, r, x, w, q)
            }, _doCryptBlock: function (a, b, c, d, e, f, g, h) {
                for (var m = this._nRounds, k = a[b] ^ c[0], l = a[b + 1] ^ c[1], n = a[b + 2] ^ c[2], p = a[b + 3] ^ c[3], q = 4, r = 1; r < m; r++) var t = d[k >>> 24] ^ e[l >>> 16 & 255] ^ f[n >>> 8 & 255] ^ g[p & 255] ^ c[q++], u = d[l >>> 24] ^ e[n >>> 16 & 255] ^ f[p >>> 8 & 255] ^ g[k & 255] ^ c[q++], v = d[n >>> 24] ^ e[p >>> 16 & 255] ^ f[k >>> 8 & 255] ^ g[l & 255] ^ c[q++], p = d[p >>> 24] ^ e[k >>> 16 & 255] ^ f[l >>> 8 & 255] ^ g[n & 255] ^ c[q++], k = t, l = u, n = v;
                t = (h[k >>> 24] << 24 | h[l >>> 16 & 255] << 16 | h[n >>> 8 & 255] << 8 | h[p & 255]) ^ c[q++];
                u = (h[l >>> 24] << 24 | h[n >>> 16 & 255] << 16 | h[p >>> 8 & 255] << 8 | h[k & 255]) ^ c[q++];
                v = (h[n >>> 24] << 24 | h[p >>> 16 & 255] << 16 | h[k >>> 8 & 255] << 8 | h[l & 255]) ^ c[q++];
                p = (h[p >>> 24] << 24 | h[k >>> 16 & 255] << 16 | h[l >>> 8 & 255] << 8 | h[n & 255]) ^ c[q++];
                a[b] = t;
                a[b + 1] = u;
                a[b + 2] = v;
                a[b + 3] = p
            }, keySize: 8
        });
        n.AES = f._createHelper(c)
    })();
function getAesString(n, f, c) {
    f = f.replace(/(^\s+)|(\s+$)/g, "");
    f = CryptoJS.enc.Utf8.parse(f);
    c = CryptoJS.enc.Utf8.parse(c);
    return CryptoJS.AES.encrypt(n, f, {
        iv: c, mode: CryptoJS.mode.CBC, padding: CryptoJS.pad.Pkcs7
    }).toString()
}
function encryptAES(n, f) {
    return f ? getAesString(randomString(64) + n, f, randomString(16)) : n
}
var $aes_chars = "ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678", aes_chars_len = $aes_chars.length;
function randomString(n) {
    var f = "";
    for (i = 0; i < n; i++) f += $aes_chars.charAt(Math.floor(Math.random() * aes_chars_len));
    return f
}
let get_password = (n, f) => {
    return encryptAES(n, f)
}
console.log(get_password('123456', "EebcecwyLAA0Irtm"));
