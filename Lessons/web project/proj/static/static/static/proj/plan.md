0. Choose some idea
-------------------

1. Design markdown -> generalized page count; names and urls; entities;
   - 3 pages: /catalog/ - show items/producs, /basket/ - show selecetd items, /catalog/<int:id>/ - show item metadata 
(1.5) Categories -> detail the categories
    - category/name/
2. Users (if any) -> user roles, functionality per role
    - 2 roles, admin and user, user can read and add to basket, admin can also delete
3. Interactive elements -> links, buttons, any other elements
    - list of pairs element:action
4. Design the models, design url patterns, design how the data from db will be injected
    - mapping page : entity data; url patterns
5. Design web forms -> pages and forms
    - mapping page:form:data
6. Check user journey and view infrastructure