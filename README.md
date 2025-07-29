# Aigeon AI Zillow Working API

## Project Description

The Aigeon AI Zillow Working API is a Python-based server application designed to interact with Zillow's property data. It provides a set of tools to retrieve property details using various inputs such as property addresses, ZPIDs (Zillow Property IDs), and Zillow URLs. Additionally, it offers functionality for property search and autocomplete features, making it a comprehensive solution for accessing Zillow's real estate data.

## Features Overview

This API server provides several key features to facilitate interaction with Zillow's data:

- Retrieve property details by property address.
- Fetch property information using ZPID.
- Obtain property data through Zillow URLs.
- Autocomplete functionality for search queries.
- Advanced search capabilities based on location, listing status, and various filters.

## Main Features and Functionality

The Aigeon AI Zillow Working API offers the following main functionalities:

1. **Property Details by Address**: Retrieve detailed property information by providing a specific property address.
2. **Property Details by ZPID**: Access property details using the unique ZPID associated with a property.
3. **Property Details by Zillow URL**: Fetch property information directly from a Zillow URL.
4. **Autocomplete Search**: Utilize Zillow's search box autocomplete data to enhance search queries.
5. **Advanced Property Search**: Perform comprehensive property searches with multiple filters, including location, listing status, price range, and more.

## Main Functions Description

### `by_property_address`

- **Description**: Retrieves property details using a given property address.
- **Parameters**:
  - `propertyaddress`: The address of the property (e.g., "3 W Forest Dr, Rochester, NY 14624").

### `by_zpid`

- **Description**: Fetches property details using the ZPID.
- **Parameters**:
  - `zpid`: The Zillow Property ID (e.g., "30907787").

### `by_zillow_url`

- **Description**: Obtains property details from a Zillow URL.
- **Parameters**:
  - `url`: The Zillow URL of the property.

### `autocomplete`

- **Description**: Provides autocomplete suggestions for search queries.
- **Parameters**:
  - `query`: The search query string.

### `search_byaddress`

- **Description**: Performs an advanced property search based on various criteria.
- **Parameters**:
  - `location`: Address, neighborhood, city, or ZIP code.
  - `listingStatus`: Type of property data to find (e.g., 'For_Sale', 'For_Rent', 'Sold').
  - `page`: Page number for paginated results.
  - `sortOrder`: Order in which to sort search results.
  - `listPriceRange`: Price range for the search.
  - `monthlyPayment`: Monthly payment range (for 'For_Sale' listings).
  - `downPayment`: Down payment amount (for 'For_Sale' listings).
  - `bed_min`: Minimum number of bedrooms.
  - `bed_max`: Maximum number of bedrooms.
  - `bathrooms`: Number of bathrooms.
  - `homeType`: Type of home (e.g., Houses, Apartments).
  - `space`: Type of space (for 'For_Rent' listings).
  - `maxHOA`: Maximum HOA fee.
  - `incIncompleteHOA`: Include homes with incomplete HOA data.
  - `listingType`: Type of listing (e.g., 'By_Agent').
  - `listingTypeOptions`: Options for listing type.
  - `propertyStatus`: Status of the property.

This API server is designed to provide robust access to Zillow's real estate data, offering a variety of tools for retrieving and searching property information efficiently.