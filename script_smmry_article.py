import json
import os
import time
import requests

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from politico.models import LinkArticle

SM_API_KEY = 'EBD4B92AE5'
SM_LENGTH = 3

# • SM_API_KEY=N	 Required, your API key.
# • SM_URL=X	 Optional, the webpage to summarize.
# • SM_LENGTH=N	 Optional, the number of sentences returned, default 7.
# • SM_KEYWORD_COUNT=N	 Optional, N the number of keywords to return.
# • SM_WITH_BREAK	 Optional, inserts the string [BREAK] between sentences.
# • SM_WITH_ENCODE	 Optional, converts HTML entities to their applicable chars.
# • SM_IGNORE_LENGTH	 Optional, returns summary regardless of quality or length.
# • SM_QUOTE_AVOID	 Optional, sentences with quotations will be excluded.
# • SM_QUESTION_AVOID	 Optional, sentences with question will be excluded.
# • SM_EXCLAMATION_AVOID	 Optional, sentences with exclamation marks will be excluded.
# Here are the possible indexes of the array returned in a JSON array.

# • sm_api_message	 Contains notices, warnings, and error messages.
# • sm_api_character_count	 Contains the amount of characters returned.
# • sm_api_title	 Contains the title when available.
# • sm_api_content	 Contains the summary.
# • sm_api_keyword_array	 Contains top ranked keywords in descending order.
# • sm_api_error	 Contains error code.

articles = LinkArticle.objects.filter(smmry_done=False)[:90 ]

for a in articles:
    response = requests.get(f"https://api.smmry.com/&SM_API_KEY={SM_API_KEY}&SM_LENGTH={SM_LENGTH}&SM_URL={a.link_url}")
    json_data = json.loads(response.text)
    if 'sm_api_error' in json_data:
        print(a.id)
        print(json_data['sm_api_message'])
        print(json_data['sm_api_error'])
    else:
        print(json_data)
        if 'sm_api_title' in json_data:
            a.smmry_title = json_data['sm_api_title']
            print(json_data['sm_api_title'])
        print(json_data['sm_api_content'])
        a.smmry_content = json_data['sm_api_content']
        a.smmry_reduced = json_data['sm_api_content_reduced']
        a.smmry_done = True
        a.save()

    time.sleep(10)


