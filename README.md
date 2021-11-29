# Zendesk Ticket Viewer

## Brief description:
Built a ticket viewer accomplishing below objectives using python and displayed results in console.

## Objectives:
* Connect to the Zendesk API
* Request all the tickets for your account
* Display them in a list
* Display individual ticket details
* Page through tickets when more than 25 are returned

## Usages:
* Run `./main.py` to start an interactive shell
* Below is the command list for the shell
  
<table>
    <tr>
        <td>Command</td>
        <td>Description</td>
    </tr>
    <tr>
        <td>menu</td>
        <td>Menu options.</td>
    </tr>
    <tr>
        <td>exit</td>
        <td>Exit the ticket viewer.</td>
    </tr>
    <tr>
        <td>viewAll</td>
        <td>* Display all tickets.<br />* Each page contains 25 tickets and show each ticket's id, status and subject. If users want to see more, users can use viewSingle to view more informaiton.<br />* Show the first page when entering, and users can select which pages to see afterward.<br />* After entering the panel, the console would show "Please select the number of page: ", and then input the chosen page.<br />Ex. 1</td>
    </tr>
    <tr>
        <td>viewSingle</td>
        <td>* Display individual ticket details.<br />* Show the ticket's id, status, subject, and description, and users can select which ticket to view after entering viewSingle.<br />* After entering the panel, the console would show "Please input ticket id or enter 'q' to leave the panel:", and then input the chosen ticket id.<br />Ex. 1</td>
    </tr>
</table>

## Design:
* Get all tickets information `Index | ID | Status | Subject` in viewAll, and show error message `Error: desc` if there is no database. 
* Use ticket's id to get its information `ID | Status | Subject | Description` via curl in viewSingle, and show error message `Error: desc` if the ticket is not exist.
* Display `Error: desc` if program couldn't connect to server.

# Environment
* Implement on Python3.6 (Windows 10)

# Author
* Shuang-Shuang(Sunny Shen)
