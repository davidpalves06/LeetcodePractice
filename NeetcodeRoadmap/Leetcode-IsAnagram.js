class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let firstCounter = new Map()
        if (s.length != t.length) return false

        for (const c of s) {
            if (!firstCounter.has(c)) 
                firstCounter.set(c,1)
            else firstCounter.set(c,firstCounter.get(c) + 1);
        }

        for (const c of t) {
            if (!firstCounter.has(c)) 
                return false
            else firstCounter.set(c,firstCounter.get(c) - 1);
        }

        for(const value of firstCounter.values()) {
            if (value != 0) return false
        }

        return true
    }
}