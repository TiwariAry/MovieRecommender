document.addEventListener("DOMContentLoaded", function() {
    // Function to determine time zone offset
    function getTimeZoneOffset() {
        const date = new Date();
        return date.getTimezoneOffset() / 60; // Convert minutes to hours
    }

    // Function to get current time in IST
    function getCurrentTimeIST() {
        const now = new Date();
        const offset = 5.5; // IST offset from UTC
        const utc = now.getTime() + (now.getTimezoneOffset() * 60000);
        return new Date(utc + (3600000 * offset));
    }

    // Function to determine background image based on time
    function setBackground() {
        const currentTimeIST = getCurrentTimeIST();
        const hours = currentTimeIST.getHours();
        let folderName;

        // Determine folder based on time
        if (hours >= 4 && hours < 10) {
            folderName = "morning";
        } else if (hours >= 10 && hours < 16) {
            folderName = "afternoon";
        } else if (hours >= 16 && hours < 21) {
            folderName = "evening";
        } else {
            folderName = "night";
        }

        // Construct URL for image based on folder and random image selection
        const imagePath = `/static/image/${folderName}/image${Math.floor(Math.random() * 5) + 1}.jpg`;

        // Set background image
        document.body.style.backgroundImage = `url(${imagePath})`;
    }

    // Call function to set background image
    setBackground();
});
