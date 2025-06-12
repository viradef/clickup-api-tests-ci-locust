from faker import Faker

fake_en = Faker()
fake_ua = Faker("uk_UA")

update_comment_text_cases = [
    (fake_en.sentence(nb_words=6), 200),
    (fake_ua.sentence(nb_words=6), 200),
    (fake_en.text(max_nb_chars=255), 200),
    (f"{fake_en.word()} {fake_en.random_number(digits=5)}", 200),
]

def generate_random_sentence():
    return fake_en.sentence()

def generate_comment_payload(comment_text=None, assignee=None, notify_all=True):
    return {
        "comment_text": comment_text or fake_en.sentence(),
        "assignee": assignee,
        "notify_all": notify_all
    }