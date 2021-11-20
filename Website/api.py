
import uvicorn
import numpy as np
from fastapi import FastAPI, Request, File,UploadFile, Form,HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import PIL.Image as Image
import io
from torchvision.io import read_image
import torchvision.transforms as transforms
import torch
from torchvision import models
from fastapi.staticfiles import StaticFiles
import os


transform = transforms.Compose([
    transforms.Resize([256, 256]),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])


IMAGEDIR = "fastapi-images/"
app=FastAPI()
templates=Jinja2Templates(directory="htmldir")
app.mount("/static",StaticFiles(directory="static"),name="static")



@app.get("/",response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("Home.html",{"request":request})


@app.post("/submitform")
async def handle_form(request: Request, fileass : UploadFile = File(...)):
    try:
        contentassign= await fileass.read()
        print(fileass.content_type)
        if('image' in fileass.content_type):
            image = Image.open(io.BytesIO(contentassign))
            image.save("static/image.png")
            image = read_image("static/image.png")
            image = image.to(torch.float32) / 255.
            image = transform(image)
            print(image.shape)
            image=image[np.newaxis,:,:,:]
            model = models.resnet50(pretrained=True)
            in_features = model.fc.in_features  # Gets the input dimension of the top output layer
            model.fc = torch.nn.Linear(in_features, 2)
            model.load_state_dict(torch.load('model/model',map_location=torch.device('cpu')))
            model.eval()
            pred=model(image)
            pred = torch.argmax(pred, dim=-1)
            if(pred==0):
                animal='cat'
            else:
                animal='dog'
            print(animal)
            return templates.TemplateResponse("image_show.html",{"request":request,"animal":animal})
        else:
            return({"error":"not an image"})
    except:
        raise HTTPException(status_code=520,details="prediction fonction stopped format not supported")
    return({"error":"prediction fonction stopped format not supported"})

if __name__=='__main__':
    port=int(os.environ.get('PORT'))
    uvicorn.run(app,host="127.0.0.1",port=port)