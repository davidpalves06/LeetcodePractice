
class PrefixNode {

    constructor() {
        this.count = 0;
        this.children = new Array(26).fill(undefined);
    }

    incrementCount() {
        this.count++;
    }

    insertChild(char) {
        let i = char.charCodeAt(0) - "a".charCodeAt(0);
        if (this.children[i] == undefined) this.children[i] = new PrefixNode();
        this.children[i].incrementCount();
        return this.children[i];
    }

}

class Trie {
    constructor() {
        this.root = new PrefixNode();
    }

    getScore(word){
        let curr = this.root;
        let score = 0;
        for (const letter of word) {
            let i = letter.charCodeAt(0) - "a".charCodeAt(0);
            curr = curr.children[i];
            score += curr.count;
        }
        return score;
    }

    insertWord(word) {
        let curr = this.root;

        for (const letter of word) {
            curr = curr.insertChild(letter);
        }
    }

}


/**
 * @param {string[]} words
 * @return {number[]}
 */
var sumPrefixScores = function(words) {
    let prefixTree = new Trie();
    let res = [];
    for (const word of words) {
        prefixTree.insertWord(word)
    }
    
    for (const word of words) {
        res.push(prefixTree.getScore(word));
    }

    return res;
    
};
console.log(sumPrefixScores(["abc","ab","bc","b"]));