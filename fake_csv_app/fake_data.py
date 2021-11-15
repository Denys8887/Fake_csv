from faker import Faker

faker = Faker()


def get_fake_data(column_type, from_value=None, to_value=None):
    if column_type == 'Full name':
        return faker.name()
    if column_type == 'Email':
        return faker.email()
    if column_type == 'Phone number':
        return faker.phone_number()
    if column_type == 'Job':
        return faker.job()
    if column_type == 'Integer':
        if from_value and to_value:
            return faker.pyint(min_value=min(from_value, to_value), max_value=max(from_value, to_value))
        if from_value:
            return faker.pyint(min_value=from_value, max_value=9999999999)
        if to_value:
            return faker.pyint(min_value=0, max_value=to_value)
        return faker.random_int()
    if column_type == 'Company':
        return faker.company()
