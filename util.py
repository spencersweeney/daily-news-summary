# Util functions
import string


def similarity_title(str1, str2) -> int:
    clean_text1 = ''.join([char.lower() for char in str1 if char not in string.punctuation])
    clean_text2 = ''.join([char.lower() for char in str2 if char not in string.punctuation])

    words_in_str1 = set(clean_text1.split())
    words_in_str2 = set(clean_text2.split())

    union = words_in_str1 & words_in_str2

    return int((len(union) / min(len(words_in_str1), len(words_in_str2))) * 100)

# print(similarity_title('Hello World', 'Hello World'))
# print(similarity_title('Hello World', 'hello world'))
# print(similarity_title('Hello World', 'Hello World Spencer'))
#
# print(similarity_title('Today Russia attacked the Ukraine, by attacking Kyiv',
#                  'The War in Russia has escalated with Russia bombing Kyiv'))
#
# print(similarity_title('Zelensky says Ukraine is ready to Discuss Neutrality',
#                  'Ukraine, Russia prepare to talk as Missiles Hit Cities'))
