import { addPost } from "../apiCalls.js";

const form = document.getElementById("post-form");
form.addEventListener("submit", (e) => {
    e.preventDefault();
    console.log("submit");
    const image = document.getElementById("image_field").files[0];
    const description = document.getElementById("description_field").value;
    const csrfToken = document.getElementsByName("csrfmiddlewaretoken").value

    const formData = new FormData(this);
    formData.append("image", image);
    formData.append("description", description);

    addPost(formData, csrfToken).then((res) => {
        console.log(res);
    });
});
