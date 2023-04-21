# import package that can send http requests
import requests

# define function that will send a post request
def post_form(ip, username, password):

    url = "http://" + ip + ":8080/Authorize"
    data = {"username": username, "password": password}

    response = requests.post(url, data=data)

    return



def main():
    # a list of ip addresses
    ip_list = ["192.168.98.144"]
    for ip in ip_list:
        print(ip)
        post_form(ip, "admin", "admin")
        
    

if __name__ == '__main__':
    main()