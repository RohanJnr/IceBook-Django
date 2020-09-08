import { routes } from "./variables.js";
import { getCSRF } from "./utils.js";

export const addPost = async (formData, csrfToken) => {
    let res = await fetch(routes.addPost, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": csrfToken,
        },
        body: formData,
    });
    return await res.json();
};

export const fetchComments = async (postID) => {
    // send GET request for comments on a specific post.
    try {
        let res = await fetch(routes.getComments(postID));
        return await res.json();
    } catch (error) {
        alert(error);
    }
};

export const postComment = async (comment, postID) => {
    const csrfToken = getCSRF();
    const response = await fetch(routes.postComment, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": csrfToken,
        },
        body: JSON.stringify({ comment: comment, post: postID }),
    });
    return await response.json();
};

export const getPosts = async () => {
    try {
        let res = await fetch("/api/posts");
        let posts = await res.json();
        return posts;
    } catch (error) {
        alert(error);
    }
};
