/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var findKthNumber = function(n, k) {
    let curr = 1;
    let index = 1;
    while (curr <= n) {
        if (index == k) return curr;
        index++;
        if (curr * 10 <= n)
            curr *= 10;
        else {
            
            while (curr >= n || curr % 10 == 9) {
                curr = Math.floor(curr / 10);
            }
            curr++;
        }
    }
    

    return curr;
};

