
import openai
openai.api_key = "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"

def imageGen(prompt,n):
  response = openai.Image.create(
    prompt=prompt,
    n=n,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  return image_url
  