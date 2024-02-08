(base) marcusmbpro@Marcuss-Work-Macbook-Pro Subgrounds % python subgrounds-cookbook.py
Traceback (most recent call last):
File "/Users/marcusrein_1/Desktop/Projects/Subgrounds/subgrounds-cookbook.py", line 17, in <module>
x = sg.query_df([
^^^^^^^^^^^^^
File "/Users/marcusrein_1/anaconda3/lib/python3.11/site-packages/subgrounds/client/sync.py", line 288, in query_df
json_data = self.query_json(fpaths, pagination_strategy=pagination_strategy)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/Users/marcusrein_1/anaconda3/lib/python3.11/site-packages/subgrounds/client/sync.py", line 186, in query_json
data = self.execute(req, pagination_strategy)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/Users/marcusrein_1/anaconda3/lib/python3.11/site-packages/subgrounds/client/sync.py", line 120, in execute
data = self.\_fetch(
^^^^^^^^^^^^
File "/Users/marcusrein_1/anaconda3/lib/python3.11/site-packages/subgrounds/client/sync.py", line 429, in \_fetch
resp.raise_for_status()
File "/Users/marcusrein_1/anaconda3/lib/python3.11/site-packages/httpx/\_models.py", line 749, in raise_for_status
raise HTTPStatusError(message, request=request, response=self)
httpx.HTTPStatusError: Server error '504 Gateway Timeout' for url 'https://api.playgrounds.network/v1/proxy/deployments/id/QmQBvtHaTS9MftEWYTSmbbmPqzXtMpgZRidivvEaELSKsc'
For more information check: https://httpstatuses.com/504
(base) marcusmbpro@Marcuss-Work-Macbook-Pro Subgrounds % python subgrounds-cookbook.py
Traceback (most recent call last):
File "/Users/marcusrein_1/Desktop/Projects/Subgrounds/subgrounds-cookbook.py", line 17, in <module>
x = sg.query_df([
^^^^^^^^^^^^^
File "/Users/marcusrein_1/anaconda3/lib/python3.11/site-packages/subgrounds/client/sync.py", line 288, in query_df
json_data = self.query_json(fpaths, pagination_strategy=pagination_strategy)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/Users/marcusrein_1/anaconda3/lib/python3.11/site-packages/subgrounds/client/sync.py", line 186, in query_json
data = self.execute(req, pagination_strategy)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/Users/marcusrein_1/anaconda3/lib/python3.11/site-packages/subgrounds/client/sync.py", line 120, in execute
data = self.\_fetch(
^^^^^^^^^^^^
File "/Users/marcusrein_1/anaconda3/lib/python3.11/site-packages/subgrounds/client/sync.py", line 442, in \_fetch
raise GraphQLError(raw_data.get("errors", "Unknown Error(s) Found"))
subgrounds.errors.GraphQLError: [{'message': 'bad indexers: [Unavailable(no status), BadResponse(500)]'}]
(base) marcusmbpro@Marcuss-Work-Macbook-Pro Subgrounds % python subgrounds-cookbook.py
Traceback (most recent call last):
File "/Users/marcusrein_1/Desktop/Projects/Subgrounds/subgrounds-cookbook.py", line 7, in <module>
seaport = sg.load_subgraph(
^^^^^^^^^^^^^^^^^
File "/Users/marcusrein_1/anaconda3/lib/python3.11/site-packages/subgrounds/client/sync.py", line 78, in load_subgraph
return self.load(url, save_schema, cache_dir, True)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/Users/marcusrein_1/anaconda3/lib/python3.11/site-packages/subgrounds/client/sync.py", line 54, in load
data = self.\_fetch(url, {"query": query})
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/Users/marcusrein_1/anaconda3/lib/python3.11/site-packages/subgrounds/client/sync.py", line 442, in \_fetch
raise GraphQLError(raw_data.get("errors", "Unknown Error(s) Found"))
subgrounds.errors.GraphQLError: [{'message': 'bad indexers: [Unavailable(no status), BadResponse(500)]'}]
(base) marcusmbpro@Marcuss-Work-Macbook-Pro Subgrounds % python subgrounds-cookbook.py
Traceback (most recent call last):
File "/Users/marcusrein_1/Desktop/Projects/Subgrounds/subgrounds-cookbook.py", line 17, in <module>
query = sg.query_df([
^^^^^^^^^^^^^
File "/Users/marcusrein_1/anaconda3/lib/python3.11/site-packages/subgrounds/client/sync.py", line 288, in query_df
json_data = self.query_json(fpaths, pagination_strategy=pagination_strategy)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/Users/marcusrein_1/anaconda3/lib/python3.11/site-packages/subgrounds/client/sync.py", line 186, in query_json
data = self.execute(req, pagination_strategy)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/Users/marcusrein_1/anaconda3/lib/python3.11/site-packages/subgrounds/client/sync.py", line 120, in execute
data = self.\_fetch(
^^^^^^^^^^^^
File "/Users/marcusrein_1/anaconda3/lib/python3.11/site-packages/subgrounds/client/sync.py", line 429, in \_fetch
resp.raise_for_status()
File "/Users/marcusrein_1/anaconda3/lib/python3.11/site-packages/httpx/\_models.py", line 749, in raise_for_status
raise HTTPStatusError(message, request=request, response=self)
httpx.HTTPStatusError: Server error '504 Gateway Timeout' for url 'https://api.playgrounds.network/v1/proxy/deployments/id/QmQBvtHaTS9MftEWYTSmbbmPqzXtMpgZRidivvEaELSKsc'
For more information check: https://httpstatuses.com/504
(base) marcusmbpro@Marcuss-Work-Macbook-Pro Subgrounds % python subgrounds-cookbook.py
Traceback (most recent call last):
File "/Users/marcusrein_1/Desktop/Projects/Subgrounds/subgrounds-cookbook.py", line 7, in <module>
seaport = sg.load_subgraph(
^^^^^^^^^^^^^^^^^
File "/Users/marcusrein_1/anaconda3/lib/python3.11/site-packages/subgrounds/client/sync.py", line 78, in load_subgraph
return self.load(url, save_schema, cache_dir, True)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/Users/marcusrein_1/anaconda3/lib/python3.11/site-packages/subgrounds/client/sync.py", line 54, in load
data = self.\_fetch(url, {"query": query})
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/Users/marcusrein_1/anaconda3/lib/python3.11/site-packages/subgrounds/client/sync.py", line 442, in \_fetch
raise GraphQLError(raw_data.get("errors", "Unknown Error(s) Found"))
subgrounds.errors.GraphQLError: [{'message': 'bad indexers: [Unavailable(no status), BadResponse(500)]'}]
(base) marcusmbpro@Marcuss-Work-Macbook-Pro Subgrounds % python subgrounds-cookbook.py
Traceback (most recent call last):
File "/Users/marcusrein_1/Desktop/Projects/Subgrounds/subgrounds-cookbook.py", line 7, in <module>
seaport = sg.load_subgraph(
^^^^^^^^^^^^^^^^^
File "/Users/marcusrein_1/anaconda3/lib/python3.11/site-packages/subgrounds/client/sync.py", line 78, in load_subgraph
return self.load(url, save_schema, cache_dir, True)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/Users/marcusrein_1/anaconda3/lib/python3.11/site-packages/subgrounds/client/sync.py", line 54, in load
data = self.\_fetch(url, {"query": query})
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/Users/marcusrein_1/anaconda3/lib/python3.11/site-packages/subgrounds/client/sync.py", line 442, in \_fetch
raise GraphQLError(raw_data.get("errors", "Unknown Error(s) Found"))
subgrounds.errors.GraphQLError: [{'message': 'bad indexers: [Unavailable(no status), BadResponse(500)]'}]
(base) marcusmbpro@Marcuss-Work-Macbook-Pro Subgrounds % python subgrounds-cookbook.py
name symbol totalRevenueETH creatorRevenueETH marketplaceRevenueETH
0 Otherdeed OTHR 4764.206871 2792.584336 1971.622535
1 BoredApeYachtClub BAYC 4675.914027 1930.741534 2745.172493
2 Art Blocks BLOCKS 4253.176024 3001.779380 1251.396644
3 MutantApeYachtClub MAYC 3163.635302 1321.867559 1841.767742
4 SewerPass SEWER 2771.745374 1868.150074 903.595300
... ... ... ... ... ...
996 DigiDaigakuSuperVillainPotions DIDSVP 20.684772 15.566630 5.118142
997 TransparentPowers TP 20.664563 15.032616 5.631947
998 Old Rock OR 20.661474 13.145433 7.516041
999 CF EchoStone ECHOSTONE 20.634824 14.473165 6.161659
1000 Pods POD 20.581454 13.036476 7.544978

[1001 rows x 5 columns]
(base) marcusmbpro@Marcuss-Work-Macbook-Pro Subgrounds %
