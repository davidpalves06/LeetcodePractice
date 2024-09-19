/**
 * @param {string} s1
 * @param {string} s2
 * @return {string[]}
 */
var uncommonFromSentences = function(s1, s2) {
    let joinSplitedSentences = s1.concat(" ",s2).split(" ");
    const uniqueArray = joinSplitedSentences.filter(item => joinSplitedSentences.indexOf(item) === joinSplitedSentences.lastIndexOf(item));
    return uniqueArray;
};
