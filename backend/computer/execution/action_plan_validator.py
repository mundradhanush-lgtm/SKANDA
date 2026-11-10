def validate_action_plan(computer_response):
    validation_list=["click", "double_click", "right_click", "type", "press_key", "scroll", "drag", "move", "wait"]
    valid_statuses = ["READY", "NEEDS_APPROVAL", "NEEDS_CLARIFICATION", "AUTHENTICATION_REQUIRED", "COMPLETED"]
    computer_response_dict=json.loads(computer_response)
    i=0
    while i<len(computer_response_dict["actions"]):
        value_of_action=computer_response_dict["actions"][i]["action"]
        if(value_of_action in validation_list):
            if(type(computer_response_dict["actions"][i]["approval_required"])==bool):
                i+=1
                continue
            else:
                return False
        else:
            return False
    if(computer_response_dict["status"] in valid_statuses):
        if(computer_response_dict["required_authentication"]==None):
            return True
        else:
            if(type(computer_response_dict["required_authentication"])==dict):
                if("missing" in computer_response_dict["required_authentication"]):
                    if(type(computer_response_dict["required_authentication"]["missing"])==list):
                        return True
        if(type(computer_response_dict["required_authentication"])!=dict):
            return False
        if(type(computer_response_dict["required_authentication"])==dict and "missing" not in computer_response_dict["required_authentication"]):
            return False
    else:
        return False