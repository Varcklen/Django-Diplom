This is a course project for the 'Python Pro' course (Prog.Academy).

The project was built in VS Code using **Django** and **Heroku**.

**Project topic**: Website for providing services.

[Bootstrap Reference](https://startbootstrap.com/theme/agency)

[Manager Table Reference](https://bbbootstrap.com/snippets/bootstrap-5-table-search-and-checkboxes-10209122)

[Link to the site with the project used (if active)](https://diplom-project-march-9b70f4bff677.herokuapp.com/)

**The site has urls**:
- manager/ (managers only)
- manager/form/<str:pk>/ (managers only, update form)
- admin/ (admin only)
- account/login/
- account/register/
- account/logout/
- successful-send/ (Appears after the form has been successfully submitted)
- any other (404 error)

**Database tables**:
- Contacts
- History
- Partners
- Portfolios
- Services
- Staff


**Update from 16.04.25:**
- Added pages 'manager/form/<str:pk>/' and 'successful-send/'.
- Added a data table to the manager page, displaying all sent data.
- The manager page can now change the data of the 'UserMessage' class (by 'Update' button) in the form on the page 'manager/form/<str:pk>/'. Available for modification date: name, email, phone, message.
- Now, when data is successfully sent in the form on the 'home' and 'manager/form/<str:pk>/' pages, the user is sent to the 'successful-send/' page, where the user is informed about the successful sending of data.
