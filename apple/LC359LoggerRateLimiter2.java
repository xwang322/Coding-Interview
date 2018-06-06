class Logger {
    private Map<String, Integer> hm;
    public Logger() {
        hm = new HashMap<>();
    }
    public boolean shouldPrintMessage(int timestamp, String message) {
        if (!hm.containsKey(message) || (hm.containsKey(message) && hm.get(message) <= timestamp - 10)) {
            hm.put(message, timestamp); 
            return true;
        } else {
            return false;
        }
    }
}
/**
 * Your Logger object will be instantiated and called as such:
 * Logger obj = new Logger();
 * boolean param_1 = obj.shouldPrintMessage(timestamp,message);
 */