function mockingMe() {
  var name = document.getElementById('mockingMeNameInput').value
  var url = "/mocking/" + name
  window.open(url, '_blank')
}

function mockingBird() {

  var request = new XMLHttpRequest();
  request.open('GET', '/mockingbird/sing', true);

  request.onload = function() {
    if (request.status >= 200 && request.status < 400) {
      // Success!
      document.querySelector('#challenge2 .result').textContent = request.responseText;
    } else {
      // We reached our target server, but it returned an error
      document.querySelector('#challenge2 .result').textContent = "There was an error with the request"
    }
  };

  request.onerror = function() {
    // There was a connection error of some sort
    document.querySelector('#challenge2 .result').textContent = "There was an error with the request"
  };

  request.send();

}

function mockingJay() {

  var name = document.getElementById('mockingJayNameInput').value
  var url = "/mockingjay/encounter/" + name
  var request = new XMLHttpRequest();
  request.open('GET', url, true);

  request.onload = function() {
    if (request.status >= 200 && request.status < 400) {
      // Success!
      document.querySelector('#challenge3 .result').textContent = request.responseText;
    } else {
      // We reached our target server, but it returned an error
      document.querySelector('#challenge3 .result').textContent = "There was an error with the request"
    }
  };

  request.onerror = function() {
    // There was a connection error of some sort
    document.querySelector('#challenge3 .result').textContent = "There was an error with the request"
  };

  request.send();

}
