/**
 * @param {number[]} rolls
 * @param {number} mean
 * @param {number} n
 * @return {number[]}
 */
var missingRolls = function(rolls, mean, n) {
    const maxSum = (rolls.length + n) * mean;
    let sumOfNewElems = maxSum - rolls.reduce((elem,acc) => acc + elem);
    let response = []
    if ((sumOfNewElems / n) > 6 || (sumOfNewElems / n) < 1) return []; 
    for (let i = 0; i < n; i++) {
        response[i] = Math.round(sumOfNewElems / (n-i));
        sumOfNewElems -= response[i];
    }
    return response;
};

