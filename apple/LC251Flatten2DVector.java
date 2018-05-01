public class Vector2D implements Iterator<Integer> {
    int current_row;
    int current_index;
    List<List<Integer>> vec;

    public Vector2D(List<List<Integer>> vec2d) {
        vec = vec2d;
        current_row = 0;
        current_index = 0;
    }

    @Override
    public Integer next() {
        return vec.get(current_row).get(current_index++);
    }

    @Override
    public boolean hasNext() {
        while (current_row < vec.size()) {
            if (current_index < vec.get(current_row).size()) {
                return true;
            } else {
                current_index = 0;
                current_row++;
            }
        }
        return false;
    }
}

/**
 * Your Vector2D object will be instantiated and called as such:
 * Vector2D i = new Vector2D(vec2d);
 * while (i.hasNext()) v[f()] = i.next();
 */
