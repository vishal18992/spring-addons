# spring-addons

Please follow the below steps.

1. Download the module and install the module without demo data.
2. Download the postman.


For the lead generate from Api.

You can download the postman collection "Spring API.postman_collection.json" and import in postman.

OR you can follow the below steps.

!important URL may vary based on your server.

1. Add the new request 
2. Write the url like http://127.0.0.1:8069/lead and set type as POST.
3. Goto Header and set the Content-Type = application/json
4. Goto Body and set as raw and put the values as json -> {
   
    "params": {
        "name": "Test",
        "phone": "+1 204-901-4522",
        "customer": "Demo",
        "salesperson": "Administrator"
    }
} 