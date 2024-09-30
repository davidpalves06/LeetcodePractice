/**
 * @param {number} maxSize
 */
class CustomStack {
    constructor(maxSize) {
        this.stack = [];
        this.maxSize = maxSize;
        this.currentLength = 0;
    }
    /**
     * @param {number} x
     * @return {void}
     */
    push(x) {
        if (this.currentLength == this.maxSize) {
            return;
        }
        else this.currentLength = this.stack.push(x);
    }
    /**
     * @return {number}
     */
    pop() {
        const poppedValue = this.stack.pop();
        this.currentLength--;
        if (poppedValue) return poppedValue;
        else return -1;
    }
    /**
     * @param {number} k
     * @param {number} val
     * @return {void}
     */
    increment(k, val) {
        let maxLength = 0;
        if (k < this.currentLength){
            maxLength = k;
        }
        else maxLength = this.currentLength;
        for (let i = 0; i < maxLength; i++) {
            this.stack[i] += val;
        }
    }
}




/** 
 * Your CustomStack object will be instantiated and called as such:
 * var obj = new CustomStack(maxSize)
 * obj.push(x)
 * var param_2 = obj.pop()
 * obj.increment(k,val)
 */