FEED_TYPES = {
    # From Custom_User:
    "REGISTER": 1,                  # 1-/api/users/register/
    "REGISTER_FACEBOOK": 2,         # 2-/api/users/registerfb/
    "REGISTER_TWITTER": 3,          # 3-/api/users/registertwitter/
    "UPDATE_BIKER": 4,              # 4-/api/users/updatebiker/
    "UPDATE_SETTINGS": 5,           # 5-/api/users/updatesetting/
    "UPDATE_AVATAR": 6,             # 6-/api/users/uploadavatar/

    # From Garage:
    "ADD_BICYCLE": 7,               # 7-/api/garage/addbicycle/
    "UPDATE_BICYCLE": 8,            # 8-/api/garage/updatebicycle/<pk>/
    "DELETE_BICYCLE": 9,            # 9-/api/garage/delbicycle/<pk>/
    "ADD_MOTORCYCLE": 10,           # 10-/api/garage/addmotorcycle/
    "UPDATE_MOTORCYCLE": 11,        # 11-/api/garage/updatemotorcycle/<pk>/
    "DELETE_MOTORCYCLE": 12,        # 12-/api/garage/delmotorcycle/<pk>/

    # From Ride:
    "START_RIDE": 13,               # 13-/api/ride/startride/
    "END_RIDE": 14,                 # 14-/api/ride/endride/

    # From Places:
    "ADD_PLACE": 15,                # 15-/api/places/addnewplace/
    "DELETE_PLACE": 16,             # 16-/api/places/deleteplace/<pk>/
    "UPDATE_PLACE": 17,             # 17-/api/places/updateplace/<pk>/

    # From Schedule Ride:
    "ADD_SCHEDULE_RIDE": 18,        # 18-/api/schedule_ride/addnewscheduleride/
    "DELETE_SCHEDULE_RIDE": 19,     # 19-/api/schedule_ride/deletescheduleride/<pk>/
    "UPDATE_SCHEDULE_RIDE": 20,     # 20-/api/schedule_ride/updatescheduleride/<pk>/
    "ADD_REQUEST": 21,              # 21-/api/schedule_ride/addreq/
    "ACCEPT_REQUEST": 22,           # 22-/api/schedule_ride/acceptreq/<pk>/
    "IGNORE_REQUEST": 23,           # 23-/api/schedule_ride/ignorereq/<pk>/
    "CANCEL_REQUEST": 24,           # 24-/api/schedule_ride/cancelreq/<pk>/
    "CANCEL_JOINING": 25,           # 25-/api/schedule_ride/canceljoining/<pk>/
}
