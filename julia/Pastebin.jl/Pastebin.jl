using HTTP
using JSON

# will later get secrets from config.json
api_dev_key = ""
api_user_name = ""
api_user_password = ""

# 0=public 1=unlisted 2=private
api_paste_private 	  = "1" 
#api_paste_expire_date	= "N" # never expires
api_paste_expire_date	= "10M" # expires in 10 minutes

# "text" applies no formatting or highlighting. See https://pastebin.com/api
# for other options
api_paste_format 		  = "text"

# if an invalid or expired api_user_key is used, an error will spawn. If no 
# api_user_key is used, a guest paste will be created
api_user_key 		  	  = "" 

url 				= "https:#pastebin.com/api/api_post.php"

# paste name
api_paste_name			= "justmyfilename.php"

# paste content
api_paste_code 	  	= "just some random text you :)"

# get secrets from config.json
function load_config()
  j = nothing
  open("config.json", "r") do io
    j = JSON.parse(io)
  end
  j
end

function login(dev_key, username, password)
  login_url = "https://pastebin.com/api/api_login.php"

  request_body = "api_dev_key=$dev_key"
  request_body *= "&api_user_name=$username"
  request_body *= "&api_user_password=$password"
  
  println("sending this request body: ", request_body)

  HTTP.request("POST", login_url, [], request_body)
end

function main()
  config = load_config()

  api_dev_key = config["api_dev_key"]
  api_user_name = config["api_user_name"]
  api_user_password = config["api_user_password"]

  response = login(api_dev_key, api_user_name, api_user_password)
  println("this is the body: ", String(response.body))
end

