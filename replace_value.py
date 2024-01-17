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
