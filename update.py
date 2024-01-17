from jira import JIRA
import sys
import os
def update_issue_field(username, password, field_id, new_values, jira_tickets):
    jira_url = "https://jira.charter.com"

    try:
        jira = JIRA(server=jira_url, basic_auth=(username, password))

        for issue_key in jira_tickets:
            issue = jira.issue(issue_key)

            current_values = getattr(issue.fields, field_id, "")
            current_values = current_values.split(",") if current_values else []

            updated_values = current_values + new_values
            updated_values_str = ",".join(updated_values)

            issue.update(fields={field_id: updated_values_str})
            if text != None:
                jira.add_comment(issue, body=text)

            print(f"Field '{field_id}' in issue '{issue_key}' updated successfully to '{updated_values}'.")
    except Exception as e:
        print(f"Failed to update the field '{field_id}'. Error:", str(e))

# Define the Jira issue keys here
ticket_details = os.environ.get('JIRA_TICKET')
jira_tickets = ticket_details.split(',')
print(f'Jira_Tickets:', jira_tickets)

# Get custom field ID and values
#field_id = "customfield_17856"
field_id = os.environ.get('FIELD_ID')
new_values = os.environ.get('VALUE')
text = os.environ.get('COMMENT')

# Check if correct number of arguments is provided (username, password)
if len(sys.argv) != 3:
    print("Usage: python filename.py username password")
    sys.exit(1)

# Parse command line arguments
username = sys.argv[1]
password = sys.argv[2]

# Update the custom field with multiple values
update_issue_field(username, password, field_id, new_values, jira_tickets)
