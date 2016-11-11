"""
http://puzzles.bostonpython.com/poetry.html
"""
from collections import Counter
import string

poem = '''a narrow fellow in the grass
occasionally rides;
you may have met him, did you not,
his notice sudden is.

the grass divides as with a comb,
a spotted shaft is seen;
and then it closes at your feet
and opens further on.

he likes a boggy acre,
a floor too cool for corn.
yet when a child, and barefoot,
i more than once, at morn,

have passed, i thought, a whip-lash
unbraiding in the sun,
when, stooping to secure it,
it wrinkled, and was gone.

several of nature's people
i know, and they know me;
i feel for them a transport
of cordiality;

but never met this fellow,
attended or alone,
without a tighter breathing,
and zero at the bone.'''

counter = Counter(poem.strip(" ,-"))


riddle = [56,38,44,56,29]
test_riddle = [1,56,7,29,42]


maping = {i:poem.count(i) for i in string.ascii_lowercase}
c = {v:k for k,v in maping.items() if v in test_riddle }

print(c)
ans = "".join([c[i] for i in test_riddle])
print(ans)

