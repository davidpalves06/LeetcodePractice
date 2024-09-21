/**
 * @param {string[]} words
 * @return {string[]}
 */
var findAllConcatenatedWordsInADict = function(words) {
    let wordSet =  new Set(words);
    let concatenatedWords = [];

    words.forEach((word) => {
        let isSubWord = Array(word.length + 1).fill(false);
        isSubWord[0]= true

        for (let i = 1; i <= word.length; i++) {
            for (let j = 0; j < i; j++) {
                if (!isSubWord[j]) continue;
                if (wordSet.has(word.slice(j,i)) && (i - j) != word.length) {
                    isSubWord[i] = true;
                    break;
                }
            }
            
        }

        if (isSubWord[word.length]) concatenatedWords.push(word)

    })
    return concatenatedWords;
};