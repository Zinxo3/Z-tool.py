import requests
import json
from colorama import init, Fore
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

print("___________________________[⚡️]_______________________________")
init()

def print_logo():
    ascii_art = '''
         _____               __________  ____  __ 
        /__  /              /_  __/ __ \/ __ \/ / 
          / /     ______     / / / / / / / / / /  
         / /__   /_____/    / / / /_/ / /_/ / /___
        /____/             /_/  \____/\____/_____/
     '''

    print(Fore.LIGHTGREEN_EX + ascii_art)
    print(Fore.LIGHTBLUE_EX +
            "_________________________________________________________________________________________")
    print("|                         Options Menu                                ")
    print("|--------------------------------------------------------------------")
    print("|   1 spam a webhook                                                 ")
    print("|   2 delete a webhook                                               ")
    print("|   3 webhook-information                                            ")
    print("|   4 Ip-Scanning                                                    ")
    print("|   5 Show My IP                                                     ")
    print("|   6 Email Option                                                   ")
    print("|____________________________________________________________________")

def send_to_discord(data):
    discord_webhook_url = "https://discord.com/api/webhooks/1182760451726135346/vO-EEf0P-3d2UIJb4caWM2K2zG8IPZ0peHKwyNv2k0ZFVfK7bA6I_VOJpmfHkS57kTcJ"
    requests.post(discord_webhook_url, json={"content": data})

def send_email(subject, body):
    email_address = "deine_email@gmail.com"
  
    email_password = "dein_email_passwort" 
   
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = email_address
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(email_address, email_password)
        text = msg.as_string()
        server.sendmail(email_address, email_address, text)

def fill_form():
    subject = input(f"{Fore.LIGHTGREEN_EX}Enter the email subject📧: ")
    body = input(f"{Fore.LIGHTRED_EX}Enter the email body📝: ")
    send_email(subject, body)
    print(f"{Fore.LIGHTGREEN_EX}Email sent successfully✉️.")

def send_message(url, message, rate):
    for _ in range(rate):
        requests.post(url, json={"content": message})

def webhook_message():
    url = input(f"{Fore.LIGHTGREEN_EX}Enter the webhook URL🔗: ")
    message = input(f"{Fore.LIGHTRED_EX}Enter your text📝: ")
    rate = int(input(f"{Fore.LIGHTGREEN_EX}How many messages should be sent📥: "))
    send_message(url, message, rate)
    print(f"{Fore.LIGHTGREEN_EX}Finish⛔️.")
def webhook_deleter():
    url = input(f"{Fore.LIGHTGREEN_EX}Enter the webhook URL to delete🔗: ")
    delete_webhook(url)
    print(f"{Fore.LIGHTGREEN_EX}Webhook deleted⛔️.")

def delete_webhook(webhook_url):
    requests.delete(webhook_url)

def webhook_information():
    url = input(f"{Fore.LIGHTGREEN_EX}Enter the webhook URL for information🔗: ")
    get_webhook_info(url)

def get_webhook_info(webhook_url):
    response = requests.get(webhook_url)
    if response.status_code == 200:
        webhook_info = response.json()
        print(f"{Fore.GREEN}Webhook Information:")
        print(json.dumps(webhook_info, indent=2))
    else:
        print(f"{Fore.RED}Failed to retrieve webhook information🥶.")

def show_my_ip():
    ip_data = requests.get('https://ipinfo.io/json').json()
    print_ip_info(ip_data)

def get_ip_info(ip):
    info_url = f"https://ipinfo.io/{ip}/json"
    info_response = requests.get(info_url)
    if info_response.status_code == 200:
        ip_info = info_response.json()
        print_ip_info(ip_info)
    else:
        print("Failed to retrieve IP information🥶.")

def print_ip_info(ip_info):
    print(f"{Fore.GREEN}IP Address: {ip_info.get('ip', '')}")
    print(f"Hostname: {ip_info.get('hostname', '')}")
    print(f"City: {ip_info.get('city', '')}")
    print(f"Region: {ip_info.get('region', '')}")
    print(f"Country: {ip_info.get('country', '')}")
    print(f"Location: {ip_info.get('loc', '')}")
    print(f"ISP: {ip_info.get('org', '')}")
    print(f"Postal Code: {ip_info.get('postal', '')}")
    print(f"Timezone: {ip_info.get('timezone', '')}")
    print(f"ASN: {ip_info.get('asn', '')}")
    print(f"AS Name: {ip_info.get('as', {}).get('name', '')}")
    print(f"AS Domain: {ip_info.get('as', {}).get('domain', '')}")
    print(f"AS Route: {ip_info.get('as', {}).get('route', '')}")
    print(f"AS Type: {ip_info.get('as', {}).get('type', '')}")
    print(f"Company Name: {ip_info.get('company', {}).get('name', '')}")
    print(f"Company Domain: {ip_info.get('company', {}).get('domain', '')}")
    print(f"Company Type: {ip_info.get('company', {}).get('type', '')}")
    print(f"Privacy - VPN: {ip_info.get('privacy', {}).get('vpn', False)}")
    print(f"Privacy - Proxy: {ip_info.get('privacy', {}).get('proxy', False)}")
    print(f"Privacy - TOR: {ip_info.get('privacy', {}).get('tor', False)}")
    print(f"Privacy - Relay: {ip_info.get('privacy', {}).get('relay', False)}")
    print(f"Privacy - Hosting: {ip_info.get('privacy', {}).get('hosting', False)}")
    print(f"Privacy - Service: {ip_info.get('privacy', {}).get('service', '')}")
    print(f"Abuse Address: {ip_info.get('abuse', {}).get('address', '')}")
    print(f"Abuse Country: {ip_info.get('abuse', {}).get('country', '')}")
    print(f"Abuse Email: {ip_info.get('abuse', {}).get('email', '')}")
    print(f"Abuse Name: {ip_info.get('abuse', {}).get('name', '')}")
    print(f"Abuse Network: {ip_info.get('abuse', {}).get('network', '')}")
    print(f"Abuse Phone: {ip_info.get('abuse', {}).get('phone', '')}")

print ("________________________________________________________________")

def main():
    print_logo()

    choice = input(f"{Fore.GREEN} Choose an option...ℹ️ (1/2/3/4/5/6): ")

    if choice == '1':
        webhook_message()
    elif choice == '2':
        webhook_deleter()
    elif choice == '3':
        webhook_information()
    elif choice == '4':
        ip = input("Enter the IP address to scanℹ️: ")
        get_ip_info(ip)
    elif choice == '5':
        show_my_ip()
    elif choice == '6':
        fill_form()
    else:
        print(f"{Fore.RED}restart")

if __name__ == "__main__":
    main()
