from urllib.request import urlopen
import sys
# import Modularity as mod


# "http://sixty-north.com/c/t.txt"
def Get_story_word(url):
    story = urlopen(url)
    story_word = []    
    for line in story:
        line_words = line.decode('utf8').split()
        for  word in line_words:
            story_word.append(word)
    story.close()
    return story_word


def print_item(item):
    for word in item:
        print(word)


def main():
    url=sys.argv[1]
    # words=Get_story_word(url)
    # print_item(words)

    
if __name__ == "__main__":
    main()
# print_story_word()
# mod.display_nth_root(16,2)
