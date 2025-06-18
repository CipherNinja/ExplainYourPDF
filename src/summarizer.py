import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.luhn import LuhnSummarizer

nltk.data.load("tokenizers/punkt/english.pickle")

def summarize_text(text):
    if not text.strip():
        return "No text to summarize."
    
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LuhnSummarizer()
    summary = summarizer(parser.document, sentences_count=3)
    return " ".join(str(sentence) for sentence in summary)