from cmd import Cmd
import sys
import subprocess
import json

subdomain = "zcc19"
email_address = "sshen98@wisc.edu"
token = "QmL9OrzgxYtY1naGtsX2aDuGGGXcsWfEygYLuVYf"

class MyPrompt(Cmd):
    def do_exit(self, inp):
        print("Thanks for using the ticket viewer. Goodbye.")
        return True
    
    def do_viewAll(self, inp):
        tickets = getData("")
        if tickets == False:
            return

        if len(tickets) == 0:
            print("Error: There is no ticket in the database.")
            return

        endPage = len(tickets) % 25
        pages = len(tickets) // 25 if endPage == 0 else len(tickets) // 25 + 1
        data = []
  
        for i in range(pages):
            page = []
            for item in range(i*25, (i+1)*25):
                if item == len(tickets):
                    break
                ticket = {}
                ticket['id'] = tickets[item]['id']
                ticket['status'] = tickets[item]['status']
                ticket['subject'] = tickets[item]['subject']
                ticket['desc'] = tickets[item]['description']
                page.append(ticket)
            data.append(page)
        
        print("====================================================================================================")
        print("{} total tickets on {} pages".format(len(tickets), pages))
        print("Index |   ID  | Status  | Subject")
        for i, item in enumerate(data[0]):
            print("{:5} | {:5} | {:7} | {}".format(str(i+1), item['id'], item['status'], item['subject']))
        print("{} tickets on page 1".format(len(data[0])))

        if pages != 1:
            stay = 1
            while stay:
                print("Please enter 'q' to exit view all page panel.")
                print("====================================================================================================")
                page = input("Please select the number of page: ")
                while page.isdigit() == False or int(page) > pages:
                    if page == 'q':
                        stay = 0
                        break
                    print("Wrong page number, please type between 1 to {} or enter 'q' to leave the panel.".format(pages))
                    print("====================================================================================================")
                    page = input("Please select the number of page: ")

                if stay == 0:
                    break
                print("Index |   ID  | Status  | Subject")
                for i, item in enumerate(data[int(page)-1]):
                    print("{:5} | {:5} | {:7} | {}".format(str(i+1), item['id'], item['status'], item['subject']))
                print("{} tickets on page {}".format(len(data[int(page)-1]), page))
    
    def do_viewSingle(self, inp):
        stay = 1
        while stay:
            print("Please enter 'q' to exit view single ticket panel.")
            print("====================================================================================================")
            inp = input("Please input ticket id: ")
            while inp.isdigit() == False: #while inp.isdigit() == False or int(inp) > len(tickets):
                if inp == 'q':
                    stay = 0
                    break
                print("Wrong ticket id, please enter digits or enter 'q' to leave the panel.") #.format(len(tickets))
                print("====================================================================================================")
                inp = input("Please input ticket id: ")

            if stay == 0:
                break
            flag = 0
            item = getData("/" + inp + ".json")
            if item == False:
                return

            if len(item) != 0:
                flag = 1
                print("ID    | Status  | Subject | Description")
                print("{:5} | {:7} | {} | {}".format(item['id'], item['status'], item['subject'], item['description']))
            # for item in tickets:
            #     if int(inp) == item['id']:
            #         print("ID | Status | Subject")
            #         print("{} | {} | {}".format(item['id'], item['status'], item['subject']))
            #         flag = 1
            #         break

            if flag == 0:
                print("Error: The ticket is not exist.")

    def do_menu(self, inp):
        print("Select view options:")
        print("\tPress 'viewAll' to view all tickets.")
        print("\tPress 'viewSingle' to view individual ticket details.")
        print('\tSee more usage examples in help.')
    
    def help_viewAll(self):
        print("Display all tickets.")
        print("Each page contains 25 tickets and show each ticket's id, status and subject. If users want to see more, users can use viewSingle to view more informaiton.")
        print("Show the first page when entering, and users can select which pages to see afterward.")
        print("\tEx. viewAll")
        print("After entering the panel, the console would show \"Please select the number of page: \", and then input the chosen page.")
        print("\tEx. 1")

    def help_viewSingle(self):
        print("Display individual ticket details.")
        print("Show the ticket's id, status, subject, and description, and users can select which ticket to view after entering viewSingle.")
        print("\tEx. viewSingle")
        print("After entering the panel, the console would show \"Please input ticket id or enter 'q' to leave the panel:\", and then input the chosen ticket id.")
        print("\tEx. 1")

    def help_menu(self):
        print("Menu options.")

    def help_exit(self):
        print("Exit the ticket viewer.")

def getData(method):
    cmd = "curl https://" + subdomain + ".zendesk.com/api/v2/requests" + method + " -v -u" + email_address + "/token:" + token + " > out"
    # requests = os.popen(cmd)
    p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    requests, err = p.communicate()
    if err != None:
        print("Error: Something went wrong to connect to the server!")
        return False

    out = json.loads(requests) # out = json.loads(requests.read())
    if 'requests' in out:
        tickets = out['requests']
    elif 'request' in out:
        tickets = out['request']
    else:
        tickets = {}
    # with open("alltickets.json", "w+") as f:
    #     f.write(str(out))
    return tickets

if __name__ == "__main__":
    print("====================================================================================================")
    print("Welcome to the ticket viewer!")
    print("Type 'menu' to view options or 'exit' to exit.")
    MyPrompt().cmdloop()