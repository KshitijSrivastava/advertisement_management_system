The project for the mid-semester involved creation of website for advertisement management systems which is frequently used by Careers360 team to add new advertisements. This includes permissions where Editor can add/modify/delete form. There are category of user role in the app (Editor, Approver-1, Approver-2 and Approver-3). 

The editor is responsible for creating/modifying/deleting advertisements.

**Approver-1:** Advertisement created by Editor will be displayed on Approver-1’s dashboard. Approver-1 will approve/reject advertisement form with comments. If Approver-1 rejects the added form then update the form status to reject and make it visible to editor. If approver-1 approves the advertisement form then form will visible to approver 2.

**Approver2:** All the Forms approved by Approver-1 will be visible to Approver-2. If Approver-2 rejects the form then show to editor with reject status and comment. If Approver-2 approves the form then form will visible to approver-3.

**Approver3:** All form that are approved by Approver-2 will be visible to Approver-3. If Approver-3 rejects the form then show to editor with reject status. If Approver-3 approves the form then form will visible to editor or other approvers with an approved status.

Form Fields :
- Title 
- Start_date 
- End_date
- Amount_per_month 
- Amount_per_day 
- Start_date_pic 
- End_date_pic 

Home Page:

Home page by default shows Login/Signup option. If the user clicks on Signup then it implements Django signup module. If user has already account and had assigned role then dashboard of user should be showed. A dashboard shows all forms list related to login user.

Login Screen:
Login by username and password

Signup :
Signup by name, email, password
