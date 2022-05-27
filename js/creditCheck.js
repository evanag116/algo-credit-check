exports.creditCheck = function(str) {
    str = str.split("")
    let sum = 0
    for (let i = 0; i < str.length; i++) {
        if(i%2 == 0) {
            str[i] *= 2
            if (str[i] > 9) {
                str[i] = (str[i] % 10) + parseInt(str[i]/10)
            }
        } else {
            str[i] *= 1
        }
        sum += str[i]
    }
    return (sum % 10 == 0) ? "The number is valid!" : "The number is invalid!"
}


