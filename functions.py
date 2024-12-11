from requests import get;

def findNonWords(*words):
   '''
   Helper function for 'poem' function. This takes in a bunch of words and returns words that does not exist in the api (see below).
   '''
   nonWordList = [];

   for i in words:
      api = get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{i}"); #source: https://dictionaryapi.dev/. No API key needed.
      nonWordList = [*nonWordList, i] if (type(api.json()).__name__ == 'dict') else nonWordList;
   return False if (len(nonWordList) == 0) else nonWordList;

def poem(noun: str, adjective: str):
   '''
   This is the main function that incorporates the helper function, findNonWords (above).
   '''
   try:
      if findNonWords(noun, adjective): raise ValueError();
      return f"{noun} are red, violets are blue. Monty Python is {adjective}, Woo hoo!";
   except ValueError:
      print(ValueError);
      return f"The following are not recognized words: {findNonWords(noun, adjective)}.";
   except:
      return 'Some other error occurred.';