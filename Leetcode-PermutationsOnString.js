/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function(s1, s2) {
    let counter = new Map()
    for (const letter of s1) {
        counter.get(letter) == undefined ? counter.set(letter,1) : counter.set(letter,counter.get(letter) + 1);
    }
    

    let size = s1.length;
    let left = 0,right = 0;
    
    while(left <= right && right < s2.length) {
        
        if (counter.get(s2.charAt(right)) > 0) {
            counter.set(s2.charAt(right),counter.get(s2.charAt(right)) - 1);
            right++;
        }
        else if (!counter.has(s2.charAt(right))) {
            while (left<right) {
                counter.set(s2.charAt(left),counter.get(s2.charAt(left)) + 1);
                left++;
            }
            left++;
            right++;
        } else {
            counter.set(s2.charAt(left),counter.get(s2.charAt(left)) + 1);
            left++;
        }

        if (right-left == size) {
            return true
        } 
    }
    return false
};

console.log(checkInclusion("adc","dcda"));

