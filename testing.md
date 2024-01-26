This test script can be followed in order to manually test the site for any faults.

| Ref No | Testcase                          | Expected Result                                         | Test Result |
|--------|-----------------------------------|---------------------------------------------------------|-------------|
|        |**Pages**                          |                                                         |             |
| 01     | Open the Homepage                 | Homepage loads with the correct template and data       | Pass        |
| 02     | Open an article                   | Post detail page loads with correct template and data   | Pass        |
| 03     | Open meet the team                | Meet the team page loads with correct template and data | Pass        |
|        | **User Account**                  |                                                         |             |
| 04     | Register a user with valid data   | Success, user is registered and logged in               | Pass        |
| 05     | Register a user with invalid data | Unsuccessful, form loads again with data and errors     | Pass        |
| 06     | Login a user with valid data      | Success, user is logged in                              | Pass        |
| 07     | Login a user with invalid data    | Unsuccessful, form loads again with data and errors     | Pass        |
| 08     | Liking an article                 | Like count increases and like button changes            | Pass        |
| 09     | Unliking an article               | Like count decreases and like button changes            | Pass        |
|        | **Commenting**                    |                                                         |             |
| 10     | Writing a comment                 | Success, comment is added to the list, message is shown | Pass        |
| 11     | Editing a comment                 | Success, comment content is edited, message is shown    | Pass        |
| 12     | Delete a comment                  | Success, comment is deleted, message is shown           | Pass        |
|        | **Unauthorised requests**         |                                                         |             |
| 13     | Liking an article                 | Request fails, button does not respond                  | Pass        |
| 14     | Writing a comment                 | Form is not present, no request is possible             | Pass        |
| 15     | Editing a comment                 | Button is not present, no request is possible           | Pass        |
| 16     | Delete a comment                  | Button is not present, no request is possible           | Pass        |


These tests are based on Kristyna Wach's test script for [Fantastic News](https://github.com/Cushione/fantastic-news/tree/main)