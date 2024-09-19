/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSubarray = function(nums) {
    let longest,max = 0;
    for (let index = 0; index < nums.length; index++) {
        let number = nums[index];
        if (number > max) {
            max = number;
            longest = 0;
        }
        if (number == max) {
            let length = 0;
            while (number == max) {
                length++;
                index++;
                number = nums[index];
            }
            if (length > longest) longest = length;
            index--;
        }
    }
    
    return longest;    
}

console.log(longestSubarray([586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,516529,516529,516529,516529,516529,516529,516529,516529,516529,516529,516529,516529,516529,516529,516529,516529,516529,516529,516529,516529,516529,516529,516529,516529,516529,516529,516529,516529,516529,516529,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,55816,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,586730,232392,232392,294503]));
