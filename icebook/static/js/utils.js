import { iconClassNames } from "./variables.js";


export const toggleSpinner = () => {
    const spinner = document.querySelector(".spinner")
    spinner.classList.toggle("active")
}

export const getCSRF = () => {
    return document.cookie.split(";").map(el => el.split("=")).find(element => {
        if (element[0] === "csrftoken") {
            return element
        }
    })[1]
}

export const toggleLike = async (e) => {
    const postID = e.target.getAttribute("data-id");
    try {
        const response = await fetch(`/api/toggle-like/${postID}`);
        const result = await response.json();
        e.target.classList.toggle(iconClassNames.likedToggle);
        const likesNumSpan = document.querySelector(`.likes-no.post-${postID}`);

        if (result.has_liked) {
            likesNumSpan.innerText = +likesNumSpan.innerText + 1;
        } else {
            likesNumSpan.innerText = +likesNumSpan.innerText - 1;
        }
    } catch (error) {
        alert(error);
    }
};