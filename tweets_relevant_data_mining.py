import re
import matplotlib.pyplot as plt
from plot_tweets_data import tweets
from plot_tweets_data import tweets_data
from tweets_raw_data_mining import word_in_text, prg_langs


def extract_link(text):
        regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
        match = re.search(regex, text)
        if match:
            return match.group()
        return ''

tweets['programming'] = tweets['text'].apply(lambda tweet: word_in_text('programming', tweet))
tweets['tutorial'] = tweets['text'].apply(lambda tweet: word_in_text('tutorial', tweet))
tweets['relevant'] = tweets['text'].apply(lambda tweet: word_in_text('programming', tweet) or word_in_text('tutorial', tweet))
tweets['link'] = tweets['text'].apply(lambda tweet: extract_link(tweet))


if __name__ == '__main__':
    print "Programming tweets:{}".format(len(tweets_data)-tweets['programming'].value_counts()[False])
    print "Tutorial:{}".format(len(tweets_data)-tweets['tutorial'].value_counts()[False])
    rel_tw_count = len(tweets_data)-tweets['relevant'].value_counts()[False]
    print "Relevant tweets:{}".format(rel_tw_count)
    print "**********************"

    rel_tw_python = rel_tw_count-tweets[tweets['relevant'] == True]['python'].value_counts()[False]
    rel_tw_js = rel_tw_count-tweets[tweets['relevant'] == True]['javascript'].value_counts()[False]
    rel_tw_ruby = rel_tw_count-tweets[tweets['relevant'] == True]['ruby'].value_counts()[False]

    print "Relevant python:{}".format(rel_tw_python)
    print "Relevant JS:{}".format(rel_tw_js)
    print "Relevant ruby:{}".format(rel_tw_ruby)
    print "**********************"

    tweets_by_prg_lang = [rel_tw_python, rel_tw_js, rel_tw_ruby]
    x_pos = list(range(len(prg_langs)))
    width = 0.8
    fig, ax = plt.subplots()
    plt.bar(x_pos, tweets_by_prg_lang, width,alpha=1,color='g')
    ax.set_ylabel('Number of tweets', fontsize=15)
    ax.set_title('Ranking: python vs. javascript vs. ruby (Relevant data)', fontsize=10, fontweight='bold')
    ax.set_xticks([p + 0.4 * width for p in x_pos])
    ax.set_xticklabels(prg_langs)
    fig.savefig('plot4.png')

    tweets_relevant = tweets[tweets['relevant'] == True]
    tweets_relevant_with_link = tweets_relevant[tweets_relevant['link'] != '']
    print "Links:"
    print "Pyhton:{}".format(tweets_relevant_with_link[tweets_relevant_with_link['python'] == True]['link'])
    print "__________________"
    print "JS:{}".format(tweets_relevant_with_link[tweets_relevant_with_link['javascript'] == True]['link'])
    print "__________________"
    print "Ruby:{}".format(tweets_relevant_with_link[tweets_relevant_with_link['ruby'] == True]['link'])
