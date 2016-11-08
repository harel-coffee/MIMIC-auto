from nltk import FreqDist
import sys
MIMIC_PATH = 'MIMIC3/MIMIC_PREPROCESSED'


def mimic_doc_yielder(mimic_path):
    for line in open(mimic_path):
        line = line.split('|')#mimic 3 |, mimic 2 \t
        codes = line[0].split()
        text = (' '.join(line[1:])).split()
        yield codes, text

def write_fd_to_file(fd, file_name):
    with open(file_name, 'w') as fp:
       # keys = fd.keys()
       # keys.sort(key=lambda x: fd[x])
        for t in fd.most_common():#keys:
            fp.write(str(t[0]) + ' ' + str(t[1]) + '\n')


if __name__ == '__main__':
    tokens_fd = FreqDist()
    tokens_doc_fd = FreqDist()
   

    for doc in  mimic_doc_yielder(sys.argv[1]):
        tokens_set = set()

        for word in doc[1]:#0 for codes, 1 for tokens
            tokens_fd[word] += 1
            tokens_set.add(word)
        print tokens_set
        print '*'*100
        tokens_doc_fd[len(tokens_set)] += 1
    

    write_fd_to_file(tokens_fd,'tokens_count_global')
    write_fd_to_file(tokens_doc_fd, 'tokens_count_doc')
    write_fd_to_file(FreqDist(tokens_fd.values()),'tokens_freq_dist')

