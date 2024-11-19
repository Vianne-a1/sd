20_bt-_smtg_ZengJ-YangT

Direct View via github pages: https://vianne-a1.github.io/20_bt-_smtg_ZengJ-YangT/index

State list credit: https://gist.github.com/pusherman/3145761

Bootstrap has many utilities, but some of their most signficant features are under the form and layout sections. Below is a summary and preview of the ones that stood out the most to team somthing.

Bootstrap allows you to easily create nice layouts for your forms. Using Bootstrap's grid system allows for an easy and responsive form layout, automatically adjusting to different screen sizes.

In Bootstrap, the col class is used as part of the grid system to create a responsive layout. It takes the form of >div class="col-md-4"<. The text after "col-" adjusts the width of elements for different device sizes. You could have extra small (".col-"), small (".col-sm-"), medium (".col-md-"), large (".col-lg-"), and extra larger (".col-xl-"). The number that follows it indicates how many columns an element should span. The Bootstrap grid is divided into 12 columns, and the numbers (1 to 12) define how much space an element should take on a row.

Gutters are the spaces between columns, providing better visual separation between elements. Bootstrap's `g-number` classes (like `g-3`) define the size of these gutters. The number in g-number ranges from 0 to 5, where g-0 means no gutter space between columns and g-1 through g-5 progressively increase the gutter size. The gutter system ensures a clean and consistent layout across different screen sizes.

You can also create drop down menus easily with Bootstrap by using the "form-select" class. In addition you can make certain values disabled. In this case, "Choose..." is disabled. This is done by writing >option selected disabled value=""<Choose...>/option<. The rest of the values for the drop down can be added just by writing >option<Whatever You Want>/option<.

Validation feedback in Bootstrap forms is a feature that provides real-time visual cues to users about the correctness of their input. It is implemented using classes like valid-feedback and invalid-feedback, which display messages when form fields meet or do not meet specific requirements. For example, when a user submits a form without filling in a required field or enters an incorrect format (such as an invalid email address), the invalid-feedback element will show a message to prompt the user to correct their input. Similarly, valid-feedback can be used to indicate that the input is correct.
