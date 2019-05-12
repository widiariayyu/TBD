from nltk.corpus import stopwords


filename = "corpus/1.txt"
with open(filename, 'r') as myfile:
  data = myfile.read()
special_char = ['!','@','?','-','.',',','"',';','—',"'",'"','“','’','”']
remove_character = data
for char in special_char:
  remove_character = remove_character.replace(char, "")

remove_split_line = ' '.join(remove_character.splitlines())
remove_dbl_space = remove_split_line.replace('  ', ' ')
while '  ' in remove_dbl_space:
    remove_dbl_space = remove_dbl_space.replace('  ', ' ')
lowercase = remove_dbl_space.lower()
words = lowercase.split(' ')
i = 0
k = 0
count_word = len(words)
token = []
stemming = []
type_freq = []

for k in range(count_word):
    token.append(0)

k = 0

for word in words:
    if word not in token:
        token[i] = word
        i += 1

for i in range(count_word):
    if 0 in token:
        token.remove(0)

token.sort()
type = []
type2 = []
stopWords = set(stopwords.words('english'))
for w in token:
    if w not in stopWords:
        type.append(w)
        type2.append(w)

count_type = len(type)
for k in range(count_type):
  type_freq.append(0)

i = 0
for a_type in type:
    for word in words:
        if a_type == word:
            type_freq[i] += 1
    i += 1
