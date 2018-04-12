class DBReplic {
    HashMap<String, String> hm = new HashMap<>();
    Set<DBReplic> replica = new HashSet<>();

    public void set(String key, String value) {
        Queue<DBReplic> q = new LinkedList<>();
        Set<DBReplic> visited = new HashSet<>();
        q.offer(this);
        visited.add(this);
        while (!q.isEmpty()) {
            DBReplic temp = q.poll();
            temp.hm.put(key, value);
            for (DBReplic replicate: temp.replica) {
                if (!visited.contains(replicate)) {
                    q.offer(replicate);
                    visited.add(replicate);
                }
            }
        }
    }

    public String get(String key) {
        return hm.get(key);
    }

    public void replicate(DBReplic db) {
        replica.add(db);
    }
}
