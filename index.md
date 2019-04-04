# Advertisement Management System based on Django

The project involved creation of website for advertisement management systems which is frequently used by various content management sites to monitor and approve the content being made. There are category of user role in the app (Editor, Approver-1, Approver-2 and Approver-3). This includes permissions where Editor can add/modify/delete advertisement form and various level of approvers/reviewers. . 

The editor is responsible for creating/modifying/deleting advertisements.

**Approver-1:** Advertisement created by Editor will be displayed on Approver-1’s dashboard. Approver-1 will approve/reject advertisement form with comments. If Approver-1 rejects the added form then advertisement form's status is updated to reject and makes it visible to editor. If approver-1 approves the advertisement form then form will visible to approver 2.

**Approver2:** All the Forms approved by Approver-1 will be visible to Approver-2. If Approver-2 rejects the form then it is shown to editor with reject status along with the comments. If Approver-2 approves the form then form will visible to approver-3.

**Approver3:** All form that are approved by Approver-2 will be visible to Approver-3. If Approver-3 rejects the form then show to editor with reject status. If Approver-3 approves the form then form will visible to editor or other approvers with an approved status.

![Flow Diagram of Project](/images/Flowdiagram.png)

**Flow Diagram For the Advertisement website**

Advertisement field was created for the following fields

## AD Form Fields :
- Title 
- Start_date 
- End_date
- Amount_per_month 
- Amount_per_day 
- Start_date_pic 
- End_date_pic 

## Home Page:

Home page by default shows Login/Signup option. If the user clicks on Signup then it implements Django modified signup module. If user has already account and had assigned role then dashboard of user should be showed. A dashboard shows all forms list related to loggedin user. For example the rejected forms will be shown to the editor while for the approvers the pending forms will be shown along with the respective comments.

## Login Screen:
Modified the Django Login Module to use email instead of username and as usual password continues be used for login.

## Signup :
Signup by Email, Password

## Few Snapshots of the website

![Sign Up](/images/Signup.JPG)

**Sign Up**

![Login](/images/Loginpage.JPG)

**Login**

![New advertisement post](/images/Newpost.JPG)

**New advertisement post**

![Reject and Accept page for Reviewer](/images/Rejectacceptpost.JPG)

**Reject and Accept page for Reviewer**

![Comment on the Post with accept and reject decision](/images/Commentpost.JPG)

**Comment on the Post with accept and reject decision**

![Rejected Posts for the Editor](/images/Rejectedpost.JPG)

**Rejected Posts for the Editor**
