import scratchattach as scratch3
from PIL import Image
import urllib.request
import requests, os

def getImgData(url, res, resize):
    imgData = []
    urllib.request.urlretrieve(url, 'img.png')
    orgImg = Image.open('img.png')
    if resize:
        orgImg = orgImg.resize((340, 200))
    orgWidth, orgHeight = orgImg.size
    if res.upper() == 'L':
        img = orgImg.resize((int(orgWidth / 20), int(orgHeight / 20)))
    elif res.upper() == 'H':
        img = orgImg.resize((int(orgWidth / 10), int(orgHeight / 10)))
    img.save('resize.png')
    img = Image.open('resize.png')
    imgData = list(img.getdata())
    width, height = img.size
    for i in imgData:
        val = i
        r = val[0]
        g = val[1]
        b = val[2]
        hex = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        imgData[imgData.index(i)] = hex
    oldImgData = list(imgData)
    imgData.clear()
    prevVal = oldImgData[0]
    count = 1
    for val in oldImgData:
        if prevVal == val:
            count += 1
        else:
            imgData.append(f'{val}/{count}/')
            count = 1
        prevVal = val
    imgData.insert(0, f'{width}/{height}/')
    return imgData


sessId = os.getenv('COOKIE')

session = scratch3.Session(sessId, username='RandomCoder9910')
connScratch = session.connect_cloud('882425161')
clientScratch = scratch3.CloudRequests(connScratch)
connTw = scratch3.TwCloudConnection(project_id='882425161')
clientTw = scratch3.TwCloudRequests(connTw)

def ping():
    print('User is pinging the server')
    return 'pong'

def loadFeaturedProject():
    print('User requested featured projects')
    featuredProjects = []
    temp = scratch3.featured_projects()
    for i in range(0, 5):
        val = temp[i]
        thumb = val['id']
        creator = val['creator']
        title = val['title']
        if len(title) > 20:
            title = title[:22]
            title = title + '...'
        featuredProjects.append(f'{thumb}%{title}%{creator}%')
    return featuredProjects

def loadFeaturedStudios():
    print('User requested featured studios')
    featuredStudios = []
    temp = scratch3.featured_studios()
    for i in range(0, 5):
        val = temp[i]
        thumb = val['id']
        title = val['title']
        if len(title) > 20:
            title = title[:22]
            title = title + '...'
        featuredStudios.append(f'{thumb}%{title}%')
    return featuredStudios

def loadSDS():
    print('User requested SDS')
    SDSprojects = []
    temp = scratch3.design_studio_projects()
    for i in range(0, 5):
        val = temp[i]
        thumb = val['id']
        creator = val['creator']
        title = val['title']
        if len(title) > 20:
            title = title[:22]
            title = title + '...'
        SDSprojects.append(f'{thumb}%{creator}%{title}%')
    return SDSprojects

def loadTopLoved():
    print('User requested top loved')
    topLoved = []
    temp = scratch3.top_loved()
    for i in range(0, 5):
        val = temp[i]
        thumb = val['id']
        creator = val['creator']
        title = val['title']
        if len(title) > 20:
            title = title[:22]
            title = title + '...'
        topLoved.append(f'{thumb}%{creator}%{title}%')
    return topLoved

def loadTopRemixed():
    print('User requested top remixed')
    topRemixed = []
    temp = scratch3.top_remixed()
    for i in range(0, 5):
        val = temp[i]
        thumb = val['id']
        creator = val['creator']
        title = val['title']
        if len(title) > 20:
            title = title[:22]
            title = title + '...'
        topRemixed.append(f'{thumb}%{creator}%{title}%')
    return topRemixed

def loadImg(type, id, res):
    if type == 'B':
        studio = session.connect_studio(id)
        img = studio.image_url
        resize = True
    else:
        project = session.connect_project(id)
        img = project.thumbnail_url
        resize = False
    return getImgData(img, res, resize)

def addFunct(funct):
    clientScratch.add_request(funct)
    clientTw.add_request(funct)


addFunct(ping)
addFunct(loadFeaturedProject)
addFunct(loadFeaturedStudios)
addFunct(loadSDS)
addFunct(loadTopLoved)
addFunct(loadTopRemixed)
addFunct(loadImg)

clientScratch.run(thread=True)
clientTw.run()
