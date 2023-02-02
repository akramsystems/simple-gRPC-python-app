import rides_pb2 as pb # import the generated code

print(pb.POOL)
print(pb.RideType.Name(pb.POOL)) # Name
print(pb.RideType.Value('REGULAR')) # Value

request = pb.StartRequest(
    car_id=1,
    driver_id='driver1',
    passenger_ids=['passenger1', 'passenger2'],
    type=pb.POOL,
)

print(request) # Print the message

