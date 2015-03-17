import Resource
reload(Resource) #Only import ONCE. Need manually reload to refresh.

#click(Resource.imgOption)
#click(Resource.imgTuyChinh)

def clickOffset(image, x, y):
    t = Pattern(image).targetOffset(x, y)
    click(t)

clickOffset(Resource.imgAmBaoOption, -150, 0)