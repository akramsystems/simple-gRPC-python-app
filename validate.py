class Error(ValueError):
    def __init__(self, field, reason):
        self.feild = field
        self.reason = reason
    
def start_request(request):
    if not request.driver_id:
        raise Error('driver_id', 'missing')
    #TODO Validate other fields