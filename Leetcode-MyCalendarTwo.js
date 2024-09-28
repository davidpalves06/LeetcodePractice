class MyCalendarTwo {
    constructor() {
        this.overlapping = [];
        this.events = [];
    }
    /**
     * @param {number} start
     * @param {number} end
     * @return {boolean}
     */
    book(start, end) {
        for (const interval of this.overlapping) {
            const {intStart,intEnd} = interval;
            if (end > intStart && start < intEnd) {
                return false;
            }
        }

        for (const event of this.events) {
            const {eStart,eEnd} = event;
            if (end > eStart && start < eEnd) {
                this.overlapping.push({intStart:Math.max(start,eStart),intEnd: Math.min(end,eEnd)});
            }
        }
        this.events.push({eStart:start,eEnd:end});
        return true;
    }
}


/** 
 * Your MyCalendarTwo object will be instantiated and called as such:
 * var obj = new MyCalendarTwo()
 * var param_1 = obj.book(start,end)
 */