from piplapis.search import SearchAPIRequest, SearchAPIError

PIPL_KEY = "BUSINESS-PREMIUM-DEMO-mrj134eaxoapqgdjau16fj9c"


def run_request(data):
    request = SearchAPIRequest(**data, api_key=PIPL_KEY)
    try:
        response = request.send()
        return response
    except SearchAPIError as e:
        print(e.http_status_code, e)
    return None


def print_person(p):
    ks = p.to_dict().keys()
    print('Name:', p.names[0].display if 'names' in ks else 'n/a')
    print('EMail:', p.emails if 'emails' in ks else 'n/a')
    print('Gender:', p.gender if 'gender' in ks else 'n/a')
    print('Username:', ", ".join(map(lambda x: str(x.display), p.usernames)) if 'usernames' in ks else 'n/a')
    print('Phone:', ", ".join(map(lambda x: str(x.display), p.phones)) if 'phones' in ks else 'n/a')
    print('Address:', ", ".join(map(lambda x: str(x.display), p.addresses)) if 'addresses' in ks else 'n/a')
    print('Education:', ", ".join(map(lambda x: str(x.display), p.educations)) if 'educations' in ks else 'n/a')
    print('Jobs:', ", ".join(map(lambda x: str(x.display), p.jobs)) if 'jobs' in ks else 'n/a')
    print('Relationships:',
          ", ".join(map(str, p.relationships)) if 'relationships' in ks else 'n/a')
    print('Photo:',
          p.image.get_thumbnail_url(200, 100, zoom_face=True, favicon=False) if 'image' in ks else 'n/a')


def main():
    print("""
    Hello!
    You are running people search program.
    We need to know some about person.
    You can fill only some parameters, other can be blank.
    """)
    data = {}
    params = ['first_name', 'last_name', 'middle name', 'age', 'city', 'phone', 'email', 'work', 'username']
    for i in params:
        x = input("Tell us the %s: " % i)
        if len(x) > 0 and x.strip() != '':
            data[i] = x
    print("\nRunning request...")
    res = run_request(data)
    l = len(res.possible_persons)
    print("\n\nWe found %d persons\n\n" % l)
    for i in range(l):
        print('\nPrinting person #%d' % i)
        print_person(res.possible_persons[i])
        print('#' * 20 + '\n')


if __name__ == '__main__':
    main()
