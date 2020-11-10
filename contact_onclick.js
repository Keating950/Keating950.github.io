function contact() {
    "use strict";
    function str_rot13(str){
        return (str+'').replace(/[a-zA-Z]/gi, function(s) {
            return String.fromCharCode(s.charCodeAt(0)+(s.toLowerCase()<'n'?13:-13))
        })
    }
    window.open(str_rot13(atob("em52eWdiOnhybmd2YXQuZXJ2cUB6bnZ5LnpwdHZ5eS5wbg==")))
}
