/**
 * @param {number} start
 * @param {number} goal
 * @return {number}
 */
var minBitFlips = function(start, goal) {
    let startBits = start.toString(2).split('').map((bit) => parseInt(bit));
    let goalBits = goal.toString(2).split('').map((bit) => parseInt(bit));
    let count = 0;
    
    
    if (startBits.length > goalBits.length) {
        let lengthDif = startBits.length - goalBits.length;
        for (let i = 0; i < lengthDif; i++) {
            goalBits.unshift(0);
        }
    }

    if (startBits.length < goalBits.length) {
        let lengthDif = goalBits.length - startBits.length;
        for (let i = 0; i < lengthDif; i++) {
            startBits.unshift(0);
        }
    }
    
    for (let i = goalBits.length - 1; i >= 0; i--) {
        if (startBits.length <= i) {
            if (goalBits[i] == 1) count++;
        } else {
            if (startBits[i] != goalBits[i]) {
                count += 1;
            }
        }
        
    }
    return count;
};


