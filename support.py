import wolframalpha
import wikipedia


def wf (data):
	client = wolframalpha.Client("API KEY")
	res = client.query(data)
	ans = next(res.results).text
	print(ans)
	return ans

def wk (data):
	res=wikipedia.summary(data,sentence=2)
	print(res)
	return res
