# Hospital-CMS-for-Covid-19

# query set documentation

https://docs.djangoproject.com/en/3.1/ref/models/querysets/

# The Python code to populate the floor and rooms in python shell without the use of admin panel
          
    from accounts.models import Room
    for floor in range(1,4):
      for room in range(101,107):
        floor_no=floor
        room_no=room
        room=Room(floor_no=floor_no,room_no=room_no)
        room.save()
                    
