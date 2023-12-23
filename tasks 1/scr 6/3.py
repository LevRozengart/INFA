from collections import Counter
def count_it(s):
    counts = Counter(map(int, s))
    return dict(counts.most_common(3))
print(count_it('123213123123213213'))
