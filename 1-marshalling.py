import rides_pb2 as pb # import the generated code

# Create a new StartRequest message
request = pb.StartRequest(
    car_id=1,
    driver_id='driver1',
    passenger_ids=['passenger1', 'passenger2']
)
print(request) # Print the message

# region Marshal
data = request.SerializeToString() # Serialize the message to a string
print('type(data):', type(data)) # type(data): <class 'bytes'>
print('size:', len(data)) # size: 35
# endregion

# region Unmarshal
request2 = pb.StartRequest() # Create a new message
request2.ParseFromString(data) # Parse the string into the message
print(request2) # Print the message
# endregion