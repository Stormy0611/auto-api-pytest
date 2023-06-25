# /review/{review_id}
# /appointment/{appointment_id}/review
review = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/Review",
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
    },
    "appointment_id": {
      "type": "string",
    },
    "rating": {
      "type": "integer",
    },
    "review": {
      "type": "string",
    },
    "client_id": {
      "type": "string",
    },
    "listing_id": {
      "type": "string",
    },
    "provider_id": {
      "type": "string",
    },
    "created_at": {
      "type": "string",
    },
  },
  "required": [
        "id",
        "appointment_id",
        "rating",
        "client_id",
        "listing_id", 
        "provider_id",
        "created_at"
  ]
}

# /user/review
# /provider/{provider_id}/review
# /listing/{listing_id}/review
get_x_all_review = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/",
  "type": "array",
  "items": review,
}

# /user/photo
url = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/URL",  
  "type": "object",
  "properties": {
      "url": {
          "type": "string"
      }
  },
  "required": [
      'url'
  ]
}

# 
card = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/Card",
  "type": "object",
  "properties": {
      "brand": {
          "type": "string",
      },
      "exp_month": {
          "type": "integer",
      },
      "exp_year": {
          "type": "integer",
      },
      "last4": {
          "type": "string",
      },
  },
  "required": [
      "brand",
      "exp_month",
      "exp_year",
      "last4"
  ]
}

# 
payment_method = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/PaymentMethod",
  "type": "object",
  "properties": {
      "id": {
          "type": "string",
      },
      "card": card
  },
  "required": [
      "id"
  ]
}

# /user/payment_method
get_x_all_payment_method = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/",
  "type": "array",
  "items": payment_method
}

# /provider/account_status
account_status = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/AccountStatus",
  "type": "object",
  "properties": {
      "account_status": {
          "type": "boolean"
      },
  },
  "required": [
          "account_status"
      ]
}

# /provider/account_link
# /provider/add_account
account_link = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/AccountLink",
  "type": "object",
  "properties": {
      "object": {
          "type": "string"
      },
      "created": {
          "type": "integer"
      },
      "expires_at": {
          "type": "integer"
      },
      "url": {
          "type": "string"
      },
  } ,
  "required": [
          "object",
          "created",
          "expires_at",
          "url",
      ]
}

# /user/{user_id}
# /user
# /signup
# /login
user = {
  
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
    },
    "username": {
      "type": ["string", "null"],
    },
    "email": {
      "type": ["string", "null"],
    },
    "user_type": {
      "type": "string",
    },
    "description": {
      "type": ["string", "null"],
    },
    "phone": {
      "type": ["string", "null"],
    },
    "lat": {
      "type": ["number", "null"],
    },
    "lng": {
      "type": ["number", "null"],
    },
    "img_url": {
      "type": ["string", "null"],
    },
    "created_at": {
      "type": "string",
    },
  },
  "required": [
        "id",
        "user_type",
        "created_at",
  ]
}

# /
# /check
# /listing/{listing_id}/availability
# /reset
# /thread/{thread_id}/read
# /notification/{notification_id}/read
# /logout
# DELETE /review/{review_id}
# DELETE /user/payment_method/{payment_method_id}
# DELETE /appointment/{appointment_id}/item/{appointment_item_id}
# DELETE /item/{listing_item_id}
# DELETE /blog/{blog_id}
# DELETE /listing/{listing_id}/schedule/override/{override_id}
# DELETE /bookmark/{bookmark_id}
# DELETE /listing/{listing_id}
# DELETE /listing/{listing_id}/tag/{listing_tag_id}
# DELETE /listing/tag/{user_tag_id}
empty_response = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/EmptyResponse",
  "type": "object",
  "properties": {
  }
}

# /listing/{listing_id}/tag
listing_tag = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/ListingTag",  
  "type": "object",
  "properties": {
      "id": {
          "type": "string"
      },
      "listing_id": {
          "type": "string"
      },
      "tag": {
          "type": "string"
      },
      "tag_id": {
          "type": "string"
      },
      "created_at": {
          "type": "string"
      },
  },
  "required": [
      "id",
      "listing_id",
      "tag",
      "tag_id",
      "created_at",
  ]
}

#
appointment_provider = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/AppointmentProvider",    
  "type": "object",
  "properties": {
      "id": {
          "type": "string"
      },
      "username": {
          "type": "string"
      },
      "distance": {
          "type": "integer"
      },
      "img_url": {
          "type": "string"
      },
  },
  "required": [
      "id",
      "username",
  ]
}

# /listing/{listing_id}
# POST /listing
listing = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/Listing",  
  "type": "object",
  "properties": {
      "id": {
          "type": "string"
      },
      "user_id": {
          "type": "string"
      },
      "title": {
          "type": "string"
      },
      "description": {
          "type": "string"
      },
      "appointment_per_timeslot": {
          "type": "string"
      },
      "timeslot_minutes": {
          "type": "string"
      },
      "tags": {
          "type": "array",
          "items": listing_tag
      },
      "provider": {
          "type": "array",
          "items": appointment_provider
      },
      "rating": {
          "type": "number"
      },
      "review_count": {
          "type": "integer"
      },
      "distance": {
          "type": "integer"
      },
      "created_at": {
          "type": "string"
      },
  },
  "required": [
      "id",
      "user_id",
      "title",
      "description",
      "appointment_per_timeslot",
      "timeslot_minutes",
      "created_at",
  ]
}

# /item/{listing_item_id}
# /item
listing_item = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/ListingItem",  
  "type": "object",
  "properties": {
      "id": {
          "type": "string"
      },
      "listing_id": {
          "type": "string"
      },
      "name": {
          "type": "string"
      },
      "price": {
          "type": "integer"
      },
      "description": {
          "type": "string"
      },
      "created_at": {
          "type": "string"
      },
  },
  "required": [
      "id",
      "listing_id",
      "name",
      "price",
      "description",
      "created_at",
  ]
}

# /appointment/{appointment_id}/item/{appointment_item_id}
# POST /appointment/{appointment_id}/item
appointment_item = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/AppointmentItem",  
  "type": "object",
  "properties": {
      "id": {
          "type": "string"
      },
      "appointment_id": {
          "type": "string"
      },
      "listing_item_id": {
          "type": "string"
      },
      "quantity": {
          "type": "integer"
      },
      "notes": {
          "type": "string"
      },
      "listing_item": listing_item,
      "created_at": {
          "type": "string"
      },
  },
  "required": [
      "id",
      "appointment_id",
      "listing_item_id",
      "listing_item",
      "created_at",
  ]
}

#
appointment_client = {
     "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/AppointmentClient",
     "type": "object",
     "properties": {
        "username": {
            "type": "string"
        },
        "img_url": {
            "type": "string"
        },
     },
     "required": [
        "username"
     ]
}

# /appointment/{id}
# /appointment/{appointment_id}
# /appointment/{appointment_id}/request
# /appointment/{appointment_id}/accept
# /appointment/{appointment_id}/decline
# /appointment/{appointment_id}/cancel
# /appointment/{appointment_id}/complete
# /appointment/draft
appointment = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/Appointment",
  "type": "object",
  "properties": {
      "id": {
          "type": "string"
      },
      "provider_id": {
          "type": "string"
      },
      "provider_username": {
          "type": "string"
      },
      "client_id": {
          "type": "string"
      },
      "status": {
          "type": "string"
      },
      "price": {
          "type": "integer"
      },
      "time": {
          "type": "string"
      },
      "description": {
          "type": "string"
      },
      "lat": {
          "type": "number"
      },
      "lng": {
          "type": "number"
      },
      "listing": listing,
      "items": {
          "type": "array",
          "items": appointment_item
      },
      "provider": appointment_provider,
      "client": appointment_client,
      "created_at": {
          "type": "string"
      }
  },
  "required": [
      "id",
      "provider_id",
      "provider_username",
      "client_id",
      "status",
      "time",
      "listing",
      "client",
  ]
}

# GET /appointment/{appointment_id}/item
get_all_appointment_items = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/" ,  
  "type": "array",
  "items": appointment_item
}

# /appointment
get_all_appointments = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/" ,
  "type": "array",
  "items": appointment 
}

# /listing/{listing_id}/item
get_all_listing_items = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/",  
  "type": "array",
  "items": listing_item
}

# POST /tag
tag = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/Tag",
  "type": "object",
  "properties": {
      "id": {
          "type": "string"
      },
      "tag": {
          "type": "string"
      },
      "created_at": {
          "type": "string"
      },
  }  ,
  "required": [
      "id",
      "tag"
  ]
}

# GET /tag
get_all_tag = {
    "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/",
    "type": "array",
    "items": tag
}

#
location = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/Location",
  "type": "object",
  "properties": {
      "lat": {
          "type": "number"
      },
      "lng": {
          "type": "number"
      },
      "name": {
          "type": "string"
      },
      "number": {
          "type": "string"
      },
      "street": {
          "type": "string"
      },
      "locality": {
          "type": "string"
      },
      "postal_code": {
          "type": "string"
      },
      "region": {
          "type": "string"
      },
      "region_code": {
          "type": "string"
      },
      "country": {
          "type": "string"
      },
      "country_code": {
          "type": "string"
      },
      "label": {
          "type": "string"
      },
  }
}

# /location
get_all_location = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/ValidationError",
  "type": "array"  ,
  "items": location
}

#
message_recipient = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/MessageRecipient",  
  "type": "object",
  "properties": {
      "username": {
          "type": "string"
      },
      "user_id": {
          "type": "string"
      },
      "img_url": {
          "type": "string"
      },
  },
  "required": [
      "username",
      "user_id",
  ]
}

# 
thread_summary = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/ThreadSummary",
  "type": "object",
  "properties": {
      "thread_id": {
          "type": "string"
      },
      "content": {
          "type": "string"
      },
      "last_message": {
          "type": "string"
      },
      "last_read": {
          "type": "string"
      },
      "recipients": {
          "type": "array",
          "items": message_recipient
      },
      "read": {
          "type": "integer"
      }
  },
  "required": [
      "thread_id",
      "content",
      "last_message",
      "recipients",
      "read",
  ]
}

# GET /thread
thread_list = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/ThreadList",
  "type": "object",
  "properties": {
      "unread_count": {
          "type": "integer"
      },
      "thread": {
          "type": "array",
          "items": thread_summary
      },
  },
  "required": [
      "unread_count",
      "thread"
  ]  
}

# /thread/{thread_id}/message
message = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/Message",
  "type": "object",
  "properties": {
      "user_id": {
          "type": "string"
      },
      "content": {
          "type": "string"
      },
      "created_at": {
          "type": "string"
      },
  },
  "required": [
      "user_id",
      "content",
      "created_at"
  ]
}

# /thread/{thread_id}
# POST /thread
thread = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/Thread",
  "type": "object",
  "properties": {
      "id": {
          "type": "string"
      },
      "message": {
          "type": "array",
          "items": message
      },
      "recipients": {
          "type": "array",
          "items": message_recipient
      }
  },
    "required": [
      "id",
      "message",
      "recipients"
  ]  
}

#
notification = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/Notification",    
  "type": "object",
  "properties": {
      "id": {
          "type": "string"
      },
      "is_read": {
          "type": "integer"
      },
      "content": {
          "type": "string"
      },
      "created_at": {
          "type": "string"
      },
  },
  "required": [
      "id",
      "is_read",
      "content",
      "created_at"
  ]
}

# /blog/{blog_id}
# POST /blog
blog = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/Blog",    
  "type": "object",
  "properties": {
      "id": {
          "type": "string"
      },
      "content": {
          "type": "string"
      },
      "title": {
          "type": "string"
      },
      "user_id": {
          "type": "string"
      },
      "created_at": {
          "type": "string"
      },
  },
  "required": [
      "id",
      "user_id",
      "created_at"
  ]
}

# GET /blog
get_all_blog = {
    "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/Blog",    
    "type": "array",
    "items": blog
}

# /notification
get_x_all_notification = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/",  
  "type": "array",
  "items": notification
}

#
timeslot = {
     "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/Timeslot",
     "type": "object",
     "properties": {
        "day": {
            "type": "integer"
        },
        "start": {
            "type": "string"
        },
        "end": {
            "type": "string"
        },
        "available": {
            "type": "integer"
        }
     },
     "required": [
        "day",
        "start",
        "end",
        "available"
     ]
}

#
override = {
     "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/Override",
     "type": "object",
     "properties": {
        "id": {
            "type": "string"
        },
        "start": {
            "type": "string"
        },
        "end": {
            "type": "string"
        },
        "available": {
            "type": "integer"
        }
     },
     "required": [
        "id",
        "start",
        "end",
        "available"
     ]
}

# /listing/{listing_id}/schedule
# /listing/{listing_id}/schedule/override/{override_id}
# /listing/{listing_id}/schedule/override
schedule = {
    "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/Schedule",  
    "type": "object",
    "properties": {
        "schedule": {
            "type": "array",
            "items": timeslot
        },
        "override": {
            "type": "array",
            "items": override
        }        
    },
    "required": [
        "schedule",
        "override"
    ]
}

# POST /bookmark
bookmark = {
     "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/Bookmark",
     "type": "object",
     "properties": {
        "id": {
            "type": "string"
        },
        "provider_id": {
            "type": "string"
        },
        "user_id": {
            "type": "string"
        },
        "username": {
            "type": "string"
        },
        "created_at": {
            "type": "string"
        }
     },
     "required": [
        "id",
        "provider_id",
        "user_id",
        "username",
        "created_at",
     ]
}

# GET /bookmark
get_all_bookmark = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/",  
  "type": "array",
  "item": bookmark
}

#
listing_search_result = {
     "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/ListingSearchResult",
     "type": "object",
     "properties": {
        "id": {
            "type": "string"
        },
        "user_id": {
            "type": "string"
        },
        "username": {
            "type": "string"
        },
        "title": {
            "type": "string"
        },
        "description": {
            "type": "string"
        },
        "lat": {
            "type": "number"
        },
        "lng": {
            "type": "number"
        },
        "distance": {
            "type": "integer"
        },
        "rating": {
            "type": "number"
        },
        "review_count": {
            "type": "integer"
        },
        "price": {
            "type": "integer"
        },
        "provider": {
          "type": "array",
          "items": appointment_provider
      },
        "created_at": {
            "type": "string"
        },
     },
     "required": [
        "id",
        "user_id",
        "username",
        "title",
        "description",
        "created_at"
     ]
}

# GET /listing
get_all_listing_search = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/ValidationError",
  "type": "array",
  "items": listing_search_result  
}

# /provider/listing
get_x_all_listing_provider = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/",  
  "type": "array",
  "items": listing
}

# /user/payment_method_intent
stripe_client_secret = {
     "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/StripeClientSecret",
     "type": "object",
     "properties": {
        "si_client_secret": {
            "type": "string"
        }
     },
     "required": [
        "si_client_secret"
     ]
}

#
body_user_profile_photo_user_photo_post = {
     "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/Body_user_profile_photo_user_photo_post",
     "type": "object",
     "properties": {
        "file": {
            "type": "string"
        }
     },
     "required": [
        "file"
     ]
}

# 
validation_error = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/ValidationError",
  "type": "object",
  "properties": {
      "loc": {
          "type": "array",
          "items": {
                  "anyOf": [
                      {
                          "type": "string"
                      },
                      {
                          "type": "integer"
                      },
                  ]
              }
      },
      "msg": {
          "type": "string"
      },
      "type": {
          "type": "string"
      },
  } ,
  "required": [
          'loc',
          'msg',
          'type'
      ]
}

# HTTP Validation Error - 422
http_validation_error = {
  "$schema": "http://appt-ecs-lb-1016726455.us-east-1.elb.amazonaws.com/openapi.json#/components/shemas/HTTPValidationError",
  "type": "object",
  "properties": {
      "detail": {
          "type": "array",
          "items": validation_error
      },
  } 
}