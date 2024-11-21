import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from datetime import timedelta


def authentify_admin_login():
    hasher = stauth.Hasher([])
    hashed_passwords = [hasher.hash(password) for password in ['admin123', 'admin234']]
    print("Hashed Passwords:", hashed_passwords)

    try:
        with open('/Users/michaeladebayo/Documents/Simplon/brief_projects/the_steel_fist/config.yml') as file:
            config = yaml.load(file, Loader=SafeLoader) 
    except FileNotFoundError:
        print("Config file not found.")
        return None
    except yaml.YAMLError as e:
        print("Error parsing config file:", e)
        return None

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['credentials'],
        timedelta(days=30),
        config['cookie']['key'],
        config['cookie']['name']
    )

    return authenticator.login('main', clear_on_submit=True)


    


# def authentify_admin_login():

#     hasher = stauth.Hasher([])
#     hashed_passwords = [hasher.hash(password) for password in ['admin123', 'admin234']]
#     print("Hashed Passwords:", hashed_passwords)

#     try:
#         with open('/Users/michaeladebayo/Documents/Simplon/brief_projects/the_steel_fist/config.yml') as file:
#             config = yaml.load(file, Loader=SafeLoader)
#     except FileNotFoundError:
#         print("Config file not found.")
#         return None
#     except yaml.YAMLError as e:
#         print("Error parsing config file:", e)
#         return None

#     authenticator = stauth.Authenticate(
#         config['credentials'],
#         config['cookie']['expiry_days'],
#         config['cookie']['key'],
#         config['cookie']['name']
#         )

#     authentication_status = authenticator.login('main', clear_on_submit=True)

#     # if authentication_status:
#     #     logout = authenticator.logout('Logout', 'main')
#     # else:
#     #     logout = None  

#     return authentication_status
