/**
 * @param {string} s
 * @return {number}
 */
var minAddToMakeValid = function(s) {
    let counter = 0
    let inserts = 0
    for (char of s) {
        if (char == '(') counter++;
        else {
            if (counter == 0) {
                inserts++;
            }
            else counter--;
        }
    }
    return counter + inserts;
};

console.log(minAddToMakeValid("((("));
console.log(minAddToMakeValid("()))(("));
