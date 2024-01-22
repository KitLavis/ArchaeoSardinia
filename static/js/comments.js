/**
 * Adds edit and delete functionality to comments
 * Original code from the Code Institute Django blog
 * https://github.com/Code-Institute-Solutions/blog/blob/main/15_testing/static/js/comments.js
 */
const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_content");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
 * Adds edit functionality to pencil icons
 * On click it recieves the respective comment's ID
 * Populates the comment content area with current content
 * Changes submit button to say update
 * Sets the form's action to `edit_comment/${commentId}`
 */
for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id");
        let commentContent = document.getElementById(`comment${commentId}`).innerText;
        commentText.value = commentContent;
        submitButton.innerText = "Update";
        commentForm.setAttribute("action", `edit_comment/${commentId}`);
    });
}

/**
 * Adds delete functionality to dustbin icons
 * On click it recieves the respective comment's ID
 * Changes deleteConfirm href to respective comments deletion endpoint
 * Displays the delete confirmation modal
 */
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id");
        deleteConfirm.href = `delete_comment/${commentId}`;
        deleteModal.show();
    });
}