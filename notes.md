# Notes about API

<details>
<summary> question here </summary>
answer here
</details>


1. What is an API with a real world example ?

API : Application programming interface. When referencing to API we are talking about sub-section of APIs ie., Web APIs. Its a kind of software that links between frontend and backend.

Web API's protocol = HTTP

Best analogy is customer ordering some food in a resturant
customer = frontend
waiter = API
kithen = backend


When you open a mobile app, and click some button ex, login button
i) mobile app will get your request (customer)
ii) mobile app will pass it to an API (waiter)
iii) API pass on this request to backend for processing (kitchen)
 

2. Main Advantages of API 

i) API provides a common platform for creating apps/websites 
    Ex: we can build ios,android,desktop apps, websites on the same platform.

ii) Automation : because we have built apps and websites on the same platform, it would be easy to perform operations on these things.

iii) Wider audiance : if we give APIs to the clients, they can personalize and build website/apps based on their requirements

iv) Integration : For example, we have a website. we can integrate google/apple/facebook apis for OAuth so we are making user experience better by integrating apps.

(Benefits of APIs - in depth version)[https://blog.api.rakuten.net/api-benefits/]
(Advantages of APIs - in short version)[https://www.bbvaapimarket.com/en/api-world/8-advantages-apis-developers/]
(Benefits of APIs - medium version)[https://digital.gov/2013/03/12/benefits-of-apis/]

Disadvantages of APIs

i) Prone to security issues 

ii) Dependency syndrome
    eg: if API is slow -> app is slow

        if API is compromised -> data is at risk

        if API is down -> app will be down

iii) Managing APIs is difficult

3. What are endpoints wrt to API ?

API endpoints are like the URLs that clients will be exposed, so when someone hits those endpoints, API will pass that request to backend. Then it serves back to the frontend as per the backend logic

4. Types of API and types of API architecture ?

Types of API

i) Open APIs 
    - public APIs

ii) Partner APIs
    - B2B, only authorized parties can access those APIs 

iii) Internal APIs
    - access within the organization

iv) Composite APIs
    - combine 2 or more APIs together

Types of API architecture (still add more summary)
i) REST
    - <diagram>
    - works with XML, JSON, HTTP, plain text
    - modest security
    - ligtweight and consume low bandwidth
    - works well with data
    - popularity ??? 
    - use case ???

ii) SOAP
    - <diagram>
    - works with XML by design
    - advanced security
    - more bandwidth
    - works well with processes
    - popularity ???
    - use case ???

iii) RPC
    - <diagram>

(API types and architecture)[https://blog.hubspot.com/website/types-of-apis]
(API types and architecture)[https://www.techtarget.com/searchapparchitecture/tip/What-are-the-types-of-APIs-and-their-differences]

5. What is REST API ?


6. What is JSON, XML, GraphQL ?

7. What are tools like postman do ? OR what tools and extensions to use while building an API ?

8. API documentation generator : Swagger -> explore this