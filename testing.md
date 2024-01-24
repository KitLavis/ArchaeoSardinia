This test script can be followed in order to manually test the site for any faults. It includes the results of our in house test.

| Ref No | Testcase                          | Expected Result                                         | Test Result |
|--------|-----------------------------------|---------------------------------------------------------|-------------|
|        |**Pages**                          |                                                         |             |
| 01     | Open the Homepage                 | Homepage loads with the correct template and data       | PASS        |
| 02     | Open an article                   | Post detail page loads with correct template and data   | PASS        |
| 03     | Open meet the team                | Meet the team page loads with correct template and data | PASS        |
|        | **User Account**                  |                                                         |             |
| 04     | Register a user with valid data   | Success, user is registered and logged in               | PASS        |
| 05     | Register a user with invalid data | Unsuccessful, form loads again with data and errors     | PASS        |
| 06     | Login a user with valid data      | Success, user is logged in                              | PASS        |
| 07     | Login a user with invalid data    | Unsuccessfuls, form loads again with data and errors    | PASS        |
| 08     | Liking an article                 | Like count increases and like button changes            | PASS        |
| 09     | Unliking an article               | Like count decreases and like button changes            | PASS        |
| 10     | **Commenting**                    |                                                         |             |
| 11     | Writing a comment                 | Success, comment is added to the list, message is shown | PASS        |
| 12     | Editing a comment                 | Success, comment content is edited, message is shown    | PASS        |
| 13     | Delete a comment                  | Success, comment is deleted, message is shown           | PASS        |
| 14     | **Unauthorised requests**         |                                                         |             |
| 15     | Liking an article                 | Request fails, button does not respond                  | PASS        |
| 16     | Writing a comment                 | Form is not present, no request is possible             | PASS        |
| 17     | Editing a comment                 | Button is not present, no request is possible           | PASS        |
| 18     | Delete a comment                  | Button is not present, no request is possible           | PASS        |