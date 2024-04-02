function updateStyle() {
    // Find the element
    let selectedDiv = document.getElementsByClassName("service");
    selectedDiv[0].style.backgroundColor = "#fff";
    selectedDiv[0].style.color = "#000";
    console.log(selectedDiv);
}

function updateStyle2() {
    // Find the element
    let selectedDiv = document.getElementsByClassName("service");
    selectedDiv[0].style.backgroundColor = "#f86121";
    selectedDiv[0].style.color = "#fff";
    console.log(selectedDiv);
}

function resetStyle() {
    // Find the element
    let selectedDiv = document.getElementsByClassName("service");
    selectedDiv[0].style.backgroundColor = "#fff";
    selectedDiv[0].style.color = "#000";
    console.log(selectedDiv);
}

// Function to show side-bar navigation on smaller screens
function showSidebar() {
const sidebar = document.getElementById('side-bar');
sidebar.style.display = "flex";
}

function hideSidebar() {
    const sidebar = document.getElementById('side-bar');
    sidebar.style.display = 'none';
}


