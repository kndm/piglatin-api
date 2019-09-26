var xhr = new XMLHttpRequest();

// Setup listener to process requests that went through
xhr.onload = function () {
	// Process return data
	if (xhr.status >= 200 && xhr.status < 300) {
        console.log('Success!', xhr.responseText);
        document.getElementById('resultbox').value ='Success!\n' + '\n' + xhr.responseText;
	} else {
		// What do when the request fails
        console.log('The request failed!');
        document.getElementById('resultbox').value = 'The request has failed';
	}


};

function submitTranslation() {
var word = document.querySelector('textarea').value;
if (word) {
    xhr.open('POST', 'http://localhost:80/translate');
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify({ "text": word,}))
    }
}


var submitBtn = document.querySelector('button');
submitBtn.addEventListener('click', submitTranslation);
