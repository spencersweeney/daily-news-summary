# Util functions
import smtplib
import string
from email.message import EmailMessage
from group_of_articles import GroupOfArticles


def similarity(str1: str, str2: str) -> int:
    """
    find the similarity of two strings (phrases)
    :param str1: the first string (phrase)
    :param str2: the second string (phrase)
    :return: a number between 1 and 100 representing how similar the two strings are
    """
    clean_text1 = ''.join([char.lower() for char in str1 if char not in string.punctuation])
    clean_text2 = ''.join([char.lower() for char in str2 if char not in string.punctuation])

    with open('/Users/spencersweeney/Desktop/EECE2140/daily_news_summary/common_words.txt') as f:
        common_words = []
        for line in f:
            common_words.append(line.strip('\n'))

    words_in_str1 = clean_text1.split()
    words_in_str2 = clean_text2.split()

    remove_common_words1 = set([word for word in words_in_str1 if word not in common_words])
    remove_common_words2 = set([word for word in words_in_str2 if word not in common_words])

    union = remove_common_words1 & remove_common_words2

    return int((len(union) / max(len(remove_common_words1), len(remove_common_words2))) * 100)


def send_email(receiver: str, articles: GroupOfArticles):
    """
    sends an email to the given receiver with the message being the given articles
    :param receiver: the person to send the email to
    :param articles: the articles to send in the email
    :return: nothing void function
    """
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login('dailynewssummarizer@gmail.com', 'EECE2140')

        msg = EmailMessage()
        msg['Subject'] = 'Your Daily News Summary'
        msg['From'] = 'dailynewssummarizer@gmail.com'
        msg['To'] = receiver
        msg.set_content(str(articles))

        smtp.send_message(msg)
