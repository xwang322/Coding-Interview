
/* RandomNumberGenerator.java */
public interface RandomNumberGenerator<T> {
  public T getRandomSample();
}
  
/* Multinomial.java */
public class Multinomial<T> implements RandomNumberGenerator<T> {
  /* Complete this class */
  
  /* Input by a list of (value, probability) pairs*/
  public Multinomial(List<Pair<T, Double>> valueProbPairList) {
    /* Implement this constructor */
  }
}

M = Multinomial([{'a', .7}, {'b', .3}, {'c', .4}]
M = Multinomial([{'a', .0234252}, {'b', .2}, {'c', .07}]
M.getRandomSample() # return 'a', 'b', 'c'


import bisect
import random
class M(object):
    def __init__(self):
        self.range_start = []
        self.boundary = 0
        self.dictionary_list = {}
        self.total = 0

    def Multilnomial(lists):
        if not lists:
            return -1
        dictionary = {}
        lists = sorted(lists, key = lambda x:x[1])
        self.boundary  = 0
        self.total = sum(lists.values())
        for item in lists:
            dictionary[item[0]] = (self.boundary, item[1]+self.boundary)
            self.boundary += item[1]
        self.dictionary_list = sorted(dictionary.iteritem(), key = lambda (k,v):(v,k))
        self.range_start = [item[1][0] for item in self.dictionary_list]

    def getRandomSample():
        answer = ''
        trial = random.uniform(0, self.total)
        found_index = bisect.bisect_left(self.range_start, trial)
        if found_index == len(self.dictionary_list):
            return self.dictionary_list[-1][0]
        return self.diciotnary_list[found_index][0]
