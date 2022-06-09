# Capstone2L1
Capstone Project 2 Level 1

This program is a task management system that stores information in files and allows you to add and manipulate the information.

You are required to enter your username and password to log in. If you enter an incorrect username or password, you will be prompted to try again. Once
you have logged in, you are presented with a menu of options.

If you select 'r' to register a user, you are requested to enter the username and password of the new user. You are required to confirm the password too.
If the username or password already exist in the file, you are prompted to try again. Once you have successfully entered the details, the new user is
added to users.txt and you are returned to the main menu.

If you select 'a' to add a task, you are requested to enter the details of the task including the name of the user to whom the task is assigned, task
title, task description and the due date of the task in the format dd/mm/yyyy. The new task with the details is added to tasks.txt and you are returned
to the main menu.

If you select 'va' to view all tasks, a list of the tasks along with the details of each task is displayed in a readable format.

If you select 'vm' to view my tasks, a list of the tasks assigned to the currently logged in user is displayed. From here, you are given the option to
either return to the main menu or select a task, which you can either edit or mark as complete. If you choose edit, you are able to change the details
of the task, and if you choose mark as complete, the task will be marked as completed in the file.

If you select 'gr' to generate reports, two new files are generated: task_overview.txt and user_overview.txt. In these files, an overview of the tasks
and users on the system as well as details about the tasks and users are stored (eg. percentage of overdue tasks, percentage of tasks still to be
completed etc).

If you select 's' to display statistics, the information stored in the task_overview.txt and user_overview.txt files is displayed. If the reports have
not yet been generated, they are generated now.

The final option 'e' allows you to exit the task management system.
