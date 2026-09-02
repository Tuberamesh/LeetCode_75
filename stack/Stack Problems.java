package stack;

//problem name: Remove All Adjacent Duplicates In String
//time complexity: O(n)
//space complexity: O(n)
class Solution {
    public String removeStars(String s) {

        Stack<Character> stack = new Stack<>();

        for (char ch : s.toCharArray()) {

            if (ch == '*') {
                stack.pop();
            } else {
                stack.push(ch);
            }
        }

        StringBuilder ans = new StringBuilder();

        for (char ch : stack) {
            ans.append(ch);
        }

        return ans.toString();
    }
}


//problem name: Asteroid Collision
//time complexity: O(n)
//space complexity: O(n)
class Solution {
    public int[] asteroidCollision(int[] asteroids) {

        Stack<Integer> st = new Stack<>();

        for (int ast : asteroids) {

            while (!st.isEmpty() && st.peek() > 0 && ast < 0) {

                if (st.peek() < Math.abs(ast)) {
                    st.pop();

                } else if (st.peek() == Math.abs(ast)) {
                    st.pop();
                    ast = 0;
                    break;

                } else {
                    ast = 0;
                    break;
                }
            }

            if (ast != 0) {
                st.push(ast);
            }
        }

        int[] result = new int[st.size()];

        for (int i = 0; i < st.size(); i++) {
            result[i] = st.get(i);
        }

        return result;
    }
}