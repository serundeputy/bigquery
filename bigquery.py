from google.cloud import bigquery

client = bigquery.Client()

query_job = client.query(
    """
    SELECT
      CONCAT(
        'https://stackoverflow.com/questions/',
        CAST(id as STRING)) as url,
      view_count
    FROM `bigquery-public-data.stackoverflow.posts_questions`
    WHERE tags like '%lando%'
    ORDER BY view_count DESC
    LIMIT 10"""
)

# Waits for job to complete.
results = query_job.result()

total = 0
for row in results:
    total += row.view_count
    print("{} : {} views".format(row.url, row.view_count))

print("Total: {}".format(total))
