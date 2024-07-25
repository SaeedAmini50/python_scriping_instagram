import json
import base64

# Load account information from JSON file
with open('instagram_cookies4.json', 'r') as f:
    account_info = json.load(f)

# Extract sessionid, csrftoken, ds_user_id from account_info
sessionid = account_info.get('sessionid')
csrftoken = account_info.get('csrftoken')
ds_user_id = account_info.get('ds_user_id')
should_use_header_over_cookies=account_info.get('should_use_header_over_cookies')
# Create combined string separated by ','
combined_string = f"{sessionid},{csrftoken},{ds_user_id},{should_use_header_over_cookies}"

# Create authorization dictionary
auth_dict = {
    "sessionid": sessionid,
    "csrftoken": csrftoken,
    "ds_user_id": ds_user_id,
    "should_use_header_over_cookies": should_use_header_over_cookies
}

# Convert dictionary to JSON string
auth_json = json.dumps(auth_dict)

# Encode JSON string to ASCII bytes
ascii_encoded = auth_json.encode('ascii')

# Encode ASCII bytes to base64
base64_encoded = base64.b64encode(ascii_encoded)

# Convert base64 bytes to string
base64_string = base64_encoded.decode('ascii')

# Print the base64 encoded string
print("Base64 Encoded String:")
print(base64_string)

# Decode base64 string back to JSON
decoded_bytes = base64.b64decode(base64_string)
decoded_string = decoded_bytes.decode('ascii')
decoded_dict = json.loads(decoded_string)

# Print the decoded JSON dictionary
print("Decoded JSON Dictionary:")
print(decoded_dict)
