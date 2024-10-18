import json

# Example data for the chart
data = {
    "labels": ["January", "February", "March", "April", "May", "June", "July"],
    "datasets": [
        {
            "label": "Dataset 1",
            "data": [65, 59, 80, 81, 56, 55, 40],
        },
        {
            "label": "Dataset 2",
            "data": [28, 48, 40, 19, 86, 27, 90],
        }
    ]
}

# Save the JSON data to a file (in _data directory)
with open('_data/chart_data.json', 'w') as outfile:
    json.dump(data, outfile)

print("Data saved to _data/chart_data.json")