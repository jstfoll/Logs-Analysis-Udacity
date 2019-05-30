import psycopg2
DB_NAME = "news"
query1 = "select title,views from article_view limit 3"
query2 = """select authors.name,sum(article_view.views) as views from
article_view,authors where authors.id = article_view.author
group by authors.name order by views desc"""
query3 = "select * from error_view where \"Percent Error\" > 1"

query1_result = dict()
query1_result['title'] = "\n1. The Three most popular articles all time:\n"

query2_result = dict()
query2_result['title'] = """\n2. The most popular article authors
all time are:\n"""

query3_result = dict()
query3_result['title'] = "\n3. Days with more than 1% :\n"

def get_query_result(query):
    db = psycopg2.connect(database=DB_NAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


def print_query_results(query_result):
    print (query_result['title'])
    for result in query_result['results']:
        print ('\t' + str(result[0]) + ' = ' + str(result[1]) + ' views')


def print_error_query_results(query_result):
    print (query_result['title'])
    for result in query_result['results']:
        print ('\t' + str(result[0]) + ' = ' + str(result[1]) + ' %')



query1_result['results'] = get_query_result(query1)
query2_result['results'] = get_query_result(query2)
query3_result['results'] = get_query_result(query3)

print_query_results(query1_result)
print_query_results(query2_result)
print_error_query_results(query3_result)
