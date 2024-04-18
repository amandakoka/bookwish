# BookWish Testing

1. [Testing](#testing)
    1. [HTML Validation](#html-validation) 
    2. [CSS Validation](#css-validation) 
    3. [JavaScript Validation](#javascript-validation) 
    4. [Python Validation](#python-validation)  
    5. [Lighthouse](#lighthouse) 
    6. [Testing user stories](#testing-user-stories) 
2. [Bugs](#bugs) 
    1. [Solved Bugs](#solved-bugs)
    2. [Known Bugs](#known-bugs)

## HTML validation
## CSS validation
## JavaScript validation
## Python validation
## Lighthouse
## Testing user stories
## Bugs
### Solved Bugs
 **Bug** | **Fix** |
| ----------- | ----------- |
| While implementing the wishlist route, I encountered a bug where the wishlist page always displayed an empty list of books, despite adding books to the database. This occurred because I mistakenly placed the return statement above the database query to fetch the list of books. As a result, the query to retrieve the books was never executed, causing the wishlist page to render without any book data.| To resolve this issue, I moved the return statement below the database query, ensuring that the query to fetch the list of books is executed before rendering the wishlist page. This correction allowed the wishlist page to display the correct list of books, restoring the functionality of the wishlist feature. By addressing this bug, I ensured that users can properly view and manage their wishlist, enhancing the overall usability and effectiveness of the application.|
| After implementing user signup functionality, I encountered an error when submitting the signup form. The error message indicated that the password exceeded the maximum allowed length. This issue arose because the hashed password exceeded the length limit specified in the user model, resulting in validation failure during form submission.| To address this issue, I adjusted the maximum length constraint for passwords in the user model to accommodate longer hashed passwords. By increasing the length limit, I ensured compatibility with the hashed password format while maintaining security standards. After making this modification, the signup form successfully processed passwords of any length within the new constraint, resolving the validation error.|
| [Edit Book Route Bug](documentation/testing/bugs/edit_book.png) I encountered a bug while creating the edit_book route, where the book_id was undefined, leading to errors during execution. This issue happened because I forgot to pass the book_id parameter in the return render_template function, despite passing the book object. As a result, attempting to run the route triggered an error message. | To address this issue, I ensured the inclusion of the book_id parameter in the template rendering process. This resolved the error, enabling seamless functionality of the edit_book route for manipulating book details. |
| When attempting to edit a book, I noticed that the content areas were initially blank instead of displaying the existing book details. This required users to rewrite everything, which was inefficient and prone to errors.| To resolve this, I updated the edit_book.html template to include the 'value' attribute for each input field. For example, I added value="{{ book.book_title }}" to ensure that the current book title is displayed in the input field when editing. By prefilling the input fields with existing book details, users can easily make modifications without having to re-enter all the information, thus improving the editing experience and reducing the likelihood of errors.|
| [Background Bug](documentation/testing/bugs/bgbug.png) I encountered a bug where the background wasn't covering the whole background as a whole, it was split at each end of the form. This occurred because the CSS classes I initially used didn't produce the desired effect.| To fix this, I modified the CSS by including it directly in the body of the HTML document. This adjustment ensured that the background covered the entire background resolving the split background problem. By integrating the CSS directly into the body, I ensured consistent application of the background styling, therefor improving the overall visual coherence of the website.|
| [Card Size Bug](documentation/testing/bugs/cardsize.png) I encountered a bug where adding books for testing revealed that cards with more content appeared longer than others, resulting in inconsistent card sizes. This occurred due to the absence of styling to ensure uniform card dimensions. | To address this issue, I implemented wishlist card styling to ensure all cards on the wishlist page are of uniform size. This allows users to scroll through cards with extensive content while maintaining visual consistency. By applying this styling, I ensured the consistency of card sizes, improving both the aesthetics and accessibility of the page. |
| [Double Message Bug](documentation/testing/bugs/double_messages.png)  I encountered a bug where submitting forms resulted in flash messages appearing twice on the page. This occurred because I mistakenly placed a flash message in my base.html instead of my welcome.html. The intended behavior was for the message to appear only when a user logs out of their account and is redirected to the welcome page. | To resolve this issue, I removed the flash message from my base.html and relocated it to my welcome.html. This ensures that the message is displayed correctly only on the welcome page after a user logs out, eliminating the duplication of flash messages. |

### Known Bugs
