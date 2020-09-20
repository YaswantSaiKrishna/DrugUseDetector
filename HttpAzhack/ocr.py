from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials
from PIL import Image
import time
import os

def ocr1(img):

    #Cognitive Services endpoint and key
    cog_key = '<Your Primary Key here>'                     #Paste your primary key here
    cog_endpoint = '<Endpoint url here>'  #Paste your endpoint here

    # Get a client for the computer vision service
    computervision_client = ComputerVisionClient(cog_endpoint, CognitiveServicesCredentials(cog_key))

    # Submit a request to read printed text in the image and get the operation ID
    try:
        recognize_handw_results = computervision_client.read(img,raw=True)
    except Exception as e:
        return str(e)

    operation_location_remote = recognize_handw_results.headers["Operation-Location"]
    operation_id = operation_location_remote.split("/")[-1]
                                                            
    while True:
        get_handw_text_results = computervision_client.get_read_result(operation_id)
        if get_handw_text_results.status not in ['notStarted', 'running']:
            break
        time.sleep(1)

    if get_handw_text_results.status == OperationStatusCodes.succeeded:
        res = []
        for text_result in get_handw_text_results.analyze_result.read_results:
            for line in text_result.lines:
                res.append(str(line.text))

    if res != []:
        res = str(" ".join(res)) #Result of OCR
    else:
        res = None
                                                                            
    return res
