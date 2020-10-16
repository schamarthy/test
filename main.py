# script to test reading dictionary in python aded agaon
a_dict= {
    "sha": "6ef917b7f281fd3275c67090f7aeab085f8a5924",
    "node_id": "MDY6Q29tbWl0MTI2MjE2ODM3OjZlZjkxN2I3ZjI4MWZkMzI3NWM2NzA5MGY3YWVhYjA4NWY4YTU5MjQ=",
    "commit": {
      "author": {
        "name": "Santosh Chamarthy",
        "email": "schamart@opentext.com",
        "date": "2018-04-09T12:52:56Z"
      },
      "committer": {
        "name": "Santosh Chamarthy",
        "email": "schamart@opentext.com",
        "date": "2018-04-09T12:52:56Z"
      },
      "message": "Added addmf,changed routes",
      "tree": {
        "sha": "01e1ac78ca73dc27c56186cb01a959a89918c94c",
        "url": "https://api.github.com/repos/schamarthy/mfolio/git/trees/01e1ac78ca73dc27c56186cb01a959a89918c94c"
      },
      "url": "https://api.github.com/repos/schamarthy/mfolio/git/commits/6ef917b7f281fd3275c67090f7aeab085f8a5924",
      "comment_count": 0,
      "verification": {
        "verified": 'false',
        "reason": "unsigned",
        "signature": 'null',
        "payload": 'null'
      }
    },
    "url": "https://api.github.com/repos/schamarthy/mfolio/commits/6ef917b7f281fd3275c67090f7aeab085f8a5924",
    "html_url": "https://github.com/schamarthy/mfolio/commit/6ef917b7f281fd3275c67090f7aeab085f8a5924",
    "comments_url": "https://api.github.com/repos/schamarthy/mfolio/commits/6ef917b7f281fd3275c67090f7aeab085f8a5924/comments",
    "author": 'null',
    "committer": 'null',
    "parents": [
      {
        "sha": "f2548be878115f753ae0907d9886ec9296071187",
        "url": "https://api.github.com/repos/schamarthy/mfolio/commits/f2548be878115f753ae0907d9886ec9296071187",
        "html_url": "https://github.com/schamarthy/mfolio/commit/f2548be878115f753ae0907d9886ec9296071187"
      }
    ]
  }

for key in a_dict:
  #Testing commit for pyex 
  if key == 'commit':
    print (a_dict[key])