/**
 * @param {number[]} arr
 * @return {number[]}
 */
var arrayRankTransform = function(arr) {
    let sortedArr = [...new Set(arr)].sort((a,b) => a-b)
    
    let rankMap = new Map()
    sortedArr.forEach((rank, number) => {
        rankMap.set(rank, number + 1)
    })    
    return arr.map(x => rankMap.get(x))
};

console.log(arrayRankTransform([37,12,28,9,100,56,80,5,12]));
