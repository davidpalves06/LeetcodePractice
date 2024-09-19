import java.util.HashSet;
import java.util.Set;

public class LeetCodeDistributeCandies {
    public int distributeCandies(int[] candyType) {
        Set<Integer> foundTypes = new HashSet<>();
        int count = 0;
      for (int type : candyType) {
        if (foundTypes.contains(type)) continue;
        foundTypes.add(type);
        count++;
        if (count == candyType.length / 2) return count;
      }
        return count;
    }
}
