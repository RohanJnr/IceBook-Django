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

