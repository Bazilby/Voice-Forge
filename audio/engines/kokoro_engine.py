from kokoro import KPipeline

_pipeline = None

# initialise kokoro
def get_pipeline():

    global _pipeline

    if _pipeline is None:
        _pipeline = KPipeline(lang_code="a")

    return _pipeline

# check kokoro is working
def check_kokoro():

    try:
        pipeline = get_pipeline()

        if pipeline :
            return {
                "name": " KOKORO ENGINE",
                "status": "OK"
            }

    except Exception as kokoroError:
        return {
            "name": "KOKORO ENGINE",
            "status": "FAIL",
            "error": str(kokoroError) 
        }