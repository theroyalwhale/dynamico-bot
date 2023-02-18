
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

