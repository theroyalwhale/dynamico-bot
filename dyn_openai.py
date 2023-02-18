
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

def imageVar(image,n):
  response = openai.Image.create_variation(
    image=open(image, "rb"),
    n=n,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  return image_url
