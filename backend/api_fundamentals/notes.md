# API Learning Log

**Course:** Introduction to APIs in Python  
**Platform:** DataCamp  
**Date:** 10 October 2026  
**Chapter:** Making API Requests with Python  
**Status:** In progress

## 1. Concepts Learned

- Web APIs enable software applications to communicate through defined interfaces.
- HTTP defines how clients and servers exchange requests and responses.
- Python provides `urllib` for HTTP operations in its standard library and third-party libraries such as `requests`.
- HTTP methods communicate the intended operation on a resource.
- URLs, headers, query parameters and status codes are essential parts of HTTP communication.

## 2. How APIs Work

An API defines how one software component interacts with another. A Web API commonly exposes resources or operations over HTTP.

1. A client sends an HTTP request to a server.
2. The server processes the request.
3. The server returns an HTTP response containing a status code, headers and, where applicable, a response body.

For example, a frontend can request a list of tasks from a Python backend. The backend returns the task data as JSON, which JavaScript can process and display.

## 3. Web APIs, Clients and Servers

- **Client:** Initiates a request, such as a browser or Python program.
- **Server:** Receives requests and returns responses.
- **Web API:** Defines how clients interact with services over the web.

### Types of Web APIs

1. **REST:** An architectural style commonly used to build web APIs around resources and standard HTTP semantics.
2. **SOAP:** A protocol with structured messaging conventions.
3. **GraphQL:** A query language and runtime approach that lets clients request specific data.

These approaches have different design goals and trade-offs; none is universally optimal for every application.

## 4. Python Libraries for APIs

### 4.1 `urllib`

`urllib` is included in Python's standard library. It provides HTTP and URL-handling functionality, although its interface can require more explicit code.

```python
from urllib.request import urlopen

url = "https://httpbin.org/get"

with urlopen(url, timeout=10) as response:
    data = response.read()
    text = data.decode("utf-8")
    print(text)
```

### 4.2 `requests`

`requests` is a third-party library that provides a convenient interface for sending HTTP requests.

```python
import requests

response = requests.get(
    "https://httpbin.org/get",
    timeout=10
)

print(response.status_code)
print(response.text)
```

The response object provides access to the status code, headers, body and other response information.

## 5. Anatomy of a URL

A URL identifies the location of a resource.

Example:

`http://example.com:8080/unit/243?floor=77`

- **Scheme:** `http` specifies the protocol.
- **Host:** `example.com` identifies the host.
- **Port:** `8080` identifies the port. The port is optional in a URL; HTTP commonly uses 80 by default and HTTPS uses 443.
- **Path:** `/unit/243` identifies a resource or route.
- **Query string:** `?floor=77` supplies an additional parameter.

An office-building analogy helps illustrate this: the host is the building's address, the port is an entry point, the path identifies an office, and the query supplies additional instructions.

### Query parameters with `requests`

The `params` argument accepts a dictionary of query parameters.

```python
import requests

query_params = {
    "floor": 77,
    "elevator": True
}

response = requests.get(
    "https://httpbin.org/get",
    params=query_params,
    timeout=10
)

print(response.url)
```

The resulting URL contains the encoded query parameters.

## 6. HTTP Methods

HTTP methods indicate the intended operation.

| Method | Typical purpose |
|---|---|
| `GET` | Retrieve a resource |
| `POST` | Submit data, often to create a resource or trigger an operation |
| `PUT` | Replace the target resource's representation |
| `PATCH` | Apply a partial modification |
| `DELETE` | Request deletion of a resource |

Using a mailbox analogy, `GET` checks the mailbox, `POST` delivers a new package, `PUT` replaces the contents, `PATCH` modifies part of the contents, and `DELETE` removes the resource.

### Examples with `requests`

```python
import requests

url = "https://httpbin.org/anything"

# Retrieve information
response = requests.get(url, timeout=10)

# Submit form data
response = requests.post(
    url,
    data={"key": "value"},
    timeout=10
)

# Replace or update a resource
response = requests.put(
    url,
    data={"key": "new value"},
    timeout=10
)

# Delete a resource
response = requests.delete(url, timeout=10)
```

These examples demonstrate request construction; the test endpoint does not represent a persistent resource store.

The `data` argument can send form-encoded data. For a JSON request body, use `json=`, for example `json={"key": "value"}`.

## 7. HTTP Headers and Status Codes

HTTP messages contain a start-line, headers and an optional body.

- **Start-line:** Identifies the request method and target, or the response status.
- **Headers:** Carry metadata as name-value pairs.
- **Body:** Contains the submitted data or returned representation when present.

### Content negotiation

The `Accept` request header indicates which response media types a client prefers. The `Content-Type` response header identifies the media type of the returned body.

```python
import requests

response = requests.get(
    "https://httpbin.org/get",
    headers={"Accept": "application/json"},
    timeout=10
)

print(response.headers.get("Content-Type"))
```

A server may return a different representation or reject the request, depending on its behavior. Sending an `Accept` header does not guarantee JSON.

### Status-code classes

| Range | Meaning |
|---|---|
| `1xx` | Informational |
| `2xx` | Successful |
| `3xx` | Redirection |
| `4xx` | Client error |
| `5xx` | Server error |

Common examples:

- `200 OK`: The request succeeded.
- `201 Created`: A resource was created.
- `400 Bad Request`: The request was invalid.
- `401 Unauthorized`: Authentication is required or failed.
- `403 Forbidden`: The server refuses the requested operation.
- `404 Not Found`: The requested resource was not found.
- `500 Internal Server Error`: The server encountered an unexpected error.

### Inspecting a response

Read the actual status code from the response object.

```python
import requests

response = requests.get(
    "https://httpbin.org/get",
    timeout=10
)

print(response.status_code)
print(response.headers.get("Content-Type"))
```

Do not assign a status code to `response.status_code`. It describes the response received from the server.

The `requests.codes` collection provides aliases for common status codes; it does not report the status of a particular request.

## 8. Practical Implementation

**Exercise 1: Successful GET request**

- Endpoint: `https://httpbin.org/get`
- Action: Send a GET request.
- Record: Actual status code and `Content-Type` header.
- Expected result: Normally HTTP `200` with a JSON response.

**Exercise 2: Missing-resource response**

- Endpoint: `https://httpbin.org/status/404`
- Action: Send a GET request.
- Record: Actual status code.
- Expected result: HTTP `404`.

**Status:** Pending execution. No observed output has been recorded yet.

Use a request timeout and handle network exceptions. Actual results should be recorded after running the exercises.

## 9. What I Understand

To be completed after independently explaining and implementing the exercises.

## 10. Remaining Questions

- How do I distinguish a successful HTTP response from a successful application operation?
- How should a client handle network errors and unsuccessful status codes?
- How does a Python application expose its own endpoints instead of only consuming existing APIs?

## 11. Next Action

1. Implement and run the two response-inspection exercises.
2. Record the actual output.
3. Continue the course's remaining exercises on headers, status codes, JSON, authentication and error handling.
4. Begin building API endpoints with FastAPI after completing the relevant introductory material.