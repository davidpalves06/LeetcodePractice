import java.util.Arrays;

public class LeetcodeConvert1Dto2DArray {
    public static int[][] construct2DArray(int[] original, int m, int n) {
        int[][] newArray = new int[m][n];

        int currentColumn = 0;
        int currentRow = 0;

        for (int i = 0; i < original.length; i++) {
            if (currentRow == m) {
                return new int[0][0];
            }
            newArray[currentRow][currentColumn] = original[i];
            if (++currentColumn == n) {
                currentColumn = 0;
                currentRow++;
            }
        }

        if (currentColumn != 0 || currentRow != m) {
            return new int[0][0];
        }

        return newArray;
    }

    public static void main(String[] args) {
        System.out.println(2);
    }
}