from jira import JIRA
import sys

def update_issue_field(username, password, field_id, new_values, jira_tickets):
    jira_url = "https://jira.charter.com"

    try:
        jira = JIRA(server=jira_url, basic_auth=(username, password))

        for issue_key in jira_tickets:
            issue = jira.issue(issue_key)

            current_values = getattr(issue.fields, field_id, "")
            current_values = current_values.split(",") if current_values else []

            # Extract artifact ID and version from new value
            new_value_info = new_values[0].split('-')[0:2]

            # Remove old values with the same artifact ID and version
            current_values = [value for value in current_values if value.split('-')[0:2] != new_value_info]

            # Add new value at the beginning
            current_values = [new_values[0]] + current_values

            updated_values_str = ",".join(current_values)

            issue.update(fields={field_id: updated_values_str})

            print(f"Field '{field_id}' in issue '{issue_key}' updated successfully to '{updated_values_str}'.")
    except Exception as e:
        print(f"Failed to update the field '{field_id}'. Error:", str(e))

# Define the Jira issue keys here
jira_tickets = ["MOBIT2-31903"]
print(f'Jira_Tickets:', jira_tickets)
# Get custom field ID and values
field_id = "customfield_17856"
new_values = ["msb-updateucm-4.0.0-343"]

# Check if correct number of arguments is provided (username, password)
if len(sys.argv) != 3:
    print("Usage: python filename.py username password")
    sys.exit(1)

# Parse command line arguments
username = sys.argv[1]
password = sys.argv[2]

# Update the custom field with multiple values
update_issue_field(username, password, field_id, new_values, jira_tickets)
