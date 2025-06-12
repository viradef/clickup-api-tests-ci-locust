from faker import Faker

fake = Faker()
fake_ua = Faker("uk_UA")

update_comment_text_cases = [
    (fake.sentence(nb_words=6), 200),
    (fake_ua.sentence(nb_words=6), 200),
    (fake.text(max_nb_chars=255), 200),
    (f"{fake.word()} {fake.random_number(digits=5)}", 200),
]