# Smart_attendance_system
Description:

❖ This attendance tracking system focuses on providing an integrated platform for managing employee attendance and leave updates.
❖ It features an interactive calendar that visually displays attendance status, marking leave days in red and calculating the number of days present.
❖ Additionally, it facilitates easy access to employee records, enabling users to apply for leave and receive updates on their requests seamlessly.
❖ This comprehensive approach ensures efficient tracking and management of attendance data, enhancing overall productivity and communication within the organization.

Technologies used:

Frontend: HTML, CSS, Javascript
Backend: Python- OpenCV, Tkinter, Numpy, Pandas
Database: MySQL

Install Dependencies:

pip install tk-tools
pip install opencv-contrib-python
pip install datetime
pip install pytest-shutil
pip install python-csv
pip install numpy
pip install pillow 
pip install pandas
pip install times

After installing the Dependencies, run the Flask app server.py, then the project can be accessed in your browser at http://localhost:5000. 
Now login as employee(krishna,krishna@2006) or HR(gokila,gokila@2005) you can change the username and password, then click face recognition on the employee page and register your face through help button on the top corner, now you can save your attendance by clicking the "Take attendance" button.
HR page is used to check the list of employees present through the calendar and to grant leave. As of now the request will be stored and sent through the local server on your computer.
