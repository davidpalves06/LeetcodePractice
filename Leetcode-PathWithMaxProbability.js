/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number[]} succProb
 * @param {number} start_node
 * @param {number} end_node
 * @return {number}
 */
var maxProbability = function(n, edges, succProb, start_node, end_node) {
    let adjacencyList = {};
    let currentMaxProbs = []

    for (let i = 0; i < n; i++) {
        adjacencyList[i] = [];
        currentMaxProbs[i] = 0; 
    }
    
    for (let i = 0; i < edges.length; i++) {
        let nodeA = edges[i][0]    
        let nodeB = edges[i][1]    
        
        adjacencyList[nodeA].push({dest : nodeB, prob: succProb[i]});
        adjacencyList[nodeB].push({dest : nodeA, prob: succProb[i]});
    }



    let queue = [];
    let currentNode = start_node;
    currentMaxProbs[start_node] = 1

    while (currentNode != undefined) {
        if (currentNode === end_node) {
            return currentMaxProbs[end_node];
        }

        for (let i = 0; i < adjacencyList[currentNode].length; i++) {
            let edge = adjacencyList[currentNode][i];
            let edgeProb = currentMaxProbs[currentNode] * edge["prob"]
            let edgeDest = edge.dest;

            if (edgeProb > currentMaxProbs[edgeDest]) {
                for (let i = 0; i < queue.length; i++) {
                    if (currentMaxProbs[queue[i]] < edgeProb) {
                        queue.splice(i,0,edgeDest);
                        break;
                    }
                }
                if (!queue.includes(edgeDest)) queue.push(edgeDest);
                currentMaxProbs[edgeDest] = edgeProb
            }
             
        }
    
        
        currentNode = queue.shift();
    }
    
    return 0;
};
