current_values = getattr(issue.fields, field_id, "")
current_values = current_values.split(",") if current_values else []

# Remove old values with the same artifact ID
current_values = [value for value in current_values if value.split('-')[0] != new_values[0].split('-')[0]]

# Add new value
current_values.append(new_values[0])

updated_values_str = ",".join(current_values)

issue.update(fields={field_id: updated_values_str})
