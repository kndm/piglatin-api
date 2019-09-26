# Pig Latin Translation API
This simple API will convert a given text into pig latin. It accepts text in the body of a POST request and returns the translation in the content of the response.

## Pre-requisites
Python 2.7
pip

## Libraries 
Pig Latin for Easy Solar uses the following libraries:
* [Falcon](https://falconframework.org/) 
* [Gunicorn](http://gunicorn.org/)

## Deployment
### Via docker-compose
Install docker-compose via pip with the following command.
```bash
pip install docker-compose
```

Just run the following command to get the API up and running quickly.
```bash
docker-compose start
```

The service listens by default on port 80. We can verify that everything went well by visiting http://localhost:80/ where we should see the service's introduction.

### Via Kubernetes
We assume that the user can access kubectl with basic use of minikube as the focus os this readme is building/launching locally.

The following Kubernetes manifests can be found in the root dir
```bash
myservice-deployment.yaml
myservice-service.yaml
```


## API Architecture
### ENDPOINTS
`/translate`

### Methods Available
`POST`

### Request Body Structure
```js
{
    "text": string
}
```
The value of `text` must have length of at least 1.

### Responses
#### Success
* **Code:** `200 OK`
* **Content:**
```js
{
    "translation": string
}
```

#### Error 
* **Code:** Varies, `4xx` to `5xx`
* **Content:**
```js
{
    "title": string,
    ["description": string]

}
```

## Accessing the API 
Two clients to easily access the API can be found in the /clients/ dir to make sure that our API is working through both Python and JS requests.

### Via the Python client
A simple script that prompts the user for the desired word to translate. Execute the following command while located in the /clients/ dir in order to run the script.

```bash
python API-client.py
```

### Via the JS client
An index.html can be accessed for ease of visualization, response can be seen in the bottom textarea as well as the desired browser's console.


## Test Coverage
Basic test coverage has been added for the API, Middlewares as well as helpers.

To run them, you can run
```bash
docker run --rm kevindamato/piglatin python tests/$TESTFILE
```
where $TESTFILE is the name of one of the test suites found in the dir (e.g. piglatin_test.py)




