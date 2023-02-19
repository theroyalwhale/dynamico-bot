
import openai
import os

def openKey(n):
  for i in range(1,n+1):
    openai.api_key = os.getenv("openaiKey-"+str(i))


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
