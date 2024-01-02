# Placeholder Image Generator

## **Overview**

This Python-based AWS Lambda function dynamically generates placeholder images based on specified dimensions. The dimensions are provided through a URL parameter in the format **`/{width}x{height}`**, for example, **`/300x100`**. The generated image contains the dimensions as text, centered within the image.

## **Example**
![300x120](https://github.com/lucasayb/lucasyamamoto.placeholder-generator/assets/17356081/642fb193-8adb-4d48-8fc6-597f99677215)

## **Features**

- **Dynamic Placeholder Image Generation:** Creates images with custom dimensions and text indicating those dimensions.
- **URL-Based Parameters:** Dimensions are specified via a URL parameter in the format **`/{width}x{height}`**.
- **Custom Fonts:** Uses a custom font (Arial Narrow) for text rendering within the image.

## **Requirements**

- Python >= 3.9
- Node >= 18.12.0
- AWS Lambda for hosting and executing the function.
- The 'serverless' framework for deployment and offline debugging.

## **Local Development and Debugging**

- **Serverless Offline:** The project is configured to use **`serverless-offline`** for local development and debugging. This allows for simulating the AWS Lambda environment on your local machine.

## **Deployment**

- **Deploy to Production:** Use the command **`serverless deploy --stage prod`** to deploy the application to the production environment.

## **Functionality**

### **`generate_image(image_width, image_height, image_name)`**

Generates an image of specified width and height. The image displays the dimensions as text.

### Parameters

- **`image_width`** (str): Width of the image.
- **`image_height`** (str): Height of the image.
- **`image_name`** (str): Text to be displayed on the image, typically the dimensions.

### **`render_image(image_bytes, status_code)`**

Prepares the generated image for HTTP response.

### Parameters

- **`image_bytes`** (bytes): Byte stream of the generated image.
- **`status_code`** (int): HTTP status code for the response.

### **`placeholder(event, context)`**

Lambda function handler. Extracts dimensions from the URL, generates the image, and returns it in the HTTP response.

### Parameters

- **`event`** (dict): Contains the request details and parameters.
- **`context`**: AWS Lambda context object (not used in this function).

## **Example Usage**

- Deploy the Lambda function.
- Make a request to the Lambda URL with the desired dimensions, e.g., **`https://your-lambda-url.com/300x100`**.
- The function will return a 300x100 image with "300x100" text displayed in the center.
