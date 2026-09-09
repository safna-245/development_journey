# from google import genai

# from mysql import connector

# connection = connector.connect(
#     user= "root",
#     password="Password@123",
#     host="localhost",
#     database="inventory_db"
# )

# cursor = connection.cursor()

# query = "select * from inventory "

# cursor.execute(query)

# item = cursor.fetchall()

# inventory_data = item



# client = genai.Client(api_key=GEMINI_API_KEY)

# prompt = f"""
# You are an AI inventory management assistant.

# Analyze the following inventory data:

# {inventory_data}

# For each inventory item:

# 1. Check the current quantity.
# 2. Compare the quantity with the reorder level.
# 3. Identify whether the item needs reordering.
# 4. Classify stock depletion risk as Low, Medium, or High.
# 5. Suggest a suitable reorder quantity.
# 6. Identify any unusual inventory situation.

# Then provide:

# 1. Overall Inventory Summary
# 2. Low Stock Items
# 3. Out of Stock Items
# 4. High Risk Items
# 5. Recommended Reorder Quantities
# 6. Suggested Actions

# Use only the information provided in the inventory data.
# Do not invent missing information.

# Give the result in a simple and clear format suitable for an inventory management system.

# """

# response = client.models.generate_content(
#     model="gemini-3.5-flash",
#     contents=prompt
#     )

# print(response)
