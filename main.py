from piplapis.search import SearchAPIRequest, SearchAPIError

PIPL_KEY = ''

def run_request(data):
    request = SearchAPIRequest(**data, api_key="BUSINESS-PREMIUM-DEMO-mrj134eaxoapqgdjau16fj9c")
    try:
        response = request.send()
        return response
    except SearchAPIError as e:
        print(e.http_status_code, e)
    return None


def print_person(p):
    print('Photo:', p.image.get_thumbnail_url(200, 100, zoom_face=True, favicon=False) if p.image else 'n/a')
    print('Name:', p.name if p.name else 'n/a')
    print('EMain:', p.email if p.email else 'n/a')
    print('Username:', p.username if p.username else 'n/a')
    print('Address:', p.address if p.address else 'n/a')
    print('Education:', p.education if p.education else 'n/a')
    print('Jobs:', ", ".join(map(str, p.person.jobs)) if p.person.jobs else 'n/a')
    print('Relationships:', ", ".join(map(str, p.person.relationships)) if p.image else 'n/a')


def main():
    data = {}
    params = ['first_name', 'last_name', 'middle name', 'age', 'city', 'phone', 'email', 'work', 'username']
    for i in params:
        x = input("Tell us the %s" % i)
        if len(x) > 0 and x.strip() != '':
            data[i] = x
    res = run_request(data)
    res.possible_persons


if __name__ == '__main__':
    a = (run_request({"first_name": "Petr", "email": "bardin.petr@gmail.com"}))
    main()
