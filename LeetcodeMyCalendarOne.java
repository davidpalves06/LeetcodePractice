

class Tree {
    public int start;
    public int end;
    public Tree left;
    public Tree right;

    public Tree(int start,int end) {
        this.end = end;
        this.start = start;
        this.left = null;
        this.right = null;
    }

    public boolean insert(int start,int end) {
        Tree currentNode = this;
        while (true) {
            if (end <= currentNode.start) {
                if (currentNode.left != null) {
                    currentNode = currentNode.left;
                }
                else {
                    currentNode.left = new Tree(start, end);
                    return true;
                }
            }
            else if (start >= currentNode.end) {
                if (currentNode.right != null) {
                    currentNode = currentNode.right;
                }
                else {
                    currentNode.right = new Tree(start, end);
                    return true;
                }
            }
            else return false;
        }
    }
}

class MyCalendar {

    private Tree bookingTree;
    public MyCalendar() {
        this.bookingTree = null;
    }
    
    public boolean book(int start, int end) {
        if (bookingTree == null) {
            bookingTree = new Tree(start, end);
            return true;
        }
        return bookingTree.insert(start, end);
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * boolean param_1 = obj.book(start,end);
 */