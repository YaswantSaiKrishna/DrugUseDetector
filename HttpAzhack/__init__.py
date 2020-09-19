import logging

import json

import azure.functions as func

from . import ocr

from . import med7nlp

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    image = req.params.get('image')
    if not image:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            image = req_body.get('image')

    if image:
        ocrText = ocr.ocr1(image)
        if ocrText != None:
            nplmodel = med7nlp.med7nlp1(ocrText)
            if nplmodel != None:
                x = {"text" : nplmodel}
                return func.HttpResponse(json.dumps(x))
            else:
                return func.HttpResponse("The drug can't be extracted from the picture please insert a clear picture from another angle")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a image link in the query string or in the request body for a personalized response.",
             status_code=200
        )
