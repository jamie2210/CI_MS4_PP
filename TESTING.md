# __Poster Prints Testing__

![Mockup image](documentation/images/device-display.jpg)

[Live webpage](https://poster-prints-8ff329d79ba2.herokuapp.com/)

## __Contents__

1. [Automated Testing](#automated-testing)
1. [Validation Testing](#validation-testing)
    * [HTML Validation](#HTML-validation)
    * [CSS Validation](#CSS-validation)
    * [JavaScript Validation](#javascript-validation)
    * [Python Validation](#python-validation)
    * [Accessibility](#accessibility)
    * [Performance](#performance)
2. [Manual Testing](#manuel-testing)
    * [Device Testing](#device-testing)
    * [Browser Compatibility](#browser-compatibility)
    * [Testing User Stories](#testing-user-stories)
3. [Bugs](#bugs)

I consistently tested throughout the build of the project with Chrome developer tools, utilising print statements in python, writing unit tests for models, views and forms and checking for device compatibility at each stage of the development.

## Automated Testing

_ _ _

- I wrote a number of unit tests(32) using the Django unit test framework [Django TestCase](https://docs.djangoproject.com/en/4.1/topics/testing/overview/)

- I also used [coverage](https://pypi.org/project/coverage/) throughout for feedback on test written.

- This is an area I look forward to learning more about and utilising as I progress as a developer as it's an area I know I can improve. I know it will prove more and more useful helping me write more robust and tested code for future projects.

### Coverage Testing

| App | Coverage | Results |
| :---| :--- | :--- |
| Home | 100% | [Coverage Home](documentation/testing/coverage/coverage-home.png) |
| Products | 69% | [Coverage Products](documentation/testing/coverage/coverage-products.png) |
| Bag | 74% | [Coverage Bag](documentation/testing/coverage/coverage-bag.png) |
| Checkout | 53% | [Coverage Checkout](documentation/testing/coverage/coverage-checkout.png)|
| Contact | 89% | [Coverage Contact](documentation/testing/coverage/coverage-contact.png) |
| Favourites | 69% | [Coverage Products](documentation/testing/coverage/coverage-products.png) |
| Profiles | 65%  | [Coverage Profiles](documentation/testing/coverage/coverage-profiles.png) |

## Validation Testing

### HTML Validation

The W3C Markup Validation Service was used to validate the HTML of the website. All pages pass with no errors.

Home [results]()
Products [results]()
Products Detail [results]()
Favourites [results]()
Profile [results]()
Contact [results]()
Contact Success [results]()
Bag [results]()
Checkout [results]()
Checkout Success [results]()




### CSS Validation

The W3C Jigsaw CSS Validation Service was used to validate the CSS of the website.
When pasting in my index errors and warnings flagged were all linked to Materialize.

When validating just my own custom CSS file it passes with no errors with only 1 warning as it could not read the Google Fonts import.
<details><summary>style.css</summary>
<img src="documentation/testing/css_validation.png">
</details><br>

### JavaScript Validation

JSHint JS Validation Service was used to validate the Javascript files. No significant issues were found. Only undefined variables flagged were those used for the emailjs functions.

OnClick buttons were flagged as unused, but /* exported */ feature was used to remove the flags as they are called in the HTML files.

<details><summary>script.js</summary>
<img src="documentation/testing/jshint.png">
</details><br>

### Python Validation

[pep8ci](#https://pep8ci.herokuapp.com/) was the linter used to check the python code, all clear with no errors.
<br>

<details><summary>Index</summary>
<img src="documentation/testing/linter/index.png">
</details>

<details><summary>Authentication</summary>
<img src="documentation/testing/linter/authentication.png">
</details>

### Accessibility

To ensure the site is accessible as possible I have taken the following steps;

- Using semantic HTML.
- Descriptive alt attributes on images.
- Label functions and links to ensure clarity of the roles of each button, icon or clickable feature.
- Ensuring that there is a sufficient colour contrast throughout the site (There are contrast flags throughout the WAVE reporting but I am happy with the way the site is represented in these case as a low contrast was my intention and part of the design. I am happy with the visibility of each flag so have left them as they are and they are all labelled with descriptions.)

[Wave accessibility](#https://wave.webaim.org/) was used to test the websites accessibility

Logged Out Home [results](https://wave.webaim.org/report#/https://rave-reviews-app.herokuapp.com/)

### Performance

Performance testing was done using lighthouse in chrome developer tools testing the performance, accessibility, best practices, and SEO of the website. Some of the scores are lower than I'd like them to be but for most of them, the lower ones especially, it was from labels or formatting within Materialize I which I could not change so it's not something I'm too worried about.
<br>
<details><summary>Logged Out Home</summary>
<img src="documentation/testing/lighthouse/logged-out-home.png">
</details>


_ _ _

## Manuel Testing

### Device testing
The website was tested on the following devices:
- MacBook Pro
- iPad Tablet
- Google Pixel 5
- iPhone 12

In addition, the website was tested using Google Chrome Developer Tools device toggle option for all available device options.

### Browser Compatibility

The website was tested on the following browsers:
- Google Chrome
- Apple Safari
- Mozilla Firefox

_ _ _

### Developer Feature Testing

| Feature | Testing Performed | Pass/Fail |
| --- | --- | --- |
| Links | Check all links navigate correctly | Pass |


_ _ _

### Testing User Stories

1. As a Shopper I want to be able to view a list of products so that I can select some to purchase.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|  |  |  | Works as expected |

<details><summary>View List</summary>
<img src="documentation/images/features/logged-out-home.png">
</details>
<br>

_ _ _

## Bugs

code ```
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-12 add-product-container">
                <form method="POST" actiom="{% url 'add_product' %}" class="form mb-2" enctype="multipart/form-data">
                    {% csrf_token %}
                    {% for field in form %}
                        {% if field.name != 'image' %}
                            {% if field.name != 'image2' %}
                                {{ field | as_crispy_field }}
                            {% else %}
                                {{ field }}
                            {% endif %}
                        {% else %}
                            {{ field }}
                        {% endif %}
                    {% endfor %}
                    <div class="text-center">
                        <a href="{% url 'products' %}?random=True" class="btn btn-dark rounded border-0 mt-2 mb-2">Cancel</a>
                        <button class="btn btn-dark rounded border-0 mt-2 mb-2">Add Product</button>
                    </div>
                </form>
            </div>
        </div>
    </div>

