import click

import requests


@click.command()
def main():
    """
    Newsfeed-This is a new app that gives you all the top headlines in the UK.
    You can access all the top headlines in the uk using this app
    
    """
    pass

#API key of the newapi.org
API_KEY = 'b5593ae03e1b41219a953bafaa7b2dab'

def top_headlines():
    main_url = 'http://newsapi.org/v2/top-headlines?country=uk&apiKey=b5593ae03e1b41219a953bafaa7b2dab'

   
#Top headlines in the uk and in JSON format
json = requests.get('http://newsapi.org/v2/top-headlines?country=uk&apiKey=b5593ae03e1b41219a953bafaa7b2dab').json()
print(json('top_headlines'))


# getting all headlines in a string articles 
top_headlines = top_headlines["articles"]



if __name__ == "__main__":
    main()