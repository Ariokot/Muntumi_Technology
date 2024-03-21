const mainSections = document.querySelectorAll("header, section, footer");
//console.log(mainSections);

const sections = [];

mainSections.forEach(function(item, index, array) {
    let section = item.className.split(' ')[0];
    sections.push(section);

    // Check if we're at the last item in the array
    if (index === array.length - 1) {
        sendFetchRequest(sections);
    }
});

//console.log(sections);

// To send sections array to the flask web server:
// Define a fetch function and evoke it using the window.onload event
function sendFetchRequest(sections) {
    fetch("/sections", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body:JSON.stringify({sections:sections}),
    })
};

console.log(sections);



