# Hospital-CMS-for-Covid-19

# query set documentation

https://docs.djangoproject.com/en/3.1/ref/models/querysets/

# The Python code to populate the floor and rooms in python shell without the use of admin panel
          
          from accounts.models import Room


          def roomcreate(floor):
            lower_limit="01"
            upper_limit="07"

            with_string_LL=str(floor)+lower_limit
            with_string_UL=str(floor)+upper_limit

            UL=int(with_string_UL)
            LL=int(with_string_LL)
            for room in range(LL,UL):
              floor_no=floor
              room_no=room
              room=Room(floor_no=floor_no,room_no=room_no)
              room.save()

          roomcreate(1)
          roomcreate(2)
          roomcreate(3)
          roomcreate(4)
