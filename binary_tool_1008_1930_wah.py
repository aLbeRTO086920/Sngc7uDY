# 代码生成时间: 2025-10-08 19:30:46
#!/usr/bin/env python

# binary_tool.py - A simple binary file read and write tool using the FALCON framework.

from falcon import API, Request, Response
import sys
import os

# Define the API resource class
class BinaryTool:
    def on_get(self, req, resp):
        """
        Handles GET requests.
        Displays a simple form to upload a binary file.
        """
        resp.media = {
            "message": "Please upload a binary file using the POST method."
        }

    def on_post(self, req, resp):
        """
        Handles POST requests.
        Reads the uploaded binary file and saves it to disk.
        """
        # Check if the file is uploaded
        file_data = req.get_media()
        if not file_data:
            resp.media = {"error": "No file uploaded."}
            resp.status = 400
            return

        # Save the file to disk
        try:
            with open('uploaded_file.bin', 'wb') as f:
                f.write(file_data)
            resp.media = {"message": "File uploaded and saved successfully."}
        except Exception as e:
            resp.media = {"error": str(e)}
            resp.status = 500

# Create the Falcon API instance
api = API()

# Add the BinaryTool resource to the API
api.add_route('/upload', BinaryTool())

if __name__ == '__main__':
    # Run the API
    api.run(port=8000)