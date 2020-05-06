import requests

headers = {"Authorization": "token <GITHUB_TOKEN>"}


def run_query(query): # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

        
# The GraphQL query (with a few aditional bits included) itself defined as a multi-line string.       
query = """
{
  repository(name: <REPO_NAME>, owner: <OWNER>) {
    pullRequest(number: <PR_NUMBER>) {
      commits(last: 1) {
        nodes {
          commit {
            status {
              state
              contexts {
                context
                description
                state
              }
            }
          }
        }
      }
    }
  }
}
"""

result = run_query(query) # Execute the query
print(result)
