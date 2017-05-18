import re

sample = 'http://testserver/campaign/2696/purchase/1381?asdkjalsd'
wrong_sample = "asdklajsdlkjasldkjasldkjaslkdjqlkwjelkasd"
pattern = '(\S+campaign\/\d+\/purchase\/\d+)'
p = re.compile(pattern)

result = p.search(sample)
print(result)
wrong_result = p.search(wrong_sample)
print(wrong_result)