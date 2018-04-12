class Solution {
    HashMap<String, List<String>> adjList = new HashMap<>();
    LinkedList<String> route = new LinkedList<>();
    int numTickets = 0;
    int numTicketsUsed = 0;
    
    public List<String> findItinerary(String[][] tickets) {
        if (tickets == null || tickets.length == 0) return route;
        numTickets = tickets.length;
        for (int i = 0; i < tickets.length; ++i) {
            if (!adjList.containsKey(tickets[i][0])) {
                List<String> list = new ArrayList<>();
                list.add(tickets[i][1]);
                adjList.put(tickets[i][0], list);
            } else {
                adjList.get(tickets[i][0]).add(tickets[i][1]);
            }
        }
        for (Map.Entry<String, List<String>> entry : adjList.entrySet()) {
            Collections.sort(entry.getValue());
        }
        
        route.add("JFK");
        dfsRoute("JFK");
        return route;
    }
    
    private void dfsRoute(String v) {
        if (!adjList.containsKey(v)) return;
        List<String> list = adjList.get(v);
        for (int i = 0; i < list.size(); ++i) {
            String neighbor = list.get(i);
            list.remove(i);
            route.add(neighbor);
            numTicketsUsed++;
            dfsRoute(neighbor);
            if (numTickets == numTicketsUsed) return;
            list.add(i, neighbor);
            route.removeLast();
            numTicketsUsed--;
        }
    }
}